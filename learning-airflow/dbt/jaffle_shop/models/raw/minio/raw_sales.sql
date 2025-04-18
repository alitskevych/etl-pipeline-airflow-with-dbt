select * from {{ source('minio', 'sales') }}
