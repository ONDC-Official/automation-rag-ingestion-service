"""
models.py — Dataclasses for all Knowledge Graph node and edge types.

Node identity conventions:
- DomainNode:     name + version  (e.g. "ONDC:FIS12" + "2.3.0")
- ActionNode:     name + domain + version  (same action name exists in every domain)
- GroupNode:      name + action + domain + version
- RuleNode:       name + action + domain + version
- FieldNode:      jsonpath  (global — shared across domains)
- EnumValueNode:  value     (global)
- PatternNode:    pattern   (global)
- OperatorNode:   name      (global)
- SessionKeyNode: key + saved_by_action + domain + version
"""

from dataclasses import dataclass, field
from typing import Optional, List


# ---------------------------------------------------------------------------
# Nodes
# ---------------------------------------------------------------------------


@dataclass
class DomainNode:
    name: str           # e.g. "ONDC:FIS12"
    version: str        # e.g. "2.3.0"
    code_name: str = "L1validations"


@dataclass
class ActionNode:
    name: str           # e.g. "search", "on_confirm"
    direction: str      # "BAP_TO_BPP" or "BPP_TO_BAP"
    domain: str         # domain name  ← part of identity
    version: str        # version string  ← part of identity


@dataclass
class GroupNode:
    name: str           # _NAME_ value
    action: str         # which action it belongs to
    domain: str         # ← part of identity
    version: str        # ← part of identity
    depth: int          # nesting depth (0 = direct child of _TESTS_[action])
    scope: Optional[str]            # _SCOPE_ value if present
    continue_expr: Optional[str]    # _CONTINUE_ expression if present
    source_file: str                # filename it came from


@dataclass
class RuleNode:
    name: str           # _NAME_ value
    action: str
    domain: str         # ← part of identity
    version: str        # ← part of identity
    rule_type: List[str]  # e.g. ["PRESENCE"], ["CROSS_REQUEST", "COMPARISON"]
    return_expr: str    # full _RETURN_ expression string
    continue_expr: Optional[str]
    scope: Optional[str]
    error_code: Optional[int]
    description: Optional[str]
    source_file: str
    is_optional: bool   # True if _CONTINUE_ contains "are present" skip-if-absent pattern


@dataclass
class FieldNode:
    jsonpath: str                   # normalised JSONPath, e.g. "$.context.domain"
    field_segment: str              # last meaningful segment, e.g. "domain"


@dataclass
class EnumValueNode:
    value: str
    value_lower: str


@dataclass
class PatternNode:
    pattern: str


@dataclass
class OperatorNode:
    name: str           # e.g. "are present", "all in", "follow regex"
    operator_type: str  # "UNARY" or "BINARY"
    description: str


@dataclass
class SessionKeyNode:
    key: str            # e.g. "transaction_id"
    saved_by_action: str
    domain: str         # ← part of identity
    version: str        # ← part of identity
    jsonpath: str       # JSONPath used to extract it


# ---------------------------------------------------------------------------
# Edge
# ---------------------------------------------------------------------------


@dataclass
class Edge:
    from_id: str        # canonical identifier for the source node
    rel_type: str       # relationship label
    to_id: str          # canonical identifier for the target node
    properties: dict = field(default_factory=dict)


# ---------------------------------------------------------------------------
# Extraction result — single container returned by extractor
# ---------------------------------------------------------------------------


@dataclass
class ExtractionResult:
    domains: list[DomainNode] = field(default_factory=list)
    actions: list[ActionNode] = field(default_factory=list)
    groups: list[GroupNode] = field(default_factory=list)
    rules: list[RuleNode] = field(default_factory=list)
    fields: list[FieldNode] = field(default_factory=list)
    enum_values: list[EnumValueNode] = field(default_factory=list)
    patterns: list[PatternNode] = field(default_factory=list)
    operators: list[OperatorNode] = field(default_factory=list)
    session_keys: list[SessionKeyNode] = field(default_factory=list)
    edges: list[Edge] = field(default_factory=list)
