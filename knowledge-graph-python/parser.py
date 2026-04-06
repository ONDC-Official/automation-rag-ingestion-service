"""
parser.py — Parse x-validations markdown files into structured dicts.

Each file has the shape:
  ---
  <YAML frontmatter>
  ---

  ```json
  { "_TESTS_": { "<action>": [...] }, "_SESSION_DATA_": { "<action>": {...} } }
  ```
"""

import json
from pathlib import Path
from typing import Any

import yaml


def parse_xvalidation_file(filepath: Path) -> dict[str, Any]:
    """Read a single x-validations markdown file and return its parsed content.

    Returns a dict with keys:
        frontmatter   — dict parsed from YAML block
        tests         — list of top-level test objects for the action
        session_data  — dict of session key → JSONPath for the action
    """
    text = filepath.read_text(encoding="utf-8")

    frontmatter = _extract_frontmatter(text)
    payload = _extract_json_block(text)

    action: str = frontmatter.get("action", "")
    tests: list = payload.get("_TESTS_", {}).get(action, [])
    session_data: dict = payload.get("_SESSION_DATA_", {}).get(action, {})

    return {
        "frontmatter": frontmatter,
        "tests": tests,
        "session_data": session_data,
    }


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------


def _extract_frontmatter(text: str) -> dict[str, Any]:
    """Extract and parse the YAML frontmatter block (between the first pair of ---)."""
    lines = text.splitlines()

    # Find the first '---' delimiter
    start_idx: int | None = None
    for i, line in enumerate(lines):
        if line.strip() == "---":
            start_idx = i
            break

    if start_idx is None:
        return {}

    # Find the closing '---'
    end_idx: int | None = None
    for i in range(start_idx + 1, len(lines)):
        if lines[i].strip() == "---":
            end_idx = i
            break

    if end_idx is None:
        return {}

    yaml_text = "\n".join(lines[start_idx + 1 : end_idx])
    return yaml.safe_load(yaml_text) or {}


def _extract_json_block(text: str) -> dict[str, Any]:
    """Extract and parse the first ```json … ``` fenced code block."""
    fence_open = "```json"
    fence_close = "```"

    start = text.find(fence_open)
    if start == -1:
        return {}

    # Move past the opening fence line
    content_start = text.index("\n", start) + 1
    end = text.find(fence_close, content_start)
    if end == -1:
        return {}

    json_text = text[content_start:end]
    return json.loads(json_text)
