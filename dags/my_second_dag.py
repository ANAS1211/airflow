from airflow.operators.python import PythonOperator
import datetime
from airflow import DAG
from airflow.utils.dates import days_ago

my_second_dag=DAG(
    dag_id="my_second_dag",
    description='My second DAG',
    tags=['tutorial_2', 'datascientest2'],
    schedule_interval=None,
    default_args={
        'owner': 'airflow',
        'start_date': days_ago(2),
    }
    )

def print_hello():
    print("hello from task 1")
    
my_task = PythonOperator(
    task_id='second_dag_task1',
    python_callable=print_hello,
    dag=my_second_dag
)

