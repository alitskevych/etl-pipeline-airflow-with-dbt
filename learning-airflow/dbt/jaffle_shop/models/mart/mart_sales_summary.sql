{{
  config(
    materialized='incremental',
    unique_key='customer_id'
  )
}}

with source_data as (
    select
        customer_id,
        sum(total_price) as total_spent,
        count(*) as total_orders
    from {{ ref('stg_sales') }}
    group by customer_id
)

select
    {% for col in get_filtered_columns_in_relation(ref('stg_sales'), ['total_orders']) %}
      {{ col }}{% if not loop.last %}, {% endif %}
    {% endfor %},
    total_orders
from source_data
