USE Retail_Analytics;
GO

-- 1. Migrate Data from Raw Import Tables
INSERT INTO customers SELECT * FROM customers_raw;
INSERT INTO orders SELECT * FROM orders_raw;
INSERT INTO order_payments SELECT * FROM order_payments_raw;

-- 2. Drop Temporary Raw Tables to clean database
DROP TABLE customers_raw;
DROP TABLE orders_raw;
DROP TABLE order_payments_raw;