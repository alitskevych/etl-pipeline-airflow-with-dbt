
  
    
    

    create  table
      "my_duckdb"."main"."raw_sales__dbt_tmp"
  
    as (
      select * from "my_duckdb"."main"."sales"
    );
  
  