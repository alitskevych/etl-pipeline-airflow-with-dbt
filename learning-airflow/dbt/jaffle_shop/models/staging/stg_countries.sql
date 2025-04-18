with source as (
    select * from {{ ref('raw_countries') }}
),

renamed as (
    select
        CountryID as country_id,
        CountryName as country_name,
        CountryCode as country_code
    from source
)

select * from renamed
