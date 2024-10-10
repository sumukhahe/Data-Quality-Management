from airflow import DAG
import pandas as pd
from airflow.operators.python import PythonOperator
from datetime import datetime
from data_cleansing import cleanse_data
def data_cleansing_task():
   
    df = pd.read_csv('heart.csv')
    
    
    cleansed_df = cleanse_data(df)
    
   
    cleansed_df.to_csv('processed_heart_data.csv', index=False)
    print("Cleansed data saved successfully.")

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 9, 1),
    'retries': 1,
}


with DAG('cleanse_data_dag', default_args=default_args, schedule_interval='@daily') as dag:
    cleanse_data_task = PythonOperator(
        task_id='cleanse_data_task',
        python_callable=data_cleansing_task
    )

cleanse_data_task
#b