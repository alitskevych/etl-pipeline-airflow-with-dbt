from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import duckdb
import pandas as pd
import sqlalchemy

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
}

dag = DAG(
    dag_id='import_data_to_duckdb',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    description='Load sales from MinIO and other tables from MySQL into DuckDB',
)


def load_sales_from_minio():
    con = duckdb.connect('/usr/local/airflow/dbt/jaffle_shop/my_duckdb.db')

    con.sql("INSTALL httpfs; LOAD httpfs;")
    con.sql("SET s3_region='us-east-1';")
    con.sql("SET s3_access_key_id='minioadmin';")
    con.sql("SET s3_secret_access_key='minioadmin';")
    con.sql("SET s3_endpoint='http://host.docker.internal:9000';")
    con.sql("SET s3_url_style='path';")
    con.sql("SET s3_use_ssl=false;")

    con.sql("""
        CREATE OR REPLACE TABLE main.sales AS
        SELECT * FROM read_csv_auto('s3://my-dbt-source/sales.csv');
    """)


def load_mysql_tables_to_duckdb():
    duckdb_path = '/usr/local/airflow/dbt/jaffle_shop/my_duckdb.db'
    con = duckdb.connect(duckdb_path)

    mysql_url = "mysql+pymysql://airflow:airflowpass@host.docker.internal:3306/test_db"
    engine = sqlalchemy.create_engine(mysql_url)

    tables = ['cities', 'customers', 'countries', 'categories', 'employees', 'products']

    for table in tables:
        df = pd.read_sql_table(table, con=engine)
        con.register('tmp_df', df)
        con.sql(f"CREATE OR REPLACE TABLE main.{table} AS SELECT * FROM tmp_df;")


load_sales_task = PythonOperator(
    task_id='load_sales_from_minio',
    python_callable=load_sales_from_minio,
    dag=dag
)

load_mysql_task = PythonOperator(
    task_id='load_mysql_tables',
    python_callable=load_mysql_tables_to_duckdb,
    dag=dag
)

load_sales_task >> load_mysql_task
