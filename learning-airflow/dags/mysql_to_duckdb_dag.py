from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.hooks.mysql_hook import MySqlHook
from datetime import datetime
import pandas as pd
import duckdb

DUCKDB_PATH = "/usr/local/airflow/data/sales.duckdb"  # Path for DuckDB file

# Function to extract data from MySQL using MySqlHook
def etl():
    # Extract data
    mysql_hook = MySqlHook(mysql_conn_id='mysql_default')
    conn = mysql_hook.get_sqlalchemy_engine().raw_connection()
    query = "SELECT id, name, price FROM products;"
    df = pd.read_sql(query, conn)
    conn.close()
    print("✅ Data extracted from MySQL.")

    # Transform data
    df["price"] = df["price"] * 1000.1
    print("✅ Data transformed (price increased by 10%).")

    # Load data into DuckDB
    conn = duckdb.connect(DUCKDB_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER,
            name STRING,
            price DOUBLE
        );
    """)
    conn.execute("INSERT INTO products SELECT * FROM df")
    conn.close()

    print("✅ Transformed data inserted into DuckDB.")


# Define Airflow DAG
default_args = {
    "owner": "airflow",
    "start_date": datetime(2024, 3, 1),
    "catchup": False
}

dag = DAG(
    "mysql_to_duckdb_dag",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False,
)

# Define task
etl_task = PythonOperator(
    task_id="transform_data",
    python_callable=etl,
    dag=dag
)

etl_task
