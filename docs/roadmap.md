# DataOps Nexus Roadmap

## Phase 1 — Project Foundation

- [x] Create repository
- [x] Create Issue-driven workflow
- [x] Create feature branch
- [x] Pin Python 3.12
- [x] Configure uv
- [x] Configure Ruff
- [x] Configure MyPy
- [x] Configure Pytest
- [x] Add initial test
- [x] Add GitHub Actions CI
- [ ] Add README and architecture documentation
- [ ] Open and review the first pull request
- [ ] Merge the foundation into main

## Phase 2 — API and Metadata

- [ ] Build FastAPI application
- [ ] Add health endpoints
- [ ] Add PostgreSQL
- [ ] Create pipeline-run metadata model
- [ ] Add file-ingestion endpoint
- [ ] Add API tests

## Phase 3 — Kafka Streaming

- [ ] Define event envelope
- [ ] Create Kafka topics
- [ ] Implement producer
- [ ] Implement consumer
- [ ] Add idempotency
- [ ] Add retry and Dead Letter Queue

## Phase 4 — PySpark and Medallion Layers

- [ ] Implement Bronze ingestion
- [ ] Implement Silver validation
- [ ] Implement quarantine dataset
- [ ] Implement Gold aggregations
- [ ] Add data-quality metrics

## Phase 5 — Databricks and Delta Lake

- [ ] Create Databricks notebooks
- [ ] Build Delta tables
- [ ] Implement MERGE
- [ ] Demonstrate Time Travel
- [ ] Add Spark SQL analytics

## Phase 6 — Airflow and Product Interface

- [ ] Build Airflow DAG
- [ ] Add retries and timeouts
- [ ] Build Streamlit dashboard
- [ ] Add Data Catalog
- [ ] Add Data Lineage
- [ ] Add Monitoring

## Phase 7 — AI Operations

- [ ] Build AI Incident Investigator
- [ ] Create RAG knowledge sources
- [ ] Add safe read-only SQL assistance
- [ ] Audit AI requests and responses
