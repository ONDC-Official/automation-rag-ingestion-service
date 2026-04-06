# Base Image
FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    dos2unix \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

# Set working directory - all subsequent COPIES go here
WORKDIR /app

# 1. Copy requirements first (better for Docker caching)
# Assuming your local structure has these folders
COPY milvus/requirements.txt ./milvus/requirements.txt
COPY knowledge-graph-python/requirements.txt ./knowledge-graph-python/requirements.txt


RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r milvus/requirements.txt && \
    pip install --no-cache-dir -r knowledge-graph-python/requirements.txt

# 2. Copy the entire project into /app
# This ensures ingest.py and the folders are all in /app/
COPY . .

# 3. Handle the entrypoint
# Since entrypoint.sh was just copied into /app, we reference it there
RUN dos2unix entrypoint.sh && chmod +x entrypoint.sh

# Environment
ENV PYTHONUNBUFFERED=1

# Use the absolute path to the entrypoint now that it's in /app
ENTRYPOINT ["/app/entrypoint.sh"]