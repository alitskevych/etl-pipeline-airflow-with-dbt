select * from {{ source('mysql', 'categories') }}
