from datetime import datetime
from airflow import DAG 
#from airflow.operators.python import PythonOperator

default_args={
    'owner':'fawz',
    'start_date':datetime(2024,4,9,3,00)
}

def stream_data():
    import requests
    import json
    res=requests.get("https://randomuser.me/api/")
    print(res.json())
#with DAG('kafka_stream',default_args=default_args,schedule_interval='@daily',catchup=False)as dag:
    #streaming_task=PythonOperator(task_id='stream_data_from_api', 
                                # python_callable=stream_data)

stream_data();    