from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

from dataquality import validate_data, process_data

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'retries': 1,
}

dag = DAG(
    'data_quality_dag',
    default_args=default_args,
    description='A DAG to process data and check quality',
    schedule_interval='@daily',
)

def validate_data_task(**kwargs):
    try:
       
        df = process_data('heart.csv')
   
        validate_data(df)
        print("Data validated.")
    except Exception as e:
        print(f"Error in data validation: {e}")
        raise

validate_task = PythonOperator(
    task_id='validate_data',
    python_callable=validate_data_task,
    provide_context=True,
    dag=dag,
)

validate_task
