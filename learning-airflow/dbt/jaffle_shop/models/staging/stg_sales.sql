with source as (
    select * from {{ ref('raw_sales') }}
),

renamed as (
    select
        SalesID as sales_id,
        SalesPersonID as sales_person_id,
        CustomerID as customer_id,
        ProductID as product_id,
        Quantity as quantity,
        Discount as discount,
        TotalPrice as total_price,
        SalesDate as sales_date,
        TransactionNumber as transaction_number
    from source
)

select * from renamed
