import pandas as pd
import os

# Analyst 3 Work - 14 May 2026
# Task: Validate data types across columns in the Olist dataset

dataset_path = r"D:\Info Tech Internship\Olist\Brazilian E-Commerce Public Dataset by Olist"

orders = pd.read_csv(os.path.join(dataset_path, "olist_orders_dataset.csv"))
customers = pd.read_csv(os.path.join(dataset_path, "olist_customers_dataset.csv"))
order_items = pd.read_csv(os.path.join(dataset_path, "olist_order_items_dataset.csv"))
payments = pd.read_csv(os.path.join(dataset_path, "olist_order_payments_dataset.csv"))
reviews = pd.read_csv(os.path.join(dataset_path, "olist_order_reviews_dataset.csv"))
products = pd.read_csv(os.path.join(dataset_path, "olist_products_dataset.csv"))
sellers = pd.read_csv(os.path.join(dataset_path, "olist_sellers_dataset.csv"))

print("DATA TYPE VALIDATION REPORT")
print("-" * 50)

datasets = {
    "Orders": orders,
    "Customers": customers,
    "Order Items": order_items,
    "Payments": payments,
    "Reviews": reviews,
    "Products": products,
    "Sellers": sellers
}

# Display original data types
print("\nORIGINAL DATA TYPES")
print("-" * 50)

for name, df in datasets.items():
    print(f"\n{name} Dataset:")
    print(df.dtypes)

# Convert date columns into datetime format
orders["order_purchase_timestamp"] = pd.to_datetime(orders["order_purchase_timestamp"], errors="coerce")
orders["order_approved_at"] = pd.to_datetime(orders["order_approved_at"], errors="coerce")
orders["order_delivered_carrier_date"] = pd.to_datetime(orders["order_delivered_carrier_date"], errors="coerce")
orders["order_delivered_customer_date"] = pd.to_datetime(orders["order_delivered_customer_date"], errors="coerce")
orders["order_estimated_delivery_date"] = pd.to_datetime(orders["order_estimated_delivery_date"], errors="coerce")

order_items["shipping_limit_date"] = pd.to_datetime(order_items["shipping_limit_date"], errors="coerce")

reviews["review_creation_date"] = pd.to_datetime(reviews["review_creation_date"], errors="coerce")
reviews["review_answer_timestamp"] = pd.to_datetime(reviews["review_answer_timestamp"], errors="coerce")

# Validate numeric columns
numeric_columns = {
    "Order Items": ["order_item_id", "price", "freight_value"],
    "Payments": ["payment_sequential", "payment_installments", "payment_value"],
    "Reviews": ["review_score"],
    "Products": [
        "product_name_lenght",
        "product_description_lenght",
        "product_photos_qty",
        "product_weight_g",
        "product_length_cm",
        "product_height_cm",
        "product_width_cm"
    ]
}

print("\nNUMERIC COLUMN VALIDATION")
print("-" * 50)

for dataset_name, columns in numeric_columns.items():
    df = datasets[dataset_name]

    for column in columns:
        if column in df.columns:
            converted_column = pd.to_numeric(df[column], errors="coerce")
            invalid_count = converted_column.isna().sum() - df[column].isna().sum()

            print(f"{dataset_name} - {column}: {invalid_count} invalid numeric values")

# Validate date columns
date_columns = {
    "Orders": [
        "order_purchase_timestamp",
        "order_approved_at",
        "order_delivered_carrier_date",
        "order_delivered_customer_date",
        "order_estimated_delivery_date"
    ],
    "Order Items": ["shipping_limit_date"],
    "Reviews": ["review_creation_date", "review_answer_timestamp"]
}

print("\nDATE COLUMN VALIDATION")
print("-" * 50)

for dataset_name, columns in date_columns.items():
    df = datasets[dataset_name]

    for column in columns:
        if column in df.columns:
            null_or_invalid_dates = df[column].isna().sum()
            print(f"{dataset_name} - {column}: {null_or_invalid_dates} null/invalid date values")

# Show updated data types after conversion
print("\nUPDATED DATA TYPES AFTER CONVERSION")
print("-" * 50)

print("\nOrders Dataset:")
print(orders.dtypes)

print("\nOrder Items Dataset:")
print(order_items.dtypes)

print("\nReviews Dataset:")
print(reviews.dtypes)

print("\nData type validation completed successfully.")