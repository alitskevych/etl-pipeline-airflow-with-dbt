FROM quay.io/astronomer/astro-runtime:12.8.0

WORKDIR "/usr/local/airflow"

# Встановлюємо всі залежності глобально
COPY dbt-requirements.txt ./
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r dbt-requirements.txt



