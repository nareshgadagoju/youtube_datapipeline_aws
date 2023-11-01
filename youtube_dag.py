from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from youtube_etl import run_youtube_etl  # Import the module where you defined your ETL code

# Define default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 10, 27),  # Modify the start date as needed
    'retries': 1,
}

# Create an Airflow DAG
dag = DAG(
    'youtube_dag',
    default_args=default_args,
    description='youtube project',  # You can specify the schedule_interval here
)

# Define a PythonOperator to run your ETL code
run_etl = PythonOperator(
    task_id='complete_youtube_etl',
    python_callable=run_youtube_etl,  # Replace with the actual function name
    dag=dag,
)
# Set up task dependencies
run_etl