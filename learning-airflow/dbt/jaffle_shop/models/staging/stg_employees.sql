with source as (
    select * from {{ ref('raw_employees') }}
),

renamed as (
    select
        EmployeeID as employee_id,
        FirstName as first_name,
        MiddleInitial as middle_initial,
        LastName as last_name,
        BirthDate as birth_date,
        Gender as gender,
        CityID as city_id,
        HireDate as hire_date
    from source
)

select * from renamed
