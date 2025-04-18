
  
    
    

    create  table
      "my_duckdb"."main"."raw_employees__dbt_tmp"
  
    as (
      select * from "my_duckdb"."main"."employees"
    );
  
  