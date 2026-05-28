USE Retail_Analytics;
GO

-- 1. Create Customers Table
CREATE TABLE customers (
    customer_id NVARCHAR(255) PRIMARY KEY,
    customer_unique_id NVARCHAR(255),
    customer_zip_code_prefix NVARCHAR(255),
    customer_city NVARCHAR(255),
    customer_state NVARCHAR(255)
);

-- 2. Create Orders Table
CREATE TABLE orders (
    order_id NVARCHAR(255) PRIMARY KEY,
    customer_id NVARCHAR(255),
    order_status NVARCHAR(50),
    order_purchase_timestamp DATETIME,
    order_approved_at DATETIME,
    order_delivered_carrier_date DATETIME,
    order_delivered_customer_date DATETIME,
    order_estimated_delivery_date DATETIME,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- 3. Create Payments Table 
CREATE TABLE order_payments (
    order_id NVARCHAR(255),
    payment_sequential INT,
    payment_type NVARCHAR(50),
    payment_installments INT,
    payment_value DECIMAL(10, 2),
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);

-- 4. Create Products Table
CREATE TABLE products (
    product_id NVARCHAR(255) PRIMARY KEY,
    product_category_name NVARCHAR(255),
    product_name_length INT,
    product_description_length INT,
    product_photos_qty INT,
    product_weight_g INT,
    product_length_cm INT,
    product_height_cm INT,
    product_width_cm INT
);

-- 5. Create Order Items Table
CREATE TABLE order_items (
    order_id NVARCHAR(255),
    order_item_id INT,
    product_id NVARCHAR(255),
    seller_id NVARCHAR(255),
    shipping_limit_date DATETIME,
    price DECIMAL(10, 2),
    freight_value DECIMAL(10, 2),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);