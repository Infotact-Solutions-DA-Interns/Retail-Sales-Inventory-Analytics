# Data Accuracy Audit Report

## Objective
Verify that the data imported into the SQL database matches the raw CSV files cleaned in Python.

## Test 1: Total Revenue Match
* **Python Result:** (From `master_df['payment_value'].sum()`)
* **SQL Result:** (From `SELECT SUM(payment_value) FROM order_payments;`)
* **Status:** PASS / FAIL 
*(Note for team: If these numbers do not match exactly, Kasak needs to re-import the payments dataset).*

## Test 2: Order Count Match
* **Python Result:** 99,441 unique orders
* **SQL Result:** (Run `SELECT COUNT(DISTINCT order_id) FROM orders;`)
* **Status:** Pending Team Verification