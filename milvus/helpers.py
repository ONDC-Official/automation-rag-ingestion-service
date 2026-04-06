import hashlib
import re


def _indent(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


def _chunk_id(action: str, chunk_type: str, path_prefix: str, type_name: str) -> str:
    raw = f"{action}|{chunk_type}|{path_prefix}|{type_name}"
    return hashlib.md5(raw.encode()).hexdigest()


def _build_chunk_text(action, source_type, chunk_type, path_prefix, type_name, body):
    return (
        f"[METADATA]\n"
        f"Action       : {action}\n"
        f"Source Type  : {source_type}\n"
        f"Chunk Type   : {chunk_type}\n"
        f"Path Prefix  : {path_prefix}\n"
        f"Type Name    : {type_name}\n"
        f"\n[CONTENT]\n"
        + body
    )


def _truncate(text: str, max_len: int) -> str:
    enc = text.encode("utf-8")
    if len(enc) <= max_len:
        return text
    return enc[: max_len - 3].decode("utf-8", errors="ignore") + "..."


def _extract_ref_types(content: str) -> list[str]:
    return re.findall(r"\$ref:([A-Za-z_][A-Za-z_0-9]*)", content)


def _resolve_partition(chunk: dict) -> str:
    """
    Decide which Milvus partition a chunk belongs to:

      source_type=api_schema  + chunk_type=schema_path  → api_schema_paths
      source_type=validation  + chunk_type=schema_path  → valid_paths
      chunk_type=type_definition                         → type_definitions
      chunk_type=validation_rule                         → validations
      chunk_type=x_validation                            → x_validations
    """
    ct = chunk.get("chunk_type", "")
    st = chunk.get("source_type", "")

    if ct == "type_definition":
        return "type_definitions"
    if ct == "schema_path":
        return "api_schema_paths" if st == "api_schema" else "valid_paths"
    if ct == "x_validation":
        return "x_validations"
    # Default validation text → validations
    return "validations"
