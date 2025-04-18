select * from {{ source('mysql', 'cities') }}
