
  
    
    

    create  table
      "my_duckdb"."main"."raw_countries__dbt_tmp"
  
    as (
      select * from "my_duckdb"."main"."countries"
    );
  
  