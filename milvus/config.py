
import os
from dotenv import load_dotenv

load_dotenv()

# ── Config ────────────────────────────────────────────────────────────────────

# OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL")
EMBED_MODEL     = "nomic-embed-text-v2-moe"
DIMENSION       = 768

# MILVUS_HOST = os.getenv("MILVUS_HOST", "localhost")
MILVUS_HOST = os.getenv("MILVUS_HOST")
MILVUS_PORT = os.getenv("MILVUS_PORT", "19530")

DEFAULT_DOMAIN      = os.getenv("DEFAULT_DOMAIN",      "ONDC:FIS12")
DEFAULT_API_VERSION = os.getenv("DEFAULT_API_VERSION", "2.0.2")

COLLECTION_NAME = f"ondc_{DEFAULT_DOMAIN}_{DEFAULT_API_VERSION}"

# Partition names — map chunk_type → partition
PARTITION_MAP = {
    "type_definition":    "type_definitions",
    # schema_path is split by source_type:
    "schema_path:api_schema":   "api_schema_paths",
    "schema_path:validation":   "valid_paths",
    # plain validation rule text blocks
    "validation_rule":    "validations",
    # cross-field / x- rules
    "x_validation":       "x_validations",
}

ALL_PARTITIONS = [
    "valid_paths",
    "validations",
    "x_validations",
    "type_definitions",
    "api_schema_paths",
]

BASE_DIR = os.path.join(os.path.dirname(__file__), "build-output", "temp")

VALIDATIONS_DIR = os.getenv("VALIDATIONS_DIR", os.path.join(BASE_DIR, "validations"))
API_SCHEMAS_DIR = os.getenv("API_SCHEMAS_DIR", os.path.join(BASE_DIR, "api schemas"))

MAX_ACTION      = 100
MAX_SOURCE_TYPE = 50
MAX_CHUNK_TYPE  = 50
MAX_PATH_PREFIX = 500
MAX_TYPE_NAME   = 200
MAX_PARTITION   = 50
MAX_CONTENT     = 32_000