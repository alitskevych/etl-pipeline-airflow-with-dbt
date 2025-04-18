with source as (
    select * from {{ ref('raw_products') }}
),

renamed as (
    select
        ProductID as product_id,
        ProductName as product_name,
        Price as price,
        CategoryID as category_id,
        Class as class,
        ModifyDate as modify_date,
        Resistant as resistant,
        IsAllergic as is_allergic,
        VitalityDays as vitality_days
    from source
)

select * from renamed