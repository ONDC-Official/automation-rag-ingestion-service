"""
queries.py — Cypher-based retrieval functions for the ONDC FIS12 knowledge graph.

Each function accepts a KnowledgeGraph instance and returns a list of plain dicts.
No print statements here — callers are responsible for display.
"""

from typing import Any

from graph import KnowledgeGraph


# ---------------------------------------------------------------------------
# 1. All rules that check a given JSONPath
# ---------------------------------------------------------------------------


def rules_for_field(kg: KnowledgeGraph, jsonpath: str) -> list[dict[str, Any]]:
    """Return all rules that reference the given JSONPath field, across all actions."""
    cypher = """
    MATCH (r:Rule)-[cf:CHECKS_FIELD]->(f:Field {jsonpath: $jsonpath})
    RETURN r.name        AS rule_name,
           r.action      AS action,
           r.rule_type   AS rule_type,
           r.return_expr AS return_expr,
           r.is_optional AS is_optional,
           cf.operator   AS operator
    ORDER BY r.action, r.name
    """
    with kg._driver.session() as session:
        return [dict(record) for record in session.run(cypher, jsonpath=jsonpath)]


# ---------------------------------------------------------------------------
# 2. All leaf rules for a specific action
# ---------------------------------------------------------------------------


def rules_for_action(kg: KnowledgeGraph, action: str) -> list[dict[str, Any]]:
    """Return all Rule nodes belonging to the given action."""
    cypher = """
    MATCH (r:Rule {action: $action})
    RETURN r.name        AS rule_name,
           r.rule_type   AS rule_type,
           r.return_expr AS return_expr,
           r.is_optional AS is_optional,
           r.scope       AS scope,
           r.error_code  AS error_code,
           r.description AS description
    ORDER BY r.name
    """
    with kg._driver.session() as session:
        return [dict(record) for record in session.run(cypher, action=action)]


# ---------------------------------------------------------------------------
# 3. Allowed enum values for a field
# ---------------------------------------------------------------------------


def enum_values_for_field(kg: KnowledgeGraph, jsonpath: str) -> list[dict[str, Any]]:
    """Return all EnumValue nodes validated against the given JSONPath field."""
    cypher = """
    MATCH (r:Rule)-[:CHECKS_FIELD]->(f:Field {jsonpath: $jsonpath})
    MATCH (r)-[ve:VALIDATES_ENUM]->(e:EnumValue)
    RETURN f.jsonpath  AS jsonpath,
           e.value     AS enum_value,
           ve.operator AS operator,
           r.name      AS rule_name,
           r.action    AS action
    ORDER BY e.value
    """
    with kg._driver.session() as session:
        return [dict(record) for record in session.run(cypher, jsonpath=jsonpath)]


# ---------------------------------------------------------------------------
# 4. All JSONPaths validated within an action
# ---------------------------------------------------------------------------


def fields_validated_by_action(kg: KnowledgeGraph, action: str) -> list[dict[str, Any]]:
    """Return all Field nodes (JSONPaths) referenced by rules in the given action."""
    cypher = """
    MATCH (r:Rule {action: $action})-[:CHECKS_FIELD]->(f:Field)
    RETURN DISTINCT f.jsonpath      AS jsonpath,
                    f.field_segment AS field_segment,
                    collect(DISTINCT r.rule_type) AS rule_types
    ORDER BY f.jsonpath
    """
    with kg._driver.session() as session:
        return [dict(record) for record in session.run(cypher, action=action)]


# ---------------------------------------------------------------------------
# 5. Fields whose enum sets differ across actions
# ---------------------------------------------------------------------------


def cross_action_field_conflicts(kg: KnowledgeGraph) -> list[dict[str, Any]]:
    """Find fields with conflicting (different) enum value sets across actions."""
    cypher = """
    MATCH (r:Rule)-[:CHECKS_FIELD]->(f:Field)
    MATCH (r)-[:VALIDATES_ENUM]->(e:EnumValue)
    WITH f.jsonpath AS jsonpath,
         r.action   AS action,
         collect(DISTINCT e.value) AS enum_set
    WITH jsonpath, collect({action: action, enum_set: enum_set}) AS per_action
    WHERE size(per_action) > 1
    RETURN jsonpath,
           per_action,
           size(per_action) AS num_actions
    ORDER BY num_actions DESC, jsonpath
    """
    with kg._driver.session() as session:
        return [dict(record) for record in session.run(cypher)]


# ---------------------------------------------------------------------------
# 6. Session data save/read chain
# ---------------------------------------------------------------------------


def session_chain(kg: KnowledgeGraph) -> list[dict[str, Any]]:
    """Return all SAVES_SESSION and READS_SESSION linkages."""
    cypher = """
    MATCH (saver:Action)-[:SAVES_SESSION]->(sk:SessionKey)
    OPTIONAL MATCH (reader:Rule)-[rs:READS_SESSION]->(sk)
    RETURN sk.key            AS session_key,
           sk.jsonpath       AS saved_jsonpath,
           saver.name        AS saved_by_action,
           collect(DISTINCT reader.name)   AS reading_rules,
           collect(DISTINCT reader.action) AS reading_actions
    ORDER BY sk.key
    """
    with kg._driver.session() as session:
        return [dict(record) for record in session.run(cypher)]


# ---------------------------------------------------------------------------
# 7. All rules of a given type
# ---------------------------------------------------------------------------


def rules_by_type(kg: KnowledgeGraph, rule_type: str) -> list[dict[str, Any]]:
    """Return all rules that include the given rule_type in their rule_type list."""
    cypher = """
    MATCH (r:Rule)
    WHERE $rule_type IN r.rule_type
    RETURN r.name        AS rule_name,
           r.action      AS action,
           r.return_expr AS return_expr,
           r.is_optional AS is_optional,
           r.scope       AS scope
    ORDER BY r.action, r.name
    """
    with kg._driver.session() as session:
        return [dict(record) for record in session.run(cypher, rule_type=rule_type)]


# ---------------------------------------------------------------------------
# 8. Impact analysis — all rules and actions affected by a field change
# ---------------------------------------------------------------------------


def impact_of_field_change(kg: KnowledgeGraph, jsonpath: str) -> list[dict[str, Any]]:
    """Return all rules and their parent actions that check the given JSONPath."""
    cypher = """
    MATCH (r:Rule)-[:CHECKS_FIELD]->(f:Field {jsonpath: $jsonpath})
    OPTIONAL MATCH (g:Group)-[:CONTAINS_RULE]->(r)
    OPTIONAL MATCH (d:Domain)-[:HAS_RULE]->(r)
    OPTIONAL MATCH (d2:Domain)-[:HAS_GROUP]->(:Group)-[:CONTAINS_RULE*]->(r)
    WITH r,
         coalesce(d.name, d2.name)  AS domain,
         g.name                     AS parent_group,
         f.jsonpath                 AS jsonpath
    RETURN DISTINCT
           r.name        AS rule_name,
           r.rule_type   AS rule_type,
           r.return_expr AS return_expr,
           r.action      AS action,
           domain,
           parent_group,
           jsonpath
    ORDER BY r.action, rule_name
    """
    with kg._driver.session() as session:
        return [dict(record) for record in session.run(cypher, jsonpath=jsonpath)]


# ---------------------------------------------------------------------------
# 10. Optional rules for an action
# ---------------------------------------------------------------------------


def optional_rules_for_action(kg: KnowledgeGraph, action: str) -> list[dict[str, Any]]:
    """Return all rules with is_optional=True for the given action."""
    cypher = """
    MATCH (r:Rule {action: $action, is_optional: true})
    RETURN r.name         AS rule_name,
           r.rule_type    AS rule_type,
           r.return_expr  AS return_expr,
           r.continue_expr AS continue_expr,
           r.scope        AS scope
    ORDER BY r.name
    """
    with kg._driver.session() as session:
        return [dict(record) for record in session.run(cypher, action=action)]
