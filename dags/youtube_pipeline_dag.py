from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

BASE_PATH = "/opt/airflow/dags"


default_args = {
    "owner": "dheeraj",
    "start_date": datetime(2024, 1, 1),
}


with DAG(
    dag_id="youtube_etl_pipeline",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False,
) as dag:

    extract = BashOperator(
        task_id="extract",
        bash_command=f"python {BASE_PATH}/jobs/extract/youtube_extract.py",
    )

    silver = BashOperator(
        task_id="silver",
        bash_command=f"python {BASE_PATH}/jobs/silver/youtube_silver.py",
    )

    gold = BashOperator(
        task_id="gold",
        bash_command=f"python {BASE_PATH}/jobs/gold/youtube_gold.py",
    )

    extract >> silver >> gold
