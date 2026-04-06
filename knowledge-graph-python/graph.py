"""
graph.py — Neo4j driver wrapper.

All write operations use MERGE so re-runs are idempotent.
"""

import logging
import os
from typing import Any

from dotenv import load_dotenv
from neo4j import GraphDatabase, Driver

log = logging.getLogger("graph")

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

load_dotenv()

class KnowledgeGraph:
    """Thin wrapper around the Neo4j driver that exposes MERGE-based write operations."""

    def __init__(self) -> None:
        uri = os.getenv("NEO4J_URI", "bolt://localhost:7687")
        user = os.getenv("NEO4J_USER", "neo4j")
        password = os.getenv("NEO4J_PASSWORD", "")
        log.info("Connecting to Neo4j at %s (user=%s)", uri, user)
        self._driver: Driver = GraphDatabase.driver(uri, auth=(user, password))
        log.info("Neo4j driver created successfully")

    def close(self) -> None:
        self._driver.close()

    # ------------------------------------------------------------------
    # Index + operator seed setup
    # ------------------------------------------------------------------

    def setup_indexes(self) -> None:
        """Create indexes on key properties for all node labels, then seed operators."""
        log.info("Creating Neo4j indexes and fulltext index …")
        index_statements = [
            "CREATE INDEX domain_comp   IF NOT EXISTS FOR (n:Domain)     ON (n.name, n.version)",
            "CREATE INDEX action_comp   IF NOT EXISTS FOR (n:Action)     ON (n.name, n.domain, n.version)",
            "CREATE INDEX group_comp    IF NOT EXISTS FOR (n:Group)      ON (n.name, n.action, n.domain, n.version)",
            "CREATE INDEX rule_comp     IF NOT EXISTS FOR (n:Rule)       ON (n.name, n.action, n.domain, n.version)",
            "CREATE INDEX field_path    IF NOT EXISTS FOR (n:Field)      ON (n.jsonpath)",
            "CREATE INDEX enum_value    IF NOT EXISTS FOR (n:EnumValue)  ON (n.value)",
            "CREATE INDEX pattern_str   IF NOT EXISTS FOR (n:Pattern)    ON (n.pattern)",
            "CREATE INDEX operator_name IF NOT EXISTS FOR (n:Operator)   ON (n.name)",
            "CREATE INDEX session_key   IF NOT EXISTS FOR (n:SessionKey) ON (n.key, n.saved_by_action, n.domain, n.version)",
        ]
        with self._driver.session() as session:
            for stmt in index_statements:
                session.run(stmt)
            # Drop and recreate fulltext index to ensure it's working
            try:
                session.run("DROP INDEX ondc_chunk_content IF EXISTS")
            except:
                pass
            session.run(
                "CREATE FULLTEXT INDEX ondc_chunk_content IF NOT EXISTS "
                "FOR (n:Rule|Group) ON EACH [n.name, n.description, n.action]"
            )

        log.info("Indexes created. Seeding operator nodes …")
        self._seed_operators()
        log.info("Operator seed complete.")

    def _seed_operators(self) -> None:
        """Ensure all static Operator nodes exist in the graph."""
        from extractor import OPERATOR_DEFINITIONS
        with self._driver.session() as session:
            for op_name, op_type, op_desc in OPERATOR_DEFINITIONS:
                session.run(
                    """
                    MERGE (o:Operator {name: $name})
                    SET o.operator_type = $operator_type,
                        o.description   = $description
                    """,
                    name=op_name,
                    operator_type=op_type,
                    description=op_desc,
                )

    # ------------------------------------------------------------------
    # Node MERGE methods
    # ------------------------------------------------------------------

    def merge_domain(self, node: DomainNode) -> None:
        with self._driver.session() as session:
            session.run(
                """
                MERGE (n:Domain {name: $name, version: $version})
                SET n.code_name = $code_name
                """,
                name=node.name,
                version=node.version,
                code_name=node.code_name,
            )

    def merge_action(self, node: ActionNode) -> None:
        with self._driver.session() as session:
            session.run(
                """
                MERGE (n:Action {name: $name, domain: $domain, version: $version})
                SET n.direction = $direction
                """,
                name=node.name,
                direction=node.direction,
                domain=node.domain,
                version=node.version,
            )

    def merge_group(self, node: GroupNode) -> None:
        with self._driver.session() as session:
            session.run(
                """
                MERGE (n:Group {name: $name, action: $action, domain: $domain, version: $version})
                SET n.depth         = $depth,
                    n.scope         = $scope,
                    n.continue_expr = $continue_expr,
                    n.source_file   = $source_file
                """,
                name=node.name,
                action=node.action,
                domain=node.domain,
                version=node.version,
                depth=node.depth,
                scope=node.scope,
                continue_expr=node.continue_expr,
                source_file=node.source_file,
            )

    def merge_rule(self, node: RuleNode) -> None:
        with self._driver.session() as session:
            session.run(
                """
                MERGE (n:Rule {name: $name, action: $action, domain: $domain, version: $version})
                SET n.rule_type     = $rule_type,
                    n.return_expr   = $return_expr,
                    n.continue_expr = $continue_expr,
                    n.scope         = $scope,
                    n.error_code    = $error_code,
                    n.description   = $description,
                    n.source_file   = $source_file,
                    n.is_optional   = $is_optional
                """,
                name=node.name,
                action=node.action,
                domain=node.domain,
                version=node.version,
                rule_type=node.rule_type,
                return_expr=node.return_expr,
                continue_expr=node.continue_expr,
                scope=node.scope,
                error_code=node.error_code,
                description=node.description,
                source_file=node.source_file,
                is_optional=node.is_optional,
            )

    def merge_field(self, node: FieldNode) -> None:
        with self._driver.session() as session:
            session.run(
                """
                MERGE (n:Field {jsonpath: $jsonpath})
                SET n.field_segment = $field_segment
                """,
                jsonpath=node.jsonpath,
                field_segment=node.field_segment,
            )

    def merge_enum_value(self, node: EnumValueNode) -> None:
        with self._driver.session() as session:
            session.run(
                """
                MERGE (n:EnumValue {value: $value})
                SET n.value_lower = $value_lower
                """,
                value=node.value,
                value_lower=node.value_lower,
            )

    def merge_pattern(self, node: PatternNode) -> None:
        with self._driver.session() as session:
            session.run(
                "MERGE (n:Pattern {pattern: $pattern})",
                pattern=node.pattern,
            )

    def merge_operator(self, node: OperatorNode) -> None:
        with self._driver.session() as session:
            session.run(
                """
                MERGE (n:Operator {name: $name})
                SET n.operator_type = $operator_type,
                    n.description   = $description
                """,
                name=node.name,
                operator_type=node.operator_type,
                description=node.description,
            )

    def merge_session_key(self, node: SessionKeyNode) -> None:
        with self._driver.session() as session:
            session.run(
                """
                MERGE (n:SessionKey {key: $key, saved_by_action: $saved_by_action,
                                     domain: $domain, version: $version})
                SET n.jsonpath = $jsonpath
                """,
                key=node.key,
                saved_by_action=node.saved_by_action,
                domain=node.domain,
                version=node.version,
                jsonpath=node.jsonpath,
            )

    # ------------------------------------------------------------------
    # Edge MERGE
    # ------------------------------------------------------------------

    def merge_edge(self, edge: Edge) -> None:
        """Resolve nodes by their canonical ID and MERGE the relationship."""
        from_label = _id_to_label(edge.from_id)
        to_label = _id_to_label(edge.to_id)
        from_match = _build_match_clause(edge.from_id, "from_")
        to_match = _build_match_clause(edge.to_id, "to_")

        props_set = ""
        if edge.properties:
            prop_parts = ", ".join(f"r.{k} = ${k}" for k in edge.properties)
            props_set = f" SET {prop_parts}"

        cypher = (
            f"MATCH (a:{from_label} {{{from_match}}}), "
            f"(b:{to_label} {{{to_match}}}) "
            f"MERGE (a)-[r:{edge.rel_type}]->(b)"
            f"{props_set}"
        )

        params: dict[str, Any] = {}
        params.update(_id_to_params(edge.from_id, "from_"))
        params.update(_id_to_params(edge.to_id, "to_"))
        if edge.properties:
            params.update(edge.properties)

        with self._driver.session() as session:
            session.run(cypher, **params)

    # ------------------------------------------------------------------
    # Batch ingest
    # ------------------------------------------------------------------

    def ingest_extraction_result(self, result: ExtractionResult) -> None:
        """Write all nodes first, then all edges (nodes must exist before edges)."""
        log.debug(
            "ingest_extraction_result | domains=%d actions=%d groups=%d rules=%d "
            "fields=%d enums=%d patterns=%d operators=%d session_keys=%d edges=%d",
            len(result.domains), len(result.actions), len(result.groups),
            len(result.rules), len(result.fields), len(result.enum_values),
            len(result.patterns), len(result.operators), len(result.session_keys),
            len(result.edges),
        )
        for node in result.domains:
            self.merge_domain(node)
        for node in result.actions:
            self.merge_action(node)
        for node in result.groups:
            self.merge_group(node)
        for node in result.rules:
            self.merge_rule(node)
        for node in result.fields:
            self.merge_field(node)
        for node in result.enum_values:
            self.merge_enum_value(node)
        for node in result.patterns:
            self.merge_pattern(node)
        for node in result.operators:
            self.merge_operator(node)
        for node in result.session_keys:
            self.merge_session_key(node)
        for edge in result.edges:
            self.merge_edge(edge)

    # ------------------------------------------------------------------
    # Utility
    # ------------------------------------------------------------------

    def drop_domain(self, domain: str, version: str) -> None:
        """Remove all nodes (and their relationships) belonging to a specific domain+version.

        Field, EnumValue, Pattern, and Operator nodes are global and are NOT removed —
        they may be shared with other domains.
        """
        with self._driver.session() as session:
            # Delete domain-scoped nodes; relationships are removed automatically via DETACH
            for label in ("Rule", "Group", "Action", "SessionKey"):
                session.run(
                    f"MATCH (n:{label} {{domain: $domain, version: $version}}) DETACH DELETE n",
                    domain=domain,
                    version=version,
                )
            session.run(
                "MATCH (n:Domain {name: $domain, version: $version}) DETACH DELETE n",
                domain=domain,
                version=version,
            )

    def has_data(self, domain: str, version: str) -> bool:
        """Return True if any domain-scoped nodes exist for this domain+version."""
        with self._driver.session() as session:
            result = session.run(
                "MATCH (n) WHERE n.domain = $domain AND n.version = $version RETURN count(n) AS c",
                domain=domain, version=version
            )
            return result.single()["c"] > 0

    def clear(self) -> None:
        """Remove all nodes and relationships from the graph."""
        log.warning("Clearing ALL nodes and relationships from the graph!")
        with self._driver.session() as session:
            session.run("MATCH (n) DETACH DELETE n")
        log.info("Graph cleared.")


# ---------------------------------------------------------------------------
# Internal helpers for canonical node ID resolution
# ---------------------------------------------------------------------------

_LABEL_MAP: dict[str, str] = {
    "domain":   "Domain",
    "action":   "Action",
    "group":    "Group",
    "rule":     "Rule",
    "field":    "Field",
    "enum":     "EnumValue",
    "pattern":  "Pattern",
    "operator": "Operator",
    "session":  "SessionKey",
}


def _id_to_label(node_id: str) -> str:
    kind = node_id.split("|", maxsplit=1)[0]
    if kind not in _LABEL_MAP:
        raise ValueError(f"Unknown node ID prefix '{kind}' in: {node_id}")
    return _LABEL_MAP[kind]


def _build_match_clause(node_id: str, prefix: str) -> str:
    """Return the Cypher property-match string for a node ID."""
    kind = node_id.split("|", maxsplit=1)[0]

    if kind == "domain":
        return f"name: ${prefix}name, version: ${prefix}version"
    elif kind == "action":
        return f"name: ${prefix}name, domain: ${prefix}domain, version: ${prefix}version"
    elif kind in ("group", "rule"):
        return f"name: ${prefix}name, action: ${prefix}action, domain: ${prefix}domain, version: ${prefix}version"
    elif kind == "operator":
        return f"name: ${prefix}name"
    elif kind == "field":
        return f"jsonpath: ${prefix}jsonpath"
    elif kind == "enum":
        return f"value: ${prefix}value"
    elif kind == "pattern":
        return f"pattern: ${prefix}pattern"
    elif kind == "session":
        return f"key: ${prefix}key, saved_by_action: ${prefix}saved_by_action, domain: ${prefix}domain, version: ${prefix}version"
    else:
        raise ValueError(f"Unknown node ID kind '{kind}'")


def _id_to_params(node_id: str, prefix: str) -> dict[str, Any]:
    """Extract Cypher parameter values from a canonical node ID."""
    kind, *rest = node_id.split("|", maxsplit=1)
    p = rest[0] if rest else ""

    if kind == "domain":
        # format: "domain|<name>|<version>"
        parts = p.split("|", maxsplit=1)
        return {f"{prefix}name": parts[0], f"{prefix}version": parts[1]}
    elif kind == "action":
        # format: "action|<domain>|<version>|<name>"
        parts = p.split("|", maxsplit=2)
        return {f"{prefix}domain": parts[0], f"{prefix}version": parts[1], f"{prefix}name": parts[2]}
    elif kind in ("group", "rule"):
        # format: "<kind>|<domain>|<version>|<action>|<name>"
        parts = p.split("|", maxsplit=3)
        return {
            f"{prefix}domain":  parts[0],
            f"{prefix}version": parts[1],
            f"{prefix}action":  parts[2],
            f"{prefix}name":    parts[3],
        }
    elif kind == "operator":
        return {f"{prefix}name": p}
    elif kind == "field":
        return {f"{prefix}jsonpath": p}
    elif kind == "enum":
        return {f"{prefix}value": p}
    elif kind == "pattern":
        return {f"{prefix}pattern": p}
    elif kind == "session":
        # format: "session|<domain>|<version>|<action>|<key>"
        parts = p.split("|", maxsplit=3)
        return {
            f"{prefix}domain":         parts[0],
            f"{prefix}version":        parts[1],
            f"{prefix}saved_by_action": parts[2],
            f"{prefix}key":            parts[3],
        }
    else:
        raise ValueError(f"Unknown node ID kind '{kind}'")
