# YouTube ETL Pipeline (Airflow + Spark + Docker)

Production-style ETL pipeline built using:

- Python
- PySpark
- Apache Airflow
- Docker
- YouTube API
- Bronze / Silver / Gold architecture

## Architecture

YouTube API → Extract → Bronze JSON → Spark Silver → Spark Gold → Airflow DAG

## Tech Stack

- Python
- PySpark
- Airflow
- Docker
- Requests
- JSON
- Parquet

## Features

- API ingestion
- Spark transformation
- Airflow scheduling
- Dockerized environment
- Production folder structure

## Run

```bash
docker compose up
