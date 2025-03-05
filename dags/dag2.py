from airflow.decorators import dag, task
from datetime import datetime


# Define the DAG using the @dag decorator
@dag(
    dag_id="hello_world_taskflow_dag_2",
    schedule_interval="@daily",  # Run the DAG daily
    start_date=datetime(2023, 10, 1),
    catchup=False,
    tags=["prod"],
)
def hello_world_dag():
    # Define the task using the @task decorator
    @task
    def print_hello():
        print("Hello, World 2!")

    # Call the task function to add it to the DAG
    print_hello()


# Instantiate the DAG
dag = hello_world_dag()
