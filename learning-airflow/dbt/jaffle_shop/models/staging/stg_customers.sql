with source as (
    select * from {{ ref('raw_customers') }}
),

renamed as (
    select
        CustomerID as customer_id,
        FirstName as first_name,
        MiddleInitial as middle_initial,
        LastName as last_name,
        CityID as city_id,
        Address as address
    from source
)

select * from renamed