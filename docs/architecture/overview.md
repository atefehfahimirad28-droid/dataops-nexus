# Architecture Overview

## Purpose

DataOps Nexus is designed as a modular DataOps platform rather than a single ETL script.

Its architecture separates ingestion, event streaming, processing, orchestration, storage, observability, and AI-assisted operations.

## Architectural Principles

1. Event-driven ingestion
2. Clear separation of responsibilities
3. Immutable Bronze data
4. Validated Silver data
5. Business-ready Gold data
6. Idempotent processing
7. Observable pipeline runs
8. Metadata and lineage by design
9. Security and least privilege
10. AI grounded in trusted operational context

## Core Components

### FastAPI

Accepts ingestion requests, validates inputs, and creates platform events.

### Apache Kafka

Decouples ingestion from processing and provides durable event delivery.

### PySpark

Processes large datasets, applies transformations, and evaluates data-quality rules.

### Databricks and Delta Lake

Provide lakehouse capabilities such as ACID tables, schema enforcement, MERGE, and Time Travel.

### Apache Airflow

Coordinates scheduled and dependency-based workflows.

### PostgreSQL

Stores metadata, pipeline runs, quality results, catalog entries, and lineage relationships.

### Streamlit

Provides a self-service user interface for pipeline operations and monitoring.

### AI Incident Investigator

Analyzes logs, metadata, lineage, and quality failures to suggest probable root causes and remediation steps.

## Data Flow

```text
Source
  ↓
FastAPI
  ↓
Kafka
  ↓
Bronze
  ↓
PySpark
  ↓
Silver
  ↓
Gold
  ↓
PostgreSQL / Delta Lake
  ↓
Dashboard / Catalog / Lineage / AI
