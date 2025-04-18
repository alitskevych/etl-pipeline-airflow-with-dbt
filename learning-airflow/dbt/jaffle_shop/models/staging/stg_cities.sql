with source as (
    select * from {{ ref('raw_cities') }}
),

renamed as (
    select
        CityID as city_id,
        CityName as city_name,
        Zipcode as zipcode,
        CountryID as country_id
    from source
)

select * from renamed
