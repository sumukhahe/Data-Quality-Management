from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from real_time_monitoring import real_time_monitoring  

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 9, 1),
    'retries': 1,
}


with DAG('real_time_monitoring_dag',
         default_args=default_args,
         schedule_interval=timedelta(hours=1),  
         catchup=False) as dag:
    
    monitor_task = PythonOperator(
        task_id='monitor_data_quality_task',
        python_callable=real_time_monitoring
    )
