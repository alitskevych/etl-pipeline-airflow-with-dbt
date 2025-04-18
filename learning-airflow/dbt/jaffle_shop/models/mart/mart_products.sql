with products as (
    select * from {{ ref('stg_products') }}
),
sales as (
    select * from {{ ref('stg_sales') }}
),
product_stats as (
    select
        product_id,
        count(*) as num_sales,
        sum(quantity) as total_quantity_sold,
        sum(total_price) as total_revenue
    from sales
    group by product_id
)
select
    p.*,
    ps.num_sales,
    ps.total_quantity_sold,
    ps.total_revenue
from products p
left join product_stats ps on p.product_id = ps.product_id
