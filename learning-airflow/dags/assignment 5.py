from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.hooks.mysql_hook import MySqlHook
from datetime import datetime
import pandas as pd
import duckdb

# Constants
DUCKDB_PATH = "/usr/local/airflow/data/final_output.duckdb"
CSV_PATH = "/usr/local/airflow/data/products.csv"  # Ensure file is accessible inside Docker


# ETL Functions

def extract_data_from_mysql(**kwargs):
    try:
        # Use Airflow connection
        mysql_hook = MySqlHook(mysql_conn_id='mysql_default')
        conn = mysql_hook.get_sqlalchemy_engine().raw_connection()
        query = "SELECT * FROM sales;"
        df = pd.read_sql(query, conn)
        conn.close()

        kwargs['ti'].xcom_push(key='sales_data', value=df.to_json())
        print("✅ MySQL data extracted and pushed to XCom")
    except Exception as e:
        print(f"❌ Error extracting from MySQL: {e}")
        raise


def extract_data_from_csv(**kwargs):
    df = pd.read_csv(CSV_PATH)
    kwargs['ti'].xcom_push(key='products_data', value=df.to_json())
    print("✅ CSV data extracted and pushed to XCom")


def transform_data(**kwargs):
    ti = kwargs['ti']
    sales_df = pd.read_json(ti.xcom_pull(key='sales_data'))
    products_df = pd.read_json(ti.xcom_pull(key='products_data'))

    merged_df = sales_df.merge(products_df, on='ProductID', how='left')
    merged_df['Revenue'] = merged_df['TotalPrice'] - (merged_df['Discount'] * merged_df['Quantity'])

    kwargs['ti'].xcom_push(key='transformed_data', value=merged_df.to_json())
    print("✅ Data transformed and pushed to XCom")


def load_data_to_duckdb(**kwargs):
    df = pd.read_json(kwargs['ti'].xcom_pull(key='transformed_data'))
    conn = duckdb.connect(DUCKDB_PATH)
    conn.execute("CREATE TABLE IF NOT EXISTS sales_products AS SELECT * FROM df")
    conn.close()
    print("✅ Data loaded into DuckDB")


# Define DAG
default_args = {
    "owner": "airflow",
    "start_date": datetime(2024, 3, 1),
    "catchup": False
}

with DAG(
        dag_id="assignment_5_dag",
        default_args=default_args,
        schedule_interval="@daily",
        catchup=False,
        tags=["ETL", "mysql", "csv", "duckdb"],
) as dag:
    extract_mysql_task = PythonOperator(
        task_id="extract_data_from_mysql",
        python_callable=extract_data_from_mysql,
        provide_context=True,
    )

    extract_csv_task = PythonOperator(
        task_id="extract_data_from_csv",
        python_callable=extract_data_from_csv,
        provide_context=True,
    )

    transform_task = PythonOperator(
        task_id="transform_join_and_calculate_revenue",
        python_callable=transform_data,
        provide_context=True,
    )

    load_duckdb_task = PythonOperator(
        task_id="load_to_duckdb_table",
        python_callable=load_data_to_duckdb,
        provide_context=True,
    )

    # Task pipeline
    extract_mysql_task >> extract_csv_task >> transform_task >> load_duckdb_task
