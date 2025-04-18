with sales as (
    select * from {{ ref('stg_sales') }}
)
select
    customer_id,
    sum(total_price) as lifetime_value,
    avg(total_price) as avg_order_value,
    count(*) as total_orders,
    dense_rank() over (order by sum(total_price) desc) as ltv_rank
from sales
group by customer_id
