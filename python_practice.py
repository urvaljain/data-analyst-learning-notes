# python_practice.py
# Practice file for learning data analysis with pandas
# Using sales_dataset.csv

import pandas as pd

# Example 1 Load dataset
df = pd.read_csv("sales_dataset.csv")

# Example 2 Show first rows
print("First 5 rows:")
print(df.head())

# Example 3 Show column names
print("\nColumn names:")
print(df.columns)

# Example 4 Total sales amount
total_sales = df["amount"].sum()
print("\nTotal Sales Amount:", total_sales)

# Example 5 Sales by city using groupby
sales_by_city = df.groupby("city")["amount"].sum()
print("\nSales by City:")
print(sales_by_city)

# Example 6 Sales by product using groupby
sales_by_product = df.groupby("product")["amount"].sum()
print("\nSales by Product:")
print(sales_by_product)

# Example 7 Average amount
average_amount = df["amount"].mean()
print("\nAverage Order Amount:", average_amount)

# Example 8 Highest order
highest_order = df["amount"].max()
print("\nHighest Order Amount:", highest_order)

# Example 9 Filter rows where city is Indore
indore_sales = df[df["city"] == "Indore"]
print("\nSales in Indore:")
print(indore_sales)

# Example 10 Count total orders
total_orders = df["order_id"].count()
print("\nTotal Orders:", total_orders)
