import requests

from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from crawl_dag.load_config import api_key, mongo_uri

from crawl_dag.task.crawl import get_video_stats
from crawl_dag.task.push_data_to_kafka import push_to_kafka

default_args = {
    "owner": "Linh",
    "retry": 5,
    "delay": timedelta(minutes=2)
}
with DAG(
    dag_id="dag_crawl_video_data_v1",
    default_args=default_args,
    description="This dag is used for crawl data from Youtube API",
    start_date=datetime(2025, 7, 3, 5),
    schedule_interval="* * * * *",
    catchup=False,
) as dag:
    fetch_task = PythonOperator(
        task_id="fetch_youtube",
        python_callable=get_video_stats,
        op_kwargs={'video_id': "bu39oUbbHxc"}
    )
    kafka_task = PythonOperator(
        task_id='push_to_kafka',
        python_callable=push_to_kafka,
        provide_context=True
    )

    fetch_task >> kafka_task

