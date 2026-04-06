#!/bin/bash
set -e

echo "🔧 Starting ONDC RAG Ingestion Container..."

# 1. Validate environment variables
required_vars=(MILVUS_HOST MILVUS_PORT NEO4J_URI OLLAMA_BASE_URL)
for var in "${required_vars[@]}"; do
  if [ -z "${!var}" ]; then
    echo "❌ Missing required env: $var"
    exit 1
  fi
done

# 2. Setup Dynamic Data Path
# This is the directory INSIDE the container where your build-output is mounted
export DATA_DIR=${DATA_DIR:-"/app/data"}
export VALIDATIONS_DIR="$DATA_DIR/validations"
export API_SCHEMAS_DIR="$DATA_DIR/api schemas"
export INGEST_MODE=${INGEST_MODE:-all}

echo "📂 Using Data Directory: $DATA_DIR"

# 3. Wait for Services Function
wait_for_service () {
  local host=$1
  local port=$2
  local name=$3
  echo "⏳ Waiting for $name at $host:$port..."
  while ! nc -z "$host" "$port"; do
    sleep 2
  done
  echo "✅ $name is ready"
}

# 4. Check Connections
if [[ "$INGEST_MODE" == "milvus" || "$INGEST_MODE" == "all" ]]; then
  wait_for_service "$MILVUS_HOST" "$MILVUS_PORT" "Milvus"
fi

if [[ "$INGEST_MODE" == "neo4j" || "$INGEST_MODE" == "all" ]]; then
  NEO4J_HOST=$(echo "$NEO4J_URI" | sed -E 's|.*://([^:]+):.*|\1|')
  wait_for_service "$NEO4J_HOST" 7687 "Neo4j"
fi

# 5. Run Milvus Ingestion
if [[ "$INGEST_MODE" == "milvus" || "$INGEST_MODE" == "all" ]]; then
  echo "📦 Running Milvus ingestion..."
  # We run it from /app so it finds the 'milvus' module
  python3 milvus/main.py
fi

# 6. Run Neo4j Ingestion
if [[ "$INGEST_MODE" == "neo4j" || "$INGEST_MODE" == "all" ]]; then
  echo "🚀 Running knowledge graph ingestion..."
  
  # Go into the subfolder so local imports work
  cd /app/knowledge-graph-python

  # We pass $DATA_DIR dynamically to the python script via flag
  python3 main.py --data-dir "$DATA_DIR" --mode append
fi

echo "✅ All ingestion tasks complete!"