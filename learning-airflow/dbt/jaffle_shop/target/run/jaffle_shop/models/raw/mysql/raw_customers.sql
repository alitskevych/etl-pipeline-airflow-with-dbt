
  
    
    

    create  table
      "my_duckdb"."main"."raw_customers__dbt_tmp"
  
    as (
      select * from "my_duckdb"."main"."customers"
    );
  
  