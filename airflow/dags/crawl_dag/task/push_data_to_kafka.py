import json

from kafka import KafkaProducer


def push_to_kafka(**context):
    data = context['ti'].xcom_pull(task_ids='fetch_youtube')
    print("--receive", data)
    producer = KafkaProducer(
        bootstrap_servers='host.docker.internal:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    for record in data:
        producer.send("youtube_metrics", value=record)
    producer.flush()
    producer.close()
