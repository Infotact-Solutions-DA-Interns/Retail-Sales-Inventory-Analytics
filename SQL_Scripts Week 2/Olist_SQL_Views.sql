USE Retail_Analytics;
GO

-- 1. REGIONAL REVENUE VIEW
CREATE OR ALTER VIEW vw_regional_revenue AS
SELECT 
    c.customer_state,
    c.customer_city,
    COUNT(DISTINCT o.order_id) AS total_orders,
    SUM(op.payment_value) AS total_revenue
FROM orders o
JOIN order_payments op ON o.order_id = op.order_id
JOIN customers c ON o.customer_id = c.customer_id
GROUP BY c.customer_state, c.customer_city;
GO

-- 2. REVENUE TREND VIEW
CREATE OR ALTER VIEW vw_revenue_trend AS
SELECT 
    CAST(o.order_purchase_timestamp AS DATE) AS order_date,
    SUM(op.payment_value) AS daily_revenue,
    COUNT(DISTINCT o.order_id) AS total_orders
FROM orders o
JOIN order_payments op ON o.order_id = op.order_id
WHERE o.order_purchase_timestamp IS NOT NULL AND o.order_status = 'delivered'
GROUP BY CAST(o.order_purchase_timestamp AS DATE);
GO

-- 3. PAYMENT PREFERENCE VIEW
CREATE OR ALTER VIEW vw_payment_preference AS
SELECT 
    payment_type,
    COUNT(DISTINCT order_id) AS total_orders,
    SUM(payment_value) AS total_revenue
FROM order_payments
GROUP BY payment_type;
GO

-- 4. DELIVERY PERFORMANCE VIEW
CREATE OR ALTER VIEW vw_delivery_performance AS
SELECT 
    order_id,
    order_status,
    CAST(order_purchase_timestamp AS DATETIME) AS purchase_time,
    CAST(order_delivered_customer_date AS DATETIME) AS actual_delivery_time,
    CAST(order_estimated_delivery_date AS DATETIME) AS estimated_delivery_time,
    DATEDIFF(day, CAST(order_purchase_timestamp AS DATETIME), CAST(order_delivered_customer_date AS DATETIME)) AS actual_delivery_days,
    DATEDIFF(day, CAST(order_purchase_timestamp AS DATETIME), CAST(order_estimated_delivery_date AS DATETIME)) AS promised_delivery_days
FROM orders
WHERE order_status = 'delivered' 
    AND order_purchase_timestamp IS NOT NULL 
    AND order_delivered_customer_date IS NOT NULL 
    AND order_estimated_delivery_date IS NOT NULL;
GO

-- 5. WEEK 2: PERFORMANCE INDEXES
CREATE NONCLUSTERED INDEX idx_orders_customer_id ON orders(customer_id);
CREATE NONCLUSTERED INDEX idx_payments_order_id ON order_payments(order_id);
CREATE NONCLUSTERED INDEX idx_customers_state ON customers(customer_state);
GO

-- 6. WEEK 2: CTE AND WINDOW FUNCTION (Ranking Cities)
CREATE OR ALTER VIEW vw_top_cities_by_state AS
WITH CityRevenueCTE AS (
    SELECT 
        c.customer_state,
        c.customer_city,
        SUM(op.payment_value) AS total_revenue
    FROM orders o
    JOIN order_payments op ON o.order_id = op.order_id
    JOIN customers c ON o.customer_id = c.customer_id
    GROUP BY c.customer_state, c.customer_city
)
SELECT 
    customer_state,
    customer_city,
    total_revenue,
    ROW_NUMBER() OVER(PARTITION BY customer_state ORDER BY total_revenue DESC) as city_rank
FROM CityRevenueCTE;
GO