import pandas as pd
import os

dataset_path = r"D:\Info Tech Internship\Olist\Brazilian E-Commerce Public Dataset by Olist"

orders      = pd.read_csv(os.path.join(dataset_path, "olist_orders_dataset.csv"))
order_items = pd.read_csv(os.path.join(dataset_path, "olist_order_items_dataset.csv"))

# Convert date columns
date_cols = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]
for col in date_cols:
    orders[col] = pd.to_datetime(orders[col], errors="coerce")

order_items["shipping_limit_date"] = pd.to_datetime(
    order_items["shipping_limit_date"], errors="coerce"
)

print("NULL HANDLING & DUPLICATE REMOVAL REPORT")
print("-" * 50)

# Before cleaning
print(f"\nOrders shape before      : {orders.shape}")
print(f"Order Items shape before : {order_items.shape}")

# Orders NULL handling
approved_nulls = orders["order_approved_at"].isnull().sum()
carrier_nulls  = orders["order_delivered_carrier_date"].isnull().sum()
customer_nulls = orders["order_delivered_customer_date"].isnull().sum()

print(f"\norder_approved_at             : {approved_nulls} NULLs kept")
print(f"order_delivered_carrier_date  : {carrier_nulls} NULLs kept")
print(f"order_delivered_customer_date : {customer_nulls} NULLs kept")

before = len(orders)
orders.dropna(subset=["order_status"], inplace=True)
print(f"order_status                  : {before - len(orders)} rows dropped")

# Order Items NULL handling
before = len(order_items)
order_items.dropna(subset=["price"], inplace=True)
print(f"\nprice          : {before - len(order_items)} rows dropped")

freight_nulls = order_items["freight_value"].isnull().sum()
order_items["freight_value"] = order_items["freight_value"].fillna(0.0)
print(f"freight_value  : {freight_nulls} NULLs filled with 0.0")

before = len(order_items)
order_items.dropna(subset=["seller_id", "product_id"], inplace=True)
print(f"seller_id / product_id : {before - len(order_items)} rows dropped")

# Duplicate removal
orders_dup = orders.duplicated(subset=["order_id"]).sum()
orders.drop_duplicates(subset=["order_id"], keep="first", inplace=True)
print(f"\nOrders duplicate rows removed      : {orders_dup}")

items_dup = order_items.duplicated(subset=["order_id", "order_item_id"]).sum()
order_items.drop_duplicates(subset=["order_id", "order_item_id"], keep="first", inplace=True)
print(f"Order Items duplicate rows removed : {items_dup}")

# After cleaning
print(f"\nOrders shape after      : {orders.shape}")
print(f"Order Items shape after : {order_items.shape}")

# Export
output_path = r"D:\Info Tech Internship\Olist\Cleaned"
os.makedirs(output_path, exist_ok=True)
orders.to_csv(os.path.join(output_path, "orders_cleaned.csv"), index=False)
order_items.to_csv(os.path.join(output_path, "order_items_cleaned.csv"), index=False)

print("\norders_cleaned.csv saved")
print("order_items_cleaned.csv saved")
print("-" * 50)
print("Completed successfully.")