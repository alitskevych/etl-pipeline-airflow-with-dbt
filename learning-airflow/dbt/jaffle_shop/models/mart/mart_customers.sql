with customers as (
    select * from {{ ref('stg_customers') }}
),
sales as (
    select * from {{ ref('stg_sales') }}
),
agg as (
    select
        s.customer_id,
        count(*) as total_orders,
        sum(s.total_price) as total_revenue,
        min(s.sales_date) as first_order_date,
        max(s.sales_date) as last_order_date
    from sales s
    group by s.customer_id
)
select
    c.*,
    a.total_orders,
    a.total_revenue,
    a.first_order_date,
    a.last_order_date
from customers c
left join agg a on c.customer_id = a.customer_id
