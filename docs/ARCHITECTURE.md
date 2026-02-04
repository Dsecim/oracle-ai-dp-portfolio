# Architecture — Oracle AI Data Platform (AI DP) Portfolio

## Overview

This project demonstrates an end-to-end AI Data Platform architecture on Oracle Cloud Infrastructure using:

- Mock data generation (Python)
- Spark-based processing (OCI Data Flow)
- Data Lake on Object Storage
- Autonomous Data Warehouse (ADW)
- Machine Learning with OCI Data Science

The goal is to show how data flows from ingestion to analytics and ML in a cloud-native and scalable way.

---

## High-Level Architecture

Data Flow:

1. Python script generates mock customer data
2. Raw data is stored in OCI Object Storage
3. Spark job (OCI Data Flow) performs ETL and writes curated data
4. Curated data is loaded into Autonomous Data Warehouse
5. OCI Data Science trains a churn prediction model
6. Model generates predictions consumed by BI or applications

---

## Architecture Diagram

See: `diagrams/architecture.drawio`

---

## Components

### 1. Data Generator (Python)
- Generates synthetic customer dataset
- Parameterized number of rows
- Deterministic using random seed

### 2. Object Storage (Raw Zone)
- Stores raw CSV files
- Acts as landing zone

### 3. OCI Data Flow (Spark ETL)
- Performs type casting and data quality checks
- Removes duplicates
- Creates enrichment columns
- Writes curated Parquet files

### 4. Object Storage (Processed Zone)
- Stores Parquet curated data
- Used by ML and DW

### 5. Autonomous Data Warehouse
- Stores structured table `CLIENTES_CHURN`
- Optimized for analytics

### 6. OCI Data Science
- Trains RandomForest model
- Saves model artifact
- Runs batch predictions

---

## Security & Governance

- Secrets stored in environment variables
- No credentials committed to Git
- Data encrypted at rest (OCI managed)

---

## Scalability

- Spark scales horizontally in OCI Data Flow
- Object Storage supports petabyte scale
- Autonomous DB auto-scales compute

---

## CI/CD

- GitHub Actions validates code
- Linting (ruff, black)
- Tests (pytest)
- Release workflow packages artifacts

---

## Future Improvements

- Add streaming ingestion
- Add feature store
- Add model registry
- Add monitoring and drift detection
