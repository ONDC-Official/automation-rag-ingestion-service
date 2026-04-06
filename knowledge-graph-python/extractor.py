"""
extractor.py — Walk a parsed JVAL test tree and extract all graph nodes and edges.

Entry point:
    extract(action, domain, version, source_file, tests, session_data) -> ExtractionResult
"""

from typing import Any, Optional

from models import (
    ActionNode,
    DomainNode,
    Edge,
    EnumValueNode,
    ExtractionResult,
    FieldNode,
    GroupNode,
    OperatorNode,
    PatternNode,
    RuleNode,
    SessionKeyNode,
)

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

BAP_TO_BPP_ACTIONS = {
    "search", "select", "init", "confirm",
    "cancel", "track", "update", "status",
}

# Keys that are part of the JVAL DSL structure — not variables
_RESERVED_KEYS = frozenset(
    {
        "_NAME_",
        "_RETURN_",
        "_SCOPE_",
        "_CONTINUE_",
        "_ERROR_CODE_",
        "_SUCCESS_CODE_",
        "_DESCRIPTION_",
    }
)

# Static operator seed data: (name, type, description)
OPERATOR_DEFINITIONS: list[tuple[str, str, str]] = [
    ("are present", "UNARY", "Assert that the referenced attribute(s) exist and are non-null"),
    ("are unique", "UNARY", "Assert that all values in the collection are distinct"),
    ("all in", "BINARY", "Assert that every value in the left operand appears in the right set"),
    ("any in", "BINARY", "Assert that at least one value in the left operand appears in the right set"),
    ("none in", "BINARY", "Assert that no value in the left operand appears in the right set"),
    ("follow regex", "BINARY", "Assert that every value in the left operand matches the right regex"),
    ("equal to", "BINARY", "Assert that the left operand equals the right operand"),
    ("greater than", "BINARY", "Assert that the left operand is greater than the right operand"),
    ("less than", "BINARY", "Assert that the left operand is less than the right operand"),
]

# ---------------------------------------------------------------------------
# Public entry point
# ---------------------------------------------------------------------------


def extract(
    action: str,
    domain: str,
    version: str,
    source_file: str,
    tests: list[dict],
    session_data: dict[str, str],
) -> ExtractionResult:
    """Walk the JVAL test tree for one action and produce an ExtractionResult."""
    result = ExtractionResult()

    # Domain node
    domain_node = DomainNode(name=domain, version=version)
    result.domains.append(domain_node)

    # Action node
    direction = "BAP_TO_BPP" if action in BAP_TO_BPP_ACTIONS else "BPP_TO_BAP"
    action_node = ActionNode(name=action, direction=direction, domain=domain, version=version)
    result.actions.append(action_node)

    # HAS_ACTION edge
    result.edges.append(Edge(
        from_id=_domain_id(domain, version),
        rel_type="HAS_ACTION",
        to_id=_action_id(action, domain, version),
    ))

    # Walk each top-level test object
    for test_obj in tests:
        _walk_test_object(
            obj=test_obj,
            action=action,
            domain=domain,
            version=version,
            parent_name=None,
            parent_is_group=False,
            depth=0,
            source_file=source_file,
            result=result,
        )

    # Session data
    _extract_session_data(action, domain, version, session_data, result)

    # Operator seed nodes (idempotent — same nodes written for every action, MERGE handles it)
    for op_name, op_type, op_desc in OPERATOR_DEFINITIONS:
        result.operators.append(OperatorNode(name=op_name, operator_type=op_type, description=op_desc))

    return result


# ---------------------------------------------------------------------------
# Recursive walker
# ---------------------------------------------------------------------------


def _walk_test_object(
    obj: dict[str, Any],
    action: str,
    domain: str,
    version: str,
    parent_name: Optional[str],
    parent_is_group: bool,
    depth: int,
    source_file: str,
    result: ExtractionResult,
) -> None:
    """Recursively process one test object node."""
    name: str = obj.get("_NAME_", "")
    return_val = obj.get("_RETURN_")
    scope: Optional[str] = obj.get("_SCOPE_")
    continue_expr: Optional[str] = obj.get("_CONTINUE_")

    if isinstance(return_val, list):
        # --- GROUP node ---
        group = GroupNode(
            name=name,
            action=action,
            domain=domain,
            version=version,
            depth=depth,
            scope=scope,
            continue_expr=continue_expr,
            source_file=source_file,
        )
        result.groups.append(group)

        # Link to parent
        if parent_name is None:
            result.edges.append(Edge(
                from_id=_domain_id(domain, version),
                rel_type="HAS_GROUP",
                to_id=_group_id(name, action, domain, version),
            ))
        elif parent_is_group:
            result.edges.append(Edge(
                from_id=_group_id(parent_name, action, domain, version),
                rel_type="CONTAINS_GROUP",
                to_id=_group_id(name, action, domain, version),
            ))
        else:
            result.edges.append(Edge(
                from_id=_domain_id(domain, version),
                rel_type="HAS_GROUP",
                to_id=_group_id(name, action, domain, version),
            ))

        # Recurse into children
        for child in return_val:
            _walk_test_object(
                obj=child,
                action=action,
                domain=domain,
                version=version,
                parent_name=name,
                parent_is_group=True,
                depth=depth + 1,
                source_file=source_file,
                result=result,
            )

    elif isinstance(return_val, str):
        # --- RULE node ---
        error_code_raw = obj.get("_ERROR_CODE_")
        error_code: int = int(error_code_raw) if error_code_raw is not None else 3000
        # Use explicit _DESCRIPTION_ if present, otherwise humanise the rule name so
        # the Neo4j fulltext index has meaningful natural-language tokens to match.
        description: Optional[str] = (
            obj.get("_DESCRIPTION_") or name.replace("_", " ").lower()
        )

        rule_type = _detect_rule_type(obj, return_val)
        is_optional = _is_optional(continue_expr)

        rule = RuleNode(
            name=name,
            action=action,
            domain=domain,
            version=version,
            rule_type=rule_type,
            return_expr=return_val,
            continue_expr=continue_expr,
            scope=scope,
            error_code=error_code,
            description=description,
            source_file=source_file,
            is_optional=is_optional,
        )
        result.rules.append(rule)

        # Link to parent
        if parent_name is None:
            result.edges.append(Edge(
                from_id=_domain_id(domain, version),
                rel_type="HAS_RULE",
                to_id=_rule_id(name, action, domain, version),
            ))
        elif parent_is_group:
            result.edges.append(Edge(
                from_id=_group_id(parent_name, action, domain, version),
                rel_type="CONTAINS_RULE",
                to_id=_rule_id(name, action, domain, version),
            ))
        else:
            result.edges.append(Edge(
                from_id=_domain_id(domain, version),
                rel_type="HAS_RULE",
                to_id=_rule_id(name, action, domain, version),
            ))

        # Extract variables from rule object
        _extract_rule_variables(obj, name, action, domain, version, return_val, result)


# ---------------------------------------------------------------------------
# Variable extraction
# ---------------------------------------------------------------------------


def _extract_rule_variables(
    obj: dict[str, Any],
    rule_name: str,
    action: str,
    domain: str,
    version: str,
    return_expr: str,
    result: ExtractionResult,
) -> None:
    """Extract Field, EnumValue, Pattern nodes and their edges from a rule object."""
    rule_node_id = _rule_id(rule_name, action, domain, version)

    for key, value in obj.items():
        if key in _RESERVED_KEYS:
            continue

        if isinstance(value, str) and value.startswith("$."):
            if value.startswith("$._EXTERNAL."):
                # Cross-request session read
                session_key_str = value[len("$._EXTERNAL."):]
                result.edges.append(Edge(
                    from_id=rule_node_id,
                    rel_type="READS_SESSION",
                    to_id=_session_key_id(session_key_str, action, domain, version),
                    properties={"key": session_key_str},
                ))
            else:
                # Regular JSONPath field (global node — no domain/version in ID)
                field_node = _make_field_node(value)
                result.fields.append(field_node)

                operator_name = _operator_for_variable(key, return_expr)
                optional = _is_optional(obj.get("_CONTINUE_"))

                result.edges.append(Edge(
                    from_id=rule_node_id,
                    rel_type="CHECKS_FIELD",
                    to_id=_field_id(value),
                    properties={"operator": operator_name, "optional": optional},
                ))

        elif isinstance(value, list) and all(isinstance(v, str) for v in value):
            if _is_regex_variable(key, return_expr):
                for pattern_str in value:
                    result.patterns.append(PatternNode(pattern=pattern_str))
                    result.edges.append(Edge(
                        from_id=rule_node_id,
                        rel_type="VALIDATES_REGEX",
                        to_id=_pattern_id(pattern_str),
                    ))
            else:
                op_name = _enum_operator_for_variable(key, return_expr)
                for val_str in value:
                    result.enum_values.append(EnumValueNode(value=val_str, value_lower=val_str.lower()))
                    result.edges.append(Edge(
                        from_id=rule_node_id,
                        rel_type="VALIDATES_ENUM",
                        to_id=_enum_id(val_str),
                        properties={"operator": op_name},
                    ))

    # USES_OPERATOR edges
    for op_name, _, _ in OPERATOR_DEFINITIONS:
        if op_name in return_expr:
            result.edges.append(Edge(
                from_id=rule_node_id,
                rel_type="USES_OPERATOR",
                to_id=_operator_id(op_name),
            ))


# ---------------------------------------------------------------------------
# Session data extraction
# ---------------------------------------------------------------------------


def _extract_session_data(
    action: str,
    domain: str,
    version: str,
    session_data: dict[str, str],
    result: ExtractionResult,
) -> None:
    """Create SessionKey nodes and Action-[:SAVES_SESSION]->SessionKey edges."""
    for key, jsonpath in session_data.items():
        sk = SessionKeyNode(key=key, saved_by_action=action, domain=domain, version=version, jsonpath=jsonpath)
        result.session_keys.append(sk)
        result.edges.append(Edge(
            from_id=_action_id(action, domain, version),
            rel_type="SAVES_SESSION",
            to_id=_session_key_id(key, action, domain, version),
        ))


# ---------------------------------------------------------------------------
# Rule type detection
# ---------------------------------------------------------------------------


def _detect_rule_type(obj: dict[str, Any], return_expr: str) -> list[str]:
    """Classify a leaf rule by inspecting its variables and _RETURN_ expression.

    A rule may match multiple types (e.g. CROSS_REQUEST + COMPARISON).
    """
    types: list[str] = []

    # CROSS_REQUEST: any variable references $._EXTERNAL.
    for key, value in obj.items():
        if key in _RESERVED_KEYS:
            continue
        if isinstance(value, str) and value.startswith("$._EXTERNAL."):
            types.append("CROSS_REQUEST")
            break

    if "follow regex" in return_expr:
        types.append("REGEX")
    if "are unique" in return_expr:
        types.append("UNIQUENESS")
    if any(op in return_expr for op in ("equal to", "greater than", "less than")):
        types.append("COMPARISON")
    if any(op in return_expr for op in ("all in", "any in", "none in")):
        types.append("ENUM")
    if "are present" in return_expr:
        types.append("PRESENCE")

    # Fallback — should not normally occur
    if not types:
        types.append("PRESENCE")

    return types


def _is_optional(continue_expr: Optional[str]) -> bool:
    """Return True if continue_expr represents a skip-if-absent pattern.

    The canonical pattern is: !(attr are present) — meaning "skip this rule if
    the attribute is not present", i.e. the field is optional.
    """
    if not continue_expr:
        return False
    return "are present" in continue_expr and "!" in continue_expr


# ---------------------------------------------------------------------------
# Operator helpers
# ---------------------------------------------------------------------------


def _operator_for_variable(var_name: str, return_expr: str) -> str:
    """Return the operator string that applies to a JSONPath variable in the expression."""
    if "are present" in return_expr:
        return "are present"
    if "are unique" in return_expr:
        return "are unique"
    if "follow regex" in return_expr:
        return "follow regex"
    for op in ("all in", "any in", "none in"):
        if op in return_expr:
            return op
    for op in ("equal to", "greater than", "less than"):
        if op in return_expr:
            return op
    return "are present"


def _enum_operator_for_variable(var_name: str, return_expr: str) -> str:
    """Return the enum operator referenced in the return expression."""
    for op in ("all in", "any in", "none in"):
        if op in return_expr:
            return op
    return "all in"


def _is_regex_variable(var_name: str, return_expr: str) -> bool:
    """Return True if this string-array variable holds regex patterns."""
    return "follow regex" in return_expr and var_name in return_expr


# ---------------------------------------------------------------------------
# Node constructors
# ---------------------------------------------------------------------------


def _make_field_node(jsonpath: str) -> FieldNode:
    segment = _last_field_segment(jsonpath)
    return FieldNode(jsonpath=jsonpath, field_segment=segment)


def _last_field_segment(jsonpath: str) -> str:
    """Extract the last meaningful path segment from a JSONPath string."""
    # Strip filter expressions and array wildcards
    import re
    # Remove filter expressions like [?(...)]
    cleaned = re.sub(r"\[.*?\]", "", jsonpath)
    parts = [p for p in cleaned.split(".") if p and p != "$"]
    return parts[-1] if parts else jsonpath


# ---------------------------------------------------------------------------
# Canonical ID helpers — used consistently for edge from_id / to_id
# ---------------------------------------------------------------------------


def _domain_id(name: str, version: str) -> str:
    return f"domain|{name}|{version}"


def _action_id(name: str, domain: str, version: str) -> str:
    return f"action|{domain}|{version}|{name}"


def _group_id(name: str, action: str, domain: str, version: str) -> str:
    return f"group|{domain}|{version}|{action}|{name}"


def _rule_id(name: str, action: str, domain: str, version: str) -> str:
    return f"rule|{domain}|{version}|{action}|{name}"


def _field_id(jsonpath: str) -> str:
    return f"field|{jsonpath}"


def _enum_id(value: str) -> str:
    return f"enum|{value}"


def _pattern_id(pattern: str) -> str:
    return f"pattern|{pattern}"


def _operator_id(name: str) -> str:
    return f"operator|{name}"


def _session_key_id(key: str, action: str, domain: str, version: str) -> str:
    return f"session|{domain}|{version}|{action}|{key}"
