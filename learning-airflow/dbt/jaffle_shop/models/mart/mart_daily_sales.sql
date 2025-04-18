select
    date(sales_date) as sales_day,
    count(*) as total_orders,
    sum(quantity) as total_items_sold,
    sum(total_price) as revenue
from {{ ref('stg_sales') }}
group by 1
order by 1
