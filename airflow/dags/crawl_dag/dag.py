import requests

from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from crawl_dag.load_config import api_key, mongo_uri

def get_video_stats(video_id):
    print("api_key", api_key)

    url = "https://www.googleapis.com/youtube/v3/videos"
    params = {
        "part": "statistics",
        "id": video_id,
        "key": api_key
    }
    response = requests.get(url, params=params)
    data = response.json()
    print("data", data)
    stats = data["items"][0]["statistics"]
    return {
        "viewCount": int(stats.get("viewCount", 0)),
        "likeCount": int(stats.get("likeCount", 0)),
        "commentCount": int(stats.get("commentCount", 0))
    }

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
    task_1 = PythonOperator(
        task_id="crawl_video_stats_from_youtube_api",
        python_callable=get_video_stats,
        op_kwargs={'video_id': "bu39oUbbHxc"}
    )

    task_1
