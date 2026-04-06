"""
main.py — CLI entry point for the ONDC Knowledge Graph project.

Usage examples:
    python3 main.py                                         # ingest FIS12 docs (append mode)
    python3 main.py --clear                                 # wipe graph, then ingest
    python3 main.py --mode upsert                           # drop+replace current domain, re-ingest
    python3 main.py --data-dir /path/to/LOG10/temp          # ingest a different domain
    python3 main.py --no-ingest --query flow                # query without re-ingesting
    python3 main.py --no-ingest --query session
    python3 main.py --no-ingest --query field --field '$.context.domain'
"""

import logging
import sys
import argparse
from pathlib import Path

from graph import KnowledgeGraph
from ingester import ingest_all
from queries import rules_for_field, session_chain

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)-8s] %(name)-20s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    stream=sys.stdout,
    force=True,
)
log = logging.getLogger("main")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="ONDC FIS12 Knowledge Graph — ingest and query tool"
    )
    parser.add_argument(
        "--data-dir",
        default="../build-output/temp",
        help="Path to the temp docs directory that contains the x-validations/ sub-folder",
    )
    parser.add_argument(
        "--clear",
        action="store_true",
        help="Clear the graph before ingesting",
    )
    parser.add_argument(
        "--no-ingest",
        action="store_true",
        help="Skip ingestion and go straight to querying",
    )
    parser.add_argument(
        "--mode",
        choices=["append", "upsert"],
        default="append",
        help=(
            "append: add docs alongside existing domains (default). "
            "upsert: drop the domain+version in the docs first, then re-ingest."
        ),
    )
    parser.add_argument(
        "--query",
        choices=["session", "field"],
        help="Run a demo query after ingestion",
    )
    parser.add_argument(
        "--field",
        help="JSONPath for the 'field' query (e.g. '$.context.domain')",
    )
    args = parser.parse_args()

    log.info("Starting knowledge graph pipeline | data_dir=%s mode=%s clear=%s no_ingest=%s",
             args.data_dir, args.mode, args.clear, args.no_ingest)

    kg = KnowledgeGraph()

    try:
        if args.clear:
            log.info("Clearing graph …")
            kg.clear()
            log.info("Graph cleared.")

        if not args.no_ingest:
            from parser import parse_xvalidation_file

            validation_dir = Path(args.data_dir) / "x-validations"
            md_files = sorted(validation_dir.glob("*.md"))

            should_skip = False
            if md_files:
                first_parsed = parse_xvalidation_file(md_files[0])
                fm = first_parsed["frontmatter"]
                domain = fm.get("domain", "ONDC:FIS12")
                version = str(fm.get("version", ""))
                log.info("Detected domain=%s version=%s from first file", domain, version)
                if kg.has_data(domain, version):
                    log.info("[SKIP] Neo4j data for %s v%s already exists. "
                             "Use --clear or --mode upsert to re-ingest.", domain, version)
                    should_skip = True

            if not should_skip:
                log.info("Setting up Neo4j indexes …")
                kg.setup_indexes()
                log.info("Ingesting from %s …", args.data_dir)
                ingest_all(Path(args.data_dir), kg, mode=args.mode)
                log.info("Ingestion complete.")

        if args.query == "session":
            log.info("Running session chain query …")
            for row in session_chain(kg):
                log.info("  %s", row)

        elif args.query == "field":
            if not args.field:
                log.error("--field is required when using --query field")
            else:
                log.info("Running rules-for-field query: %s", args.field)
                for row in rules_for_field(kg, args.field):
                    log.info("  %s", row)

    finally:
        kg.close()
        log.info("Neo4j driver closed.")


if __name__ == "__main__":
    main()
