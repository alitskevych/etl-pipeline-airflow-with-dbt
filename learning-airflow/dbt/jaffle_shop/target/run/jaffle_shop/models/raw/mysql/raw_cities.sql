
  
    
    

    create  table
      "my_duckdb"."main"."raw_cities__dbt_tmp"
  
    as (
      select * from "my_duckdb"."main"."cities"
    );
  
  