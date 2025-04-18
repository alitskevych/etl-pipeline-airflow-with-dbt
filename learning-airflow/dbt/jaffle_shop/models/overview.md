{% docs __overview__ %}

## Jaffle Shop: Data Documentation Overview

The `jaffle_shop` project is a fictional e-commerce store designed to demonstrate and test `dbt` functionality. This project showcases how to transform raw data into meaningful insights using `dbt`.

### Project Structure

- **Raw Models**: Represent unprocessed data ingested from source systems. These models serve as the foundation for all transformations.
- **Staging Models**: Clean and standardize raw data, preparing it for downstream transformations and aggregations.
- **Mart Models**: Contain aggregated and transformed data optimized for reporting and analytics.

### Key Features

- **Data Transformation**: Transform raw data into clean, structured datasets.
- **Testing**: Ensure data quality with built-in tests for uniqueness, null values, and referential integrity.
- **Documentation**: Comprehensive documentation for all models, making it easy to understand the data pipeline.

### Source Code

The source code for this project is available on [GitHub](https://github.com/clrcrl/jaffle_shop).

{% enddocs %}