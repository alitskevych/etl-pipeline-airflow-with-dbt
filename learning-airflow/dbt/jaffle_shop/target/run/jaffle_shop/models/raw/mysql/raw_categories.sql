
  
    
    

    create  table
      "my_duckdb"."main"."raw_categories__dbt_tmp"
  
    as (
      select * from "my_duckdb"."main"."categories"
    );
  
  