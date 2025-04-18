
  
    
    

    create  table
      "my_duckdb"."main"."raw_products__dbt_tmp"
  
    as (
      select * from "my_duckdb"."main"."products"
    );
  
  