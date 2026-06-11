import pandas as pd
import os

dataset_path = r"D:\Info Tech Internship\Olist\Brazilian E-Commerce Public Dataset by Olist"
cleaned_path = r"D:\Info Tech Internship\Olist\Cleaned"

orders      = pd.read_csv(os.path.join(cleaned_path, "orders_cleaned.csv"))
order_items = pd.read_csv(os.path.join(cleaned_path, "order_items_cleaned.csv"))
payments    = pd.read_csv(os.path.join(dataset_path, "olist_order_payments_dataset.csv"))
customers   = pd.read_csv(os.path.join(dataset_path, "olist_customers_dataset.csv"))
products    = pd.read_csv(os.path.join(dataset_path, "olist_products_dataset.csv"))
category_translation = pd.read_csv(os.path.join(dataset_path, "product_category_name_translation.csv"))

print("BEST-SELLING PRODUCTS & GEOGRAPHIC TRENDS REPORT")
print("-" * 50)

# Merge order_items with products and category translation
items_products = order_items.merge(
    products[["product_id", "product_category_name"]], on="product_id", how="left"
)
items_products = items_products.merge(
    category_translation, on="product_category_name", how="left"
)

# Best-Selling Categories by Order Volume
print("\nBEST-SELLING PRODUCT CATEGORIES - By Order Volume")
best_by_volume = (
    items_products.groupby("product_category_name_english")["order_id"]
    .count()
    .reset_index()
    .rename(columns={"order_id": "total_orders"})
    .sort_values("total_orders", ascending=False)
)
print(best_by_volume.head(10).to_string(index=False))

# Best-Selling Categories by Revenue
print("\nBEST-SELLING PRODUCT CATEGORIES - By Revenue")
best_by_revenue = (
    items_products.groupby("product_category_name_english")["price"]
    .sum()
    .reset_index()
    .rename(columns={"price": "total_revenue"})
    .sort_values("total_revenue", ascending=False)
)
print(best_by_revenue.head(10).to_string(index=False))

# Geographic Trends - Orders per City
print("\nGEOGRAPHIC TRENDS - Top Cities by Order Volume")
orders_customers = orders.merge(
    customers[["customer_id", "customer_city", "customer_state"]], on="customer_id", how="left"
)
city_orders = (
    orders_customers.groupby(["customer_city", "customer_state"])["order_id"]
    .count()
    .reset_index()
    .rename(columns={"order_id": "total_orders"})
    .sort_values("total_orders", ascending=False)
)
print(city_orders.head(10).to_string(index=False))

# Geographic Trends - Revenue per State
print("\nGEOGRAPHIC TRENDS - Top States by Revenue")
orders_payments = orders.merge(
    payments[["order_id", "payment_value"]], on="order_id", how="left"
)
orders_payments_customers = orders_payments.merge(
    customers[["customer_id", "customer_state"]], on="customer_id", how="left"
)
state_revenue = (
    orders_payments_customers.groupby("customer_state")["payment_value"]
    .sum()
    .reset_index()
    .rename(columns={"payment_value": "total_revenue"})
    .sort_values("total_revenue", ascending=False)
)
print(state_revenue.head(10).to_string(index=False))

# Export
output_path = r"D:\Info Tech Internship\Olist\Cleaned"
best_by_volume.to_csv(os.path.join(output_path, "best_selling_by_volume.csv"), index=False)
best_by_revenue.to_csv(os.path.join(output_path, "best_selling_by_revenue.csv"), index=False)
city_orders.to_csv(os.path.join(output_path, "geographic_city_orders.csv"), index=False)
state_revenue.to_csv(os.path.join(output_path, "geographic_state_revenue.csv"), index=False)

print("\nbest_selling_by_volume.csv saved")
print("best_selling_by_revenue.csv saved")
print("geographic_city_orders.csv saved")
print("geographic_state_revenue.csv saved")
print("-" * 50)
print("Completed successfully.")