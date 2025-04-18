select * from {{ source('mysql', 'customers') }}
