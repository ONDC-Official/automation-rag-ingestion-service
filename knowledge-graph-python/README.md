# ONDC Knowledge Graph

A Neo4j knowledge graph built from ONDC protocol validation documentation. Ingests structured JVAL (JSON Validation Language) rule definitions and models them as a rich, queryable graph — enabling impact analysis, conflict detection, session tracing, and RAG-augmented retrieval.

**Multi-domain capable** — multiple domains (e.g. FIS12, LOG10) and versions can coexist in the same graph without collision. Switching or updating a domain is a single command.

---

## What It Does

The standard approach to RAG over these docs is to chunk the markdown files and embed them. That works for simple lookups but breaks for relational questions like:

- _"What fields must be present in a `confirm` payload?"_
- _"Which rules will break if `$.context.domain` changes?"_
- _"What data saved during `search` is verified in `on_confirm`?"_

This project models the **entire validation corpus as a graph** so those questions become 1–2 hop Cypher traversals rather than fuzzy vector searches.

---

## Graph Schema

### Node Types

| Label        | Identity key(s)                            | Key Properties                                                                                              |
| ------------ | ------------------------------------------ | ----------------------------------------------------------------------------------------------------------- |
| `Domain`     | `name + version`                           | `code_name`                                                                                                 |
| `Action`     | `name + domain + version`                  | `direction` (BAP_TO_BPP / BPP_TO_BAP)                                                                       |
| `Group`      | `name + action + domain + version`         | `depth`, `scope`, `continue_expr`, `source_file`                                                            |
| `Rule`       | `name + action + domain + version`         | `rule_type` _(list)_, `return_expr`, `continue_expr`, `scope`, `error_code` _(default 3000)_, `is_optional` |
| `Field`      | `jsonpath` _(global)_                      | `field_segment`                                                                                             |
| `EnumValue`  | `value` _(global)_                         | `value_lower`                                                                                               |
| `Pattern`    | `pattern` _(global)_                       | —                                                                                                           |
| `Operator`   | `name` _(global)_                          | `operator_type` (UNARY/BINARY), `description`                                                               |
| `SessionKey` | `key + saved_by_action + domain + version` | `jsonpath`                                                                                                  |

Nodes marked **global** are shared across all domains — a JSONPath, enum value, regex pattern, or JVAL operator means the same thing regardless of which domain uses it. All other nodes are domain+version scoped and never collide.

### Relationship Types

| Relationship      | From → To           | Meaning                                                     |
| ----------------- | ------------------- | ----------------------------------------------------------- |
| `HAS_ACTION`      | Domain → Action     | Domain owns this action                                     |
| `HAS_GROUP`       | Domain → Group      | Top-level group belongs to domain                           |
| `CONTAINS_GROUP`  | Group → Group       | Nested group hierarchy                                      |
| `CONTAINS_RULE`   | Group → Rule        | Leaf rule inside a group                                    |
| `HAS_RULE`        | Domain → Rule       | Top-level leaf rule belongs to domain (no parent group)     |
| `CHECKS_FIELD`    | Rule → Field        | Rule validates this JSONPath (`operator`, `optional` props) |
| `VALIDATES_ENUM`  | Rule → EnumValue    | Rule checks value is in this set (`operator` prop)          |
| `VALIDATES_REGEX` | Rule → Pattern      | Rule checks value matches this pattern                      |
| `USES_OPERATOR`   | Rule → Operator     | JVAL operator used in `_RETURN_` expression                 |
| `READS_SESSION`   | Rule → SessionKey   | Rule reads cross-request session data                       |
| `SAVES_SESSION`   | Action → SessionKey | Action saves data for later actions                         |

### Rule Types

Each `Rule` node's `rule_type` is a **list of strings** — a rule may match multiple types simultaneously (e.g. a cross-request comparison yields `["CROSS_REQUEST", "COMPARISON"]`).

| Type            | Detected by                                                    |
| --------------- | -------------------------------------------------------------- |
| `PRESENCE`      | `_RETURN_` contains `are present`                              |
| `ENUM`          | `_RETURN_` contains `all in`, `any in`, or `none in`           |
| `REGEX`         | `_RETURN_` contains `follow regex`                             |
| `UNIQUENESS`    | `_RETURN_` contains `are unique`                               |
| `COMPARISON`    | `_RETURN_` contains `equal to`, `greater than`, or `less than` |
| `CROSS_REQUEST` | Any variable references `$._EXTERNAL.`                         |

All matching types are collected; if none match, `["PRESENCE"]` is used as fallback.

### `error_code` default

If a rule does not specify `_ERROR_CODE_` in the JVAL config, `error_code` defaults to `3000`.

### `is_optional` flag

A `Rule` is marked `is_optional: true` when its `_CONTINUE_` expression follows the skip-if-absent pattern (`!(attr are present)`), meaning the field is optional — the rule only runs if the field is present.

---

## Data Source

All data is extracted from the x-validations markdown files in `../build-output/temp/x-validations/`. Each file (e.g. `search.md`, `on_confirm.md`) contains:

1. **YAML frontmatter** — action name, domain, version, test count
2. **JSON code block** — the full JVAL config with `_TESTS_` and `_SESSION_DATA_`

The `x-validations/` files are the **source of truth**. The `validations/` files are human-readable companions generated from them.

---

## Project Structure

```
knowledge-graph-python/
├── models.py       Dataclasses for all node and edge types
├── parser.py       Reads x-validations .md files → structured dicts
├── extractor.py    Walks the JVAL test tree → ExtractionResult
├── graph.py        Neo4j driver wrapper — MERGE-based writes + Cypher helpers
├── ingester.py     Orchestrates parse → extract → ingest for all action files
├── queries.py      10 Cypher retrieval functions
└── main.py         CLI entry point
```

### How data flows

```
x-validations/*.md
      │
      ▼
  parser.py          parse_xvalidation_file(path)
      │               → { frontmatter, tests, session_data }
      ▼
  extractor.py       extract(action, domain, version, ...)
      │               → ExtractionResult (nodes + edges)
      ▼
  graph.py           kg.ingest_extraction_result(result)
      │               → MERGE into Neo4j
      ▼
  Neo4j graph
      │
      ▼
  queries.py         rules_for_field(kg, jsonpath) etc.
```

---

## Setup

### Prerequisites

- Python 3.11+
- A running Neo4j instance (local or Docker)

### Install

```bash
pip install -r requirements.txt
```

### Configure

```bash
cp .env.example .env
# Edit .env and set your Neo4j password
```

`.env.example`:

```
NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=your_password_here
```

### Run Neo4j with Docker (if needed)

```bash
docker run \
  --name neo4j \
  -p 7474:7474 -p 7687:7687 \
  -e NEO4J_AUTH=neo4j/your_password_here \
  neo4j:5
```

---

## Usage

All commands are run from the `knowledge-graph-python/` directory.

### Ingest everything (first run)

```bash
python3 main.py
```

Indexes are created and all action files are parsed and ingested.

### Clear and re-ingest

```bash
python3 main.py --clear
```

### Query without re-ingesting

```bash
# Cross-request session data linkages
python3 main.py --no-ingest --query session

# All rules that check a specific JSONPath
python3 main.py --no-ingest --query field --field '$.context.domain'
```

---

## Multi-Domain & Version Updates

The graph is designed to hold multiple domains and versions simultaneously without any data collision. `Action`, `Group`, `Rule`, and `SessionKey` nodes are all keyed by `domain + version`, so `REQUIRED_CONTEXT_DOMAIN` in FIS12 and `REQUIRED_CONTEXT_DOMAIN` in LOG10 are **separate nodes**. `Field`, `EnumValue`, `Pattern`, and `Operator` nodes are global and shared across all domains.

### Add a second domain alongside the current one

```bash
# Point at the new domain's build output — FIS12 stays untouched
python3 main.py --data-dir /path/to/LOG10/temp --mode append
```

### Update docs for a domain you already ingested

Use `--mode upsert`. It reads the `domain` and `version` from the frontmatter of the files, drops all existing nodes for that domain+version, then re-ingests fresh. Global nodes (Field, EnumValue, etc.) are never deleted.

```bash
python3 main.py --data-dir ../build-output/temp --mode upsert
```

### Wipe everything and start fresh

```bash
python3 main.py --clear
```

### Ingestion mode summary

| Mode                 | What it does                                                                                  |
| -------------------- | --------------------------------------------------------------------------------------------- |
| `append` _(default)_ | Adds data to the graph. Safe to run multiple times — all writes are `MERGE`.                  |
| `upsert`             | Drops the domain+version found in the docs, then re-ingests. Use when updating existing docs. |
| `--clear` flag       | Deletes the entire graph before ingesting.                                                    |

---

## Queries Reference

All query functions live in `queries.py`. Each takes a `KnowledgeGraph` instance and returns a `list[dict]`.

| Function                                 | What it returns                                           |
| ---------------------------------------- | --------------------------------------------------------- |
| `rules_for_field(kg, jsonpath)`          | All rules that check a given JSONPath, across all actions |
| `rules_for_action(kg, action)`           | All leaf rules for a specific action                      |
| `enum_values_for_field(kg, jsonpath)`    | All allowed enum values for a field                       |
| `fields_validated_by_action(kg, action)` | All JSONPaths validated in an action                      |
| `cross_action_field_conflicts(kg)`       | Fields with different enum sets across actions            |
| `session_chain(kg)`                      | All save/read session data linkages                       |
| `rules_by_type(kg, rule_type)`           | All rules whose `rule_type` list includes the given type  |
| `impact_of_field_change(kg, jsonpath)`   | All rules and actions affected by a field change          |
| `optional_rules_for_action(kg, action)`  | Rules with `is_optional=True` for an action               |

### Example — use queries directly in Python

```python
from graph import KnowledgeGraph
from queries import (
    rules_for_field,
    enum_values_for_field,
    impact_of_field_change,
    session_chain,
    cross_action_field_conflicts,
)

kg = KnowledgeGraph()

# What rules validate $.context.domain?
for row in rules_for_field(kg, "$.context.domain"):
    print(row)

# What enum values are allowed for that field?
for row in enum_values_for_field(kg, "$.context.domain"):
    print(row)

# If $.context.domain changes, what breaks?
for row in impact_of_field_change(kg, "$.context.domain"):
    print(row)

# What cross-request state is tracked across the transaction?
for row in session_chain(kg):
    print(row)

# Are there any fields with conflicting allowed values across actions?
for row in cross_action_field_conflicts(kg):
    print(row)

kg.close()
```

---

## Stats (ONDC FIS12 v2.0.2)

After a full ingest across all 12 actions:

| Metric           | Count  |
| ---------------- | ------ |
| Actions          | 12     |
| Groups           | 113    |
| Rules            | 408    |
| Field references | 409    |
| Total edges      | ~1,700 |

---

## Extending

### Add a new action file

Drop a new `.md` file into `../build-output/temp/x-validations/` following the same format (YAML frontmatter + JSON code block). Re-run `python3 main.py` — ingestion is idempotent.

### Add a new query

Add a function to `queries.py`. Follow the same pattern: accept `kg: KnowledgeGraph`, run a Cypher query via `kg._driver.session()`, return `list[dict]`.

### Change the graph schema

1. Update the relevant `@dataclass` in `models.py`
2. Update the `merge_*` method in `graph.py`
3. Update extraction logic in `extractor.py` if the new property comes from the JVAL config
