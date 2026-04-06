from helpers import _build_chunk_text, _chunk_id, _truncate, _indent
from config import *
import re


def chunk_type_definitions(pre_main_text: str, action: str, source_type: str) -> list[dict]:
    chunks = []
    pattern = re.compile(
        r"^## ([A-Za-z_][A-Za-z_0-9]*)\n(.*?)(?=^## |\Z)",
        re.MULTILINE | re.DOTALL,
    )
    for m in pattern.finditer(pre_main_text):
        type_name   = m.group(1).strip()
        fields_body = m.group(2).strip()
        if not fields_body:
            continue
        path_prefix = f"$ref:{type_name}"
        body        = f"Type Definition: {type_name}\n\n{fields_body}"
        content     = _build_chunk_text(action, source_type, "type_definition",
                                        path_prefix, type_name, body)
        chunks.append(dict(
            chunk_id    = _chunk_id(action, "type_definition", path_prefix, type_name),
            action      = action,
            source_type = source_type,
            chunk_type  = "type_definition",
            path_prefix = _truncate(path_prefix, MAX_PATH_PREFIX),
            type_name   = _truncate(type_name,   MAX_TYPE_NAME),
            content     = _truncate(content,     MAX_CONTENT),
        ))
    return chunks


def chunk_main_schema(main_schema_text: str, action: str, source_type: str) -> list[dict]:
    chunks: list[dict] = []
    lines  = main_schema_text.splitlines()

    current_path  = ""
    current_lines: list[str] = []
    in_message_order = False

    def flush():
        nonlocal current_path, current_lines
        body_text = "\n".join(current_lines).strip()
        if not (current_path and body_text):
            current_path, current_lines = "", []
            return
        body    = f"Schema for path: {current_path}\n\n{body_text}"
        content = _build_chunk_text(action, source_type, "schema_path",
                                    current_path, "", body)
        chunks.append(dict(
            chunk_id    = _chunk_id(action, "schema_path", current_path, ""),
            action      = action,
            source_type = source_type,
            chunk_type  = "schema_path",
            path_prefix = _truncate(current_path, MAX_PATH_PREFIX),
            type_name   = "",
            content     = _truncate(content, MAX_CONTENT),
        ))
        current_path, current_lines = "", []

    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            if current_lines:
                current_lines.append(line)
            continue
        ind       = _indent(line)
        key_match = re.match(r"^([a-zA-Z_][a-zA-Z_0-9\[\*\]]*):(.*)$", stripped)
        if not key_match:
            if current_lines is not None:
                current_lines.append(line)
            continue
        key = key_match.group(1)
        val = key_match.group(2).strip()

        if ind == 0 and key == "context":
            flush(); current_path = "$.context"; current_lines = [line]; in_message_order = False
        elif ind == 0 and key == "message":
            flush(); in_message_order = False
        elif ind == 2 and (key == "order" or key == "intent"):
            flush(); current_path = f"$.message.{key}"; current_lines = [line]; in_message_order = True
        elif in_message_order and ind == 4:
            if not val or val.startswith("$ref:"):
                # Use current_path which is now dynamic ($.message.order or $.message.intent)
                flush(); current_path = f"{current_path}.{key}"; current_lines = [line]
            else:
                current_lines.append(line)
        else:
            current_lines.append(line)

    flush()
    return chunks


def chunk_validation_rules(text: str, action: str, source_type: str) -> list[dict]:
    """
    Detect x_validation blocks (lines starting with 'x-' or 'X-') and
    split them into a separate chunk_type so they land in the x_validations
    partition.  Everything else becomes a validation_rule chunk.
    """
    chunks: list[dict] = []

    # Split on top-level rule headers: lines that begin with a digit or bullet
    rule_blocks = re.split(r"(?m)^(?=\d+\.|[-*]\s)", text.strip())

    for block in rule_blocks:
        block = block.strip()
        if not block:
            continue

        # Classify: does it reference an x- / cross-field rule?
        is_x = bool(re.search(r"\bx[-_]", block, re.IGNORECASE))
        ct   = "x_validation" if is_x else "validation_rule"

        # Extract a short path hint from the first $. reference if available
        path_match  = re.search(r"(\$\.[A-Za-z_.]+)", block)
        path_prefix = path_match.group(1) if path_match else ""

        body    = f"Validation Rule [{action}]:\n\n{block}"
        content = _build_chunk_text(action, source_type, ct, path_prefix, "", body)

        chunks.append(dict(
            chunk_id    = _chunk_id(action, ct, path_prefix, block[:40]),
            action      = action,
            source_type = source_type,
            chunk_type  = ct,
            path_prefix = _truncate(path_prefix, MAX_PATH_PREFIX),
            type_name   = "",
            content     = _truncate(content, MAX_CONTENT),
        ))
    return chunks


def parse_md_file(filepath: str, source_type: str) -> list[dict]:
    action = os.path.splitext(os.path.basename(filepath))[0]
    with open(filepath, "r", encoding="utf-8") as fh:
        raw = fh.read()

    # Extract domain and version from frontmatter
    domain = None
    version = None
    domain_match = re.search(r"^domain:\s*(.+)$", raw, re.MULTILINE)
    if domain_match:
        domain = domain_match.group(1).strip()
    version_match = re.search(r"^version:\s*(.+)$", raw, re.MULTILINE)
    if version_match:
        version = version_match.group(1).strip()

    main_m    = re.search(r"^# ── Main Schema", raw, re.MULTILINE)
    example_m = re.search(r"^# ── Example",     raw, re.MULTILINE)

    if main_m:
        pre_main    = raw[: main_m.start()]
        main_end    = example_m.start() if example_m else len(raw)
        main_schema = raw[main_m.end() : main_end]
    else:
        pre_main    = raw
        main_schema = ""

    chunks: list[dict] = []
    chunks.extend(chunk_type_definitions(pre_main, action, source_type))
    chunks.extend(chunk_main_schema(main_schema, action, source_type))

    # For validation source files, also extract rule-level chunks
    if source_type == "validation":
        # Take the pre_main section minus the type-def blocks as rule text
        rule_text = re.sub(
            r"^## [A-Za-z_][A-Za-z_0-9]*\n.*?(?=^## |\Z)",
            "", pre_main, flags=re.MULTILINE | re.DOTALL
        ).strip()
        if rule_text:
            chunks.extend(chunk_validation_rules(rule_text, action, source_type))

    # Attach detected domain and version
    for c in chunks:
        c["_domain"] = domain
        c["_version"] = version

    return chunks


def collect_all_chunks() -> list[dict]:
    all_chunks: list[dict] = []
    dir_map = {
        VALIDATIONS_DIR: "validation",
        API_SCHEMAS_DIR: "api schema",
    }
    for directory, source_type in dir_map.items():
        if not os.path.isdir(directory):
            print(f"  [WARN] Skipping missing dir: {directory}")
            continue
        md_files = sorted(f for f in os.listdir(directory) if f.endswith(".md"))
        if not md_files:
            print(f"  [WARN] No .md files in: {directory}")
            continue
        print(f"\n  [{source_type}]  {directory}  ({len(md_files)} files)")
        for filename in md_files:
            path = os.path.join(directory, filename)
            try:
                fc = parse_md_file(path, source_type)
                print(f"    {filename:35s} → {len(fc):>4} chunks")
                all_chunks.extend(fc)
            except Exception as exc:
                print(f"    [ERROR] {filename}: {exc}")
    return all_chunks
