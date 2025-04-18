{% docs mart %}
### Mart Models
The `mart` directory contains 8 models that represent aggregated and transformed data for reporting and analytics purposes.

#### Models:
- **mart_sales_summary**: Aggregated sales data summarizing total spent and total orders per customer.
- **mart_sales_detailed**: Detailed sales data including running totals and order numbers for each customer.
- **mart_product_performance**: Performance metrics for products, including total sales and revenue.
- **mart_customer_lifetime_value**: Customer lifetime value metrics, including total revenue and average order value.
- **mart_sales_by_region**: Sales data aggregated by region, including total revenue and order count.
- **mart_monthly_sales**: Monthly sales data, including total revenue and order count.
- **mart_top_customers**: Data for top customers based on total revenue and order count.
- **mart_sales_trends**: Sales trends over time, including revenue and order count.
{% enddocs %}

{% docs raw %}
### Raw Models
The `raw` directory contains 7 models that represent the unprocessed data ingested from source systems.

#### Models:
- **raw_customers**: Raw customer data ingested from the source system.
- **raw_orders**: Raw order data ingested from the source system.
- **raw_products**: Raw product data ingested from the source system.
- **raw_sales**: Raw sales data ingested from the source system.
- **raw_regions**: Raw region data ingested from the source system.
- **raw_inventory**: Raw inventory data ingested from the source system.
- **raw_suppliers**: Raw supplier data ingested from the source system.
{% enddocs %}

{% docs staging %}
### Staging Models
The `staging` directory contains 7 models that clean and transform raw data into a more usable format for downstream models.

#### Models:
- **stg_customers**: Cleaned and transformed customer data.
- **stg_orders**: Cleaned and transformed order data.
- **stg_products**: Cleaned and transformed product data.
- **stg_sales**: Cleaned and transformed sales data.
- **stg_regions**: Cleaned and transformed region data.
- **stg_inventory**: Cleaned and transformed inventory data.
- **stg_suppliers**: Cleaned and transformed supplier data.
{% enddocs %}