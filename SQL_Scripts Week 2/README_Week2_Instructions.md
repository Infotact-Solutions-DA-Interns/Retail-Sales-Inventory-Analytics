# Week 2: SQL Development & Metrics

## Instructions for Data Import (Kasak & Ahmad)
1. **Database Creation:** Please run `01_create_schema.sql` in your local MySQL/PostgreSQL environment to create the empty tables.
2. **Data Import Order:** You MUST import the CSV files in this exact order to avoid Foreign Key errors:
   - First: `olist_orders_dataset.csv` (into the `orders` table)
   - Second: `olist_products_dataset.csv` (into the `products` table)
   - Third: `olist_order_payments_dataset.csv` (into `order_payments`)
   - Fourth: `olist_order_items_dataset.csv` (into `order_items`)
3. **Status Update:** Please confirm in the team chat once your local databases are populated so we can begin writing the metric queries.
