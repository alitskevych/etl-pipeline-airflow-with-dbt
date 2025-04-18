with sales as (
    select * from {{ ref('stg_sales') }}
)
select
    *,
    sum(total_price) over (renamed.partition by sales_person_id) as total_sales_per_employee,
    rank() over (renamed.partition by sales_person_id order by sales_date desc) as sales_rank
from sales
