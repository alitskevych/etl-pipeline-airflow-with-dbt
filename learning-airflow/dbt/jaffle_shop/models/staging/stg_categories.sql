with source as (
    select * from {{ ref('raw_categories') }}
),

renamed as (
    select
        CategoryID as category_id,
        CategoryName as category_name
    from source
)

select * from renamed
