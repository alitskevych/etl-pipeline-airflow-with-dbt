with sales as (
    select * from {{ ref('stg_sales') }}
)

select
    *,
    row_number() over (renamed.partition by customer_id order by sales_date) as order_number,
    sum(total_price) over (renamed.partition by customer_id order by sales_date rows between unbounded preceding and current row) as running_total
from sales
