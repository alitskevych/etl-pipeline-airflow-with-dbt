from airflow import DAG
from airflow.operators.bash import BashOperator
from pendulum import datetime

default_args = {
    "start_date": datetime(2023, 1, 1),
}

with DAG(
    dag_id="load_raw_data",
    default_args=default_args,
    schedule=None,
    catchup=False,
    description="Load raw data from sources using dbt",
    tags=["dbt", "raw"],
) as dag:


    dbt_run_raw = BashOperator(
        task_id="run_dbt_raw_models",
        bash_command=(
            "dbt run "
            "--project-dir /usr/local/airflow/dbt/jaffle_shop "
            "--profiles-dir /usr/local/airflow/dbt/profiles "
            "--select path:models/raw"
        ),
        dag=dag,
    )
