-- View 1: Revenue by Category for Power BI / Tableau
CREATE VIEW vw_category_revenue AS
SELECT 
    p.product_category_name,
    COUNT(DISTINCT op.order_id) as total_orders,
    SUM(op.payment_value) AS total_revenue
FROM 
    order_payments op
JOIN 
    order_items oi ON op.order_id = oi.order_id
JOIN 
    products p ON oi.product_id = p.product_id
GROUP BY 
    p.product_category_name;

-- View 2: Daily Sales Trend
CREATE VIEW vw_daily_sales AS
SELECT 
    DATE(o.order_purchase_timestamp) AS sale_date,
    SUM(op.payment_value) AS daily_revenue
FROM 
    orders o
JOIN 
    order_payments op ON o.order_id = op.order_id
GROUP BY 
    DATE(o.order_purchase_timestamp);