"""
ingester.py — Orchestrates the full parse → extract → ingest pipeline.

Entry point:
    ingest_all(data_dir, kg, mode="append")

Modes:
    append  — Add new domain alongside existing ones (default).
    upsert  — Drop the domain+version found in the docs first, then re-ingest.
              Use this when you update docs for a domain you already ingested.
"""

import logging
from pathlib import Path

from extractor import extract
from graph import KnowledgeGraph
from parser import parse_xvalidation_file

log = logging.getLogger("ingester")


def ingest_all(data_dir: Path, kg: KnowledgeGraph, mode: str = "append") -> None:
    """Parse all x-validation markdown files and ingest them into the knowledge graph.

    Args:
        data_dir: Path to the directory containing the ``x-validations/`` sub-folder.
        kg:       An initialised KnowledgeGraph instance.
        mode:     ``"append"`` adds data without removing anything.
                  ``"upsert"`` drops the domain+version found in the files before
                  re-ingesting, so the graph always reflects the current docs.
    """
    validation_dir = data_dir / "x-validations"
    md_files = sorted(validation_dir.glob("*.md"))

    if not md_files:
        log.warning("No markdown files found under %s", validation_dir)
        return

    log.info("Found %d markdown files in %s (mode=%s)", len(md_files), validation_dir, mode)

    # In upsert mode, detect the domain+version from the first file and drop it first
    if mode == "upsert":
        first_parsed = parse_xvalidation_file(md_files[0])
        fm = first_parsed["frontmatter"]
        domain = fm.get("domain", "ONDC:FIS12")
        version = str(fm.get("version", ""))
        log.info("Upsert mode — dropping existing nodes for %s v%s", domain, version)
        kg.drop_domain(domain, version)
        log.info("Dropped existing domain. Re-ingesting …")

    total_rules = total_groups = total_fields = total_edges = 0

    for filepath in md_files:
        log.info("Processing %s …", filepath.name)

        parsed = parse_xvalidation_file(filepath)
        fm = parsed["frontmatter"]

        action: str = fm.get("action", filepath.stem)
        domain: str = fm.get("domain", "ONDC:FIS12")
        version: str = str(fm.get("version", ""))
        log.debug("  frontmatter: action=%s domain=%s version=%s", action, domain, version)

        result = extract(
            action=action,
            domain=domain,
            version=version,
            source_file=filepath.name,
            tests=parsed["tests"],
            session_data=parsed["session_data"],
        )

        kg.ingest_extraction_result(result)

        n_rules  = len(result.rules)
        n_groups = len(result.groups)
        n_fields = len(result.fields)
        n_edges  = len(result.edges)
        total_rules  += n_rules
        total_groups += n_groups
        total_fields += n_fields
        total_edges  += n_edges

        log.info("  → %d rules, %d groups, %d field refs, %d edges",
                 n_rules, n_groups, n_fields, n_edges)

    log.info(
        "Done. Totals: %d rules, %d groups, %d field refs, %d edges across %d file(s)",
        total_rules, total_groups, total_fields, total_edges, len(md_files),
    )
