from airflow import DAG
from airflow.operators.bash import BashOperator
from pendulum import datetime

default_args = {
    "start_date": datetime(2023, 1, 1),
}

with DAG(
    dag_id="transform_data",
    default_args=default_args,
    schedule=None,
    catchup=False,
    description="Transform staged data into marts using dbt",
    tags=["dbt", "transform"],
) as dag:

    dbt_run_stage = BashOperator(
        task_id="run_dbt_stage_models",
        bash_command="dbt run --project-dir /usr/local/airflow/dbt/jaffle_shop --select path:models/stage",
    )

    dbt_run_marts = BashOperator(
        task_id="run_dbt_mart_models",
        bash_command="dbt run --project-dir /usr/local/airflow/dbt/jaffle_shop --select path:models/mart",
    )

    dbt_run_stage >> dbt_run_marts
