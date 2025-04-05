
# Online Python - IDE, Editor, Compiler, Interpreter

import pandas as pd

# 1) Load, Clean and Update the CSV file
df = pd.read_csv("auto.csv")

# Optional: Display the first few rows to understand the structure
print("Original Data:")
print(df.head())

# Clean: Remove duplicates, handle missing values (you can adjust how)
df.drop_duplicates(inplace=True)
df.dropna(subset=["price", "company"], inplace=True)

# Convert price and average-mileage to numeric if they're not
df["price"] = pd.to_numeric(df["price"], errors='coerce')
df["average-mileage"] = pd.to_numeric(df["average-mileage"], errors='coerce')

# Drop rows again if numeric conversion created NaNs
df.dropna(subset=["price", "average-mileage"], inplace=True)

# 2) Find the most expensive car company name
most_expensive_company = df.loc[df["price"].idxmax(), "company"]
print(f"\n2) Most expensive car company: {most_expensive_company}")

# 3) Print all Toyota car details
print("\n3) All Toyota car details:")
print(df[df["company"].str.lower() == "toyota"])

# 4) Print total cars of all companies
print("\n4) Total number of cars by company:")
print(df["company"].value_counts())

# 5) Find the highest priced car of all companies
print("\n5) Highest priced car(s) by each company:")
print(df.loc[df.groupby("company")["price"].idxmax()])

# 6) Find the average mileage of all companies
print("\n6) Average mileage of all companies:")
print(df.groupby("company")["average-mileage"].mean())

# 7) Sort all cars by Price column
sorted_cars = df.sort_values(by="price", ascending=False)
print("\n7) All cars sorted by price (descending):")
print(sorted_cars)

# Optional: Save cleaned file
df.to_csv("auto_cleaned.csv", index=False)

