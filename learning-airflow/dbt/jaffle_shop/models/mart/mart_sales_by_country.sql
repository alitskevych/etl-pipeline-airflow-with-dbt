select
    co.country_name,
    sum(s.total_price) as total_revenue,
    count(*) as num_sales
from {{ ref('stg_sales') }} s
join {{ ref('stg_customers') }} c on s.customer_id = c.customer_id
join {{ ref('stg_cities') }} ci on c.city_id = ci.city_id
join {{ ref('stg_countries') }} co on ci.country_id = co.country_id
group by co.country_name
