from config import *
from pymilvus import FieldSchema, CollectionSchema, DataType,connections, Collection, utility, Partition
from langchain_ollama import OllamaEmbeddings
from collections import defaultdict
import re
from load_ollama import ensure_ollama_model
from chunking_strategy import collect_all_chunks
from helpers import _resolve_partition
from collections import Counter
from schema import _build_schema


def ingest_milvus(all_chunks: list[dict], domain: str, version: str) -> None:
    

    raw_col_name = f"{domain}_{version}"
    safe_col_name = re.sub(r'[^a-zA-Z0-9_]', '_', raw_col_name)
    if not re.match(r'^[a-zA-Z_]', safe_col_name):
        safe_col_name = "col_" + safe_col_name

    print(f"\n{'═'*60}")
    print(f"MILVUS INGESTION  →  collection: {safe_col_name} (from {domain}:{version})")
    print(f"{'═'*60}")
    print(f"Connecting to Milvus at {MILVUS_HOST}:{MILVUS_PORT} ...")

    try:
        connections.connect("default", host=MILVUS_HOST, port=MILVUS_PORT)
    except Exception as exc:
        print(f"[FATAL] Cannot connect to Milvus: {exc}")
        return

    # Skip if collection already exists
    if utility.has_collection(safe_col_name):
        print(f"\n[SKIP] Milvus collection '{safe_col_name}' already exists. Delete it manually to re-ingest.")
        return

    col = Collection(safe_col_name, schema=_build_schema(domain, version))
    print(f"Collection '{safe_col_name}' created.")

    # Create partitions
    for pname in ALL_PARTITIONS:
        col.create_partition(pname)
    print(f"Partitions created: {ALL_PARTITIONS}")

    # Resolve partition per chunk
    for c in all_chunks:
        c["_partition"] = _resolve_partition(c)

    # Pull model
    print(f"\nChecking Ollama model '{EMBED_MODEL}' ...")
    ensure_ollama_model(EMBED_MODEL, OLLAMA_BASE_URL)

    
    embeddings = OllamaEmbeddings(model=EMBED_MODEL, base_url=OLLAMA_BASE_URL)

    # Group by partition and insert
    by_partition: dict[str, list[dict]] = defaultdict(list)
    for c in all_chunks:
        by_partition[c["_partition"]].append(c)

    BATCH_SIZE     = 50
    inserted_total = 0
    grand_total    = len(all_chunks)

    for pname in ALL_PARTITIONS:
        batch_list = by_partition.get(pname, [])
        if not batch_list:
            print(f"  Partition '{pname}': 0 chunks (skipped)")
            continue

        print(f"\n  Partition '{pname}': {len(batch_list)} chunks")
        partition = Partition(col, pname)

        for start in range(0, len(batch_list), BATCH_SIZE):
            batch = batch_list[start : start + BATCH_SIZE]
            texts = [f"search_document: {c['content']}" for c in batch]

            try:
                vectors = embeddings.embed_documents(texts)
            except Exception as exc:
                print(f"\n[FATAL] Embedding failed at partition={pname} offset={start}: {exc}")
                return

            partition.insert([
                [c["action"]       for c in batch],
                [c["source_type"]  for c in batch],
                [c["chunk_type"]   for c in batch],
                [c["path_prefix"]  for c in batch],
                [c["type_name"]    for c in batch],
                [c["_partition"]   for c in batch],   # stored for easy filtering
                [c["content"]      for c in batch],
                vectors,
            ])
            inserted_total += len(batch)
            print(f"    {inserted_total} / {grand_total} inserted ...", end="\r")

        print(f"    '{pname}' done ({len(batch_list)} chunks){'':20}")

    print(f"\nAll {inserted_total} chunks inserted across {len(ALL_PARTITIONS)} partitions.")

    # Build vector index
    print(f"\nBuilding IVF_FLAT index on 'vector' field for {safe_col_name}...")
    col.create_index("vector", {
        "index_type": "IVF_FLAT",
        "metric_type": "COSINE",
        "params": {"nlist": 128},
    })
    
    print(f"Flushing data for {safe_col_name}...")
    col.flush()
    col.load()
    print(f"Index built and data flushed. Collection '{safe_col_name}' loaded.")
    
    # Verify counts
    print(f"\nVerifying entity counts for '{safe_col_name}':")
    for pname in ALL_PARTITIONS:
        p = Partition(col, pname)
        count = p.num_entities
        print(f"  Partition '{pname}': {count} entities")
    print(f"  Total Collection Entities: {col.num_entities}")

    # Summary
    print(f"\n{'─'*45}")
    print(f"{'Partition':<25} {'Chunks':>8}  {'% of total':>10}")
    print(f"{'─'*45}")
    for pname in ALL_PARTITIONS:
        n = len(by_partition.get(pname, []))
        pct = n / grand_total * 100 if grand_total else 0
        print(f"  {pname:<23} {n:>8}  {pct:>9.1f}%")
    print(f"{'─'*45}")
    print(f"  {'TOTAL':<23} {grand_total:>8}")
    print(f"{'─'*45}\n")


def ingest():
    print("\n" + "═" * 60)
    print(f"ONDC MILVUS INGESTION")
    print("═" * 60)

    print("\nCollecting chunks from source directories ...")
    all_chunks = collect_all_chunks()

    if not all_chunks:
        print("[ERROR] No chunks produced. Check source directories.")
        return

    
    ctr = Counter((c["source_type"], c["chunk_type"]) for c in all_chunks)
    print(f"\nTotal chunks: {len(all_chunks)}")
    for (st, ct), n in sorted(ctr.items()):
        print(f"  {st:<15}  {ct:<20}  {n:>5}")

    # Group chunks by format: domain and version
    # Group by (domain, version)
    groups = defaultdict(list)
    for c in all_chunks:
        d = c.get("_domain") or DEFAULT_DOMAIN
        v = c.get("_version") or DEFAULT_API_VERSION
        key = (d, v)
        groups[key].append(c)

    # Ingest each group to a dynamically named collection
    for (d, v), chunks in groups.items():
        ingest_milvus(chunks, d, v)

    print("═" * 60)
    print("Ingestion complete.")
    print("═" * 60 + "\n")