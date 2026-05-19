-- Calculate Total Revenue and Average Order Value
SELECT 
    COUNT(DISTINCT order_id) AS total_orders,
    SUM(payment_value) AS total_revenue,
    SUM(payment_value) / COUNT(DISTINCT order_id) AS average_order_value
FROM 
    order_payments;
    