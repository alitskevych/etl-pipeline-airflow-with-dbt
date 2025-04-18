# dags/export_to_duckdb.py
from airflow import DAG
from airflow.operators.python import PythonOperator
from pendulum import datetime
import polars as pl
import duckdb

MART_TABLES = [
    "mart_sales_summary", "mart_sales_detailed", "mart_product_performance",
    "mart_customer_lifetime_value", "mart_sales_by_region", "mart_monthly_sales",
    "mart_top_customers", "mart_sales_trends"
]

def export_marts():
    conn_mysql = duckdb.connect()  # якщо dbt вже зберігає у DuckDB, то цього досить
    conn_duckdb = duckdb.connect("C:/Users/ARTEM/learning-airflow/output.duckdb")

    for table in MART_TABLES:
        df = conn_mysql.execute(f"SELECT * FROM {table}").fetchdf()
        pl_df = pl.from_pandas(df)
        conn_duckdb.execute(f"CREATE OR REPLACE TABLE {table} AS SELECT * FROM pl_df")

with DAG(
    dag_id="export_to_duckdb",
    start_date=datetime(2023, 1, 1),
    schedule=None,
    catchup=False,
    tags=["export", "duckdb"],
) as dag:

    export = PythonOperator(
        task_id="export_marts_to_duckdb",
        python_callable=export_marts,
    )
