import pandas as pd
import os
# Test cleaned Olist data for logical errors

dataset_path = r"D:\Info Tech Internship\Olist\Brazilian E-Commerce Public Dataset by Olist"

orders = pd.read_csv(os.path.join(dataset_path, "olist_orders_dataset.csv"))
order_items = pd.read_csv(os.path.join(dataset_path, "olist_order_items_dataset.csv"))
payments = pd.read_csv(os.path.join(dataset_path, "olist_order_payments_dataset.csv"))
reviews = pd.read_csv(os.path.join(dataset_path, "olist_order_reviews_dataset.csv"))

# Convert date columns
orders["order_purchase_timestamp"] = pd.to_datetime(orders["order_purchase_timestamp"], errors="coerce")
orders["order_approved_at"] = pd.to_datetime(orders["order_approved_at"], errors="coerce")
orders["order_delivered_carrier_date"] = pd.to_datetime(orders["order_delivered_carrier_date"], errors="coerce")
orders["order_delivered_customer_date"] = pd.to_datetime(orders["order_delivered_customer_date"], errors="coerce")
orders["order_estimated_delivery_date"] = pd.to_datetime(orders["order_estimated_delivery_date"], errors="coerce")

reviews["review_creation_date"] = pd.to_datetime(reviews["review_creation_date"], errors="coerce")
reviews["review_answer_timestamp"] = pd.to_datetime(reviews["review_answer_timestamp"], errors="coerce")

print("LOGICAL ERROR CHECK REPORT")
print("-" * 50)

# 1. Duplicate order IDs
duplicate_orders = orders["order_id"].duplicated().sum()
print(f"Duplicate order IDs: {duplicate_orders}")

# 2. Approved date before purchase date
approved_before_purchase = (
    orders["order_approved_at"] < orders["order_purchase_timestamp"]
).sum()
print(f"Orders approved before purchase date: {approved_before_purchase}")

# 3. Delivered to carrier before approval
carrier_before_approval = (
    orders["order_delivered_carrier_date"] < orders["order_approved_at"]
).sum()
print(f"Orders delivered to carrier before approval: {carrier_before_approval}")

# 4. Delivered to customer before purchase
customer_delivery_before_purchase = (
    orders["order_delivered_customer_date"] < orders["order_purchase_timestamp"]
).sum()
print(f"Orders delivered to customer before purchase: {customer_delivery_before_purchase}")

# 5. Delivered orders missing customer delivery date
delivered_orders = orders[orders["order_status"] == "delivered"]
missing_delivery_date = delivered_orders["order_delivered_customer_date"].isna().sum()
print(f"Delivered orders missing customer delivery date: {missing_delivery_date}")

# 6. Negative or zero product price
invalid_price = (order_items["price"] <= 0).sum()
print(f"Order items with zero or negative price: {invalid_price}")

# 7. Negative freight value
negative_freight = (order_items["freight_value"] < 0).sum()
print(f"Order items with negative freight value: {negative_freight}")

# 8. Invalid payment value
invalid_payment = (payments["payment_value"] <= 0).sum()
print(f"Payments with zero or negative payment value: {invalid_payment}")

# 9. Invalid payment installments
invalid_installments = (payments["payment_installments"] < 0).sum()
print(f"Payments with negative installments: {invalid_installments}")

# 10. Review score outside 1 to 5
invalid_review_score = (
    (reviews["review_score"] < 1) | (reviews["review_score"] > 5)
).sum()
print(f"Reviews with score outside 1 to 5: {invalid_review_score}")

# 11. Review answer before review creation
answer_before_creation = (
    reviews["review_answer_timestamp"] < reviews["review_creation_date"]
).sum()
print(f"Reviews answered before creation date: {answer_before_creation}")

# 12. Order items without matching order ID
items_without_order = ~order_items["order_id"].isin(orders["order_id"])
print(f"Order items without matching order ID: {items_without_order.sum()}")

# 13. Payments without matching order ID
payments_without_order = ~payments["order_id"].isin(orders["order_id"])
print(f"Payments without matching order ID: {payments_without_order.sum()}")

# 14. Reviews without matching order ID
reviews_without_order = ~reviews["order_id"].isin(orders["order_id"])
print(f"Reviews without matching order ID: {reviews_without_order.sum()}")

print("-" * 50)
print("Logical error check completed successfully.")