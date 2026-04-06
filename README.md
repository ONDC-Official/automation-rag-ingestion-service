# ONDC RAG Ingestion Service

A specialized ingestion pipeline designed to process ONDC (Open Network for Digital Commerce) API specifications and validation rules into a hybrid RAG (Retrieval-Augmented Generation) architecture. This system populates both a **Vector Database (Milvus)** for semantic search and a **Graph Database (Neo4j)** for structured relationship mapping.

---

## 🏗️ Architecture Overview

The system processes Markdown-based documentation and validation configs from the ONDC FIS12 (Financial Services) domain into two distinct representations:

1.  **Vector Store (Milvus)**: Chunks API schemas, type definitions, and validation rules for high-performance semantic retrieval using embeddings.
2.  **Knowledge Graph (Neo4j)**: Maps the complex relationships between API actions, field paths, and cross-field (x-validation) rules.
3.  **Local LLM (Ollama)**: Powers the embedding generation locally using models like `nomic-embed-text-v2-moe`.

---

## 📁 Project Structure

```text
.
├── milvus/                 # Vector ingestion logic (Python)
│   ├── chunking_strategy.py # ONDC-aware splitting logic
│   ├── ingestion.py        # Milvus collection/partition management
│   └── config.py           # Milvus & Embedding configurations
├── knowledge-graph-python/ # Graph ingestion logic (Python)
│   ├── graph.py            # Neo4j driver and Cypher queries
│   ├── extractor.py        # Relationship extraction logic
│   └── parser.py           # X-Validation JSON/MD parser
├── build-output/           # Input Data (Markdown & JSON)
│   └── temp/
│       ├── api schemas/    # API field specifications
│       ├── validations/    # Human-readable validation rules
│       ├── x-validations/  # Machine-readable cross-field rules
│       └── dsl/            # JVAL Expression documentation
├── docker-compose.yml      # Orchestrates Milvus, Neo4j, Ollama, Attu
└── entrypoint.sh           # Container lifecycle and wait-for-service script
```

---

## ⚙️ Configuration (.env)

| Variable          | Description                                   | Default                   |
| :---------------- | :-------------------------------------------- | :------------------------ |
| `INGEST_MODE`     | Ingestion target: `milvus`, `neo4j`, or `all` | `all`                     |
| `MILVUS_HOST`     | Hostname for Milvus standalone                | `milvus`                  |
| `NEO4J_URI`       | Bolt URI for Neo4j                            | `bolt://neo4j:7687`       |
| `OLLAMA_BASE_URL` | API endpoint for Ollama                       | `http://ollama:11434`     |
| `EMBEDDING_MODEL` | Model used for vector embeddings              | `nomic-embed-text-v2-moe` |
| `DATA_DIR`        | Mounted data directory inside container       | `/app/data`               |

---

## 🚀 Getting Started

### 1. Prerequisites

- Docker & Docker Compose
- 16GB+ RAM (Recommended for running Milvus + Neo4j + LLM)

### 2. Deployment

```bash
# Clone the repository
git clone <repo-url>
cd ondc-rag-ingestion

# Start all services (Databases + Ingestion)
docker-compose up --build
```

### 3. Monitoring

- **Milvus UI (Attu)**: Visit `http://localhost:8001` to view collections and partitions.
- **Neo4j Browser**: Visit `http://localhost:7474` (User: `neo4j`, Pass: `password`) to explore the knowledge graph.
- **Ollama Status**: Visit `http://localhost:11434` to verify the LLM server.

---

## 🧠 Ingestion & Chunking Logic

### Vector Strategy (Milvus)

The system uses a specialized ONDC-aware chunking strategy:

- **Type Definitions**: Extracted from `##` headers and stored in the `type_definitions` partition.
- **Schema Paths**: Maps JSONPaths (e.g., `$.message.intent`) to specific metadata for filtered retrieval.
- **Validation Rules**: Distinguishes between standard field rules and complex cross-field (x-) logic.

### Graph Strategy (Neo4j)

- **Nodes**: `Action`, `Field`, `ValidationRule`, `Domain`.
- **Edges**: `VALIDATES_FIELD`, `PART_OF_ACTION`, `DEPENDS_ON`.
- It specifically parses the machine-readable `x-validations` to build a dependency map of the FIS12 protocol.

---

## 🛠️ Development & Debugging

### Running Ingestion Locally (without Docker)

1. Install requirements:
   ```bash
   pip install -r milvus/requirements.txt
   pip install -r knowledge-graph-python/requirements.txt
   ```
2. Run Milvus ingestion:
   ```bash
   python3 milvus/main.py
   ```
3. Run Neo4j ingestion:
   ```bash
   cd knowledge-graph-python && python3 main.py
   ```

### Common Commands

- **Clear Graph**: `python3 main.py --clear`
- **Upsert Mode**: `python3 main.py --mode upsert` (Replaces data for the specific domain/version)
- **Check Connections**: `nc -zv localhost 19530` (Milvus) or `nc -zv localhost 7687` (Neo4j)
