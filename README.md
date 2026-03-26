# YouTube ETL Pipeline using Airflow + Spark + Docker

Production-style ETL pipeline built with Apache Airflow, PySpark, Docker, and YouTube API.

This project demonstrates a real-world Data Engineering workflow using Bronze / Silver / Gold architecture.

---

## Architecture

YouTube API  
↓  
Extract (Python)  
↓  
Bronze JSON  
↓  
Spark Silver  
↓  
Spark Gold  
↓  
Airflow DAG  
↓  
Dockerized execution  

---

## Tech Stack

- Python
- PySpark
- Apache Airflow
- Docker
- Requests API
- JSON / Parquet
- Postgres
- Redis

---

## Features

- API ingestion pipeline
- Spark transformations
- Airflow scheduling
- Docker environment
- Bronze / Silver / Gold layers
- Production folder structure

---

## Project Structure

```
etl_prod_pipeline/
│
├── dags/
├── jobs/
│   ├── extract/
│   ├── silver/
│   ├── gold/
│
├── config/
├── data/
├── requirements.txt
├── docker-compose.yaml
└── README.md
```

---

## Run

Start docker

```
docker compose up
```

Open Airflow UI

```
http://localhost:8080
```

Run DAG

```
youtube_etl_pipeline
```

---

## Author

Dheeraj Reddy  
Data Engineering Portfolio Project
