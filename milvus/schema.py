from config import *
from pymilvus import FieldSchema, CollectionSchema, DataType


def _build_schema(domain: str, version: str):
    fields = [
        FieldSchema("id",          DataType.INT64,        is_primary=True, auto_id=True),
        FieldSchema("action",      DataType.VARCHAR,      max_length=MAX_ACTION),
        FieldSchema("source_type", DataType.VARCHAR,      max_length=MAX_SOURCE_TYPE),
        FieldSchema("chunk_type",  DataType.VARCHAR,      max_length=MAX_CHUNK_TYPE),
        FieldSchema("path_prefix", DataType.VARCHAR,      max_length=MAX_PATH_PREFIX),
        FieldSchema("type_name",   DataType.VARCHAR,      max_length=MAX_TYPE_NAME),
        FieldSchema("partition_name", DataType.VARCHAR,   max_length=MAX_PARTITION),
        FieldSchema("content",     DataType.VARCHAR,      max_length=MAX_CONTENT),
        FieldSchema("vector",      DataType.FLOAT_VECTOR, dim=DIMENSION),
    ]
    return CollectionSchema(
        fields,
        description=f"ONDC {domain.upper()} {version} API chunks",
        enable_dynamic_field=False,
    )

