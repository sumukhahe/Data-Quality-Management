from airflow import DAG
import pandas as pd
from airflow.operators.python import PythonOperator
from datetime import datetime
from dataquality import validate_data

def data_quality_task():
    df = pd.read_csv('heart.csv')
    validate_data(df)

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 9, 1),
    'retries': 1,
}

with DAG('validate_data_dag', default_args=default_args, schedule_interval='@daily') as dag:
    validate_data_task = PythonOperator(
        task_id='validate_data_task',
        python_callable=data_quality_task
    )
