
# Online Python - IDE, Editor, Compiler, Interpreter
import pandas as pd
import matplotlib.pyplot as plt

sales_df = pd.read_csv("sales.csv")

# 1) Toothpaste sales data using scatter plot
plt.figure(figsize=(8, 5))
plt.scatter(sales_df["month_number"], sales_df["toothpaste"], color='blue', label='Toothpaste Sales')
plt.title("Monthly Toothpaste Sales")
plt.xlabel("Month")
plt.ylabel("Units Sold")
plt.grid(True)
plt.legend()
plt.show()

# 2) Face cream and face wash sales using bar chart
plt.figure(figsize=(10, 6))
bar_width = 0.35
index = sales_df["month_number"]

plt.bar(index - 0.15, sales_df["facecream"], bar_width, label='Face Cream', color='orange')
plt.bar(index + 0.15, sales_df["facewash"], bar_width, label='Face Wash', color='green')

plt.xlabel("Month")
plt.ylabel("Sales Units")
plt.title("Face Cream & Face Wash Monthly Sales")
plt.xticks(index)
plt.legend()
plt.grid(True)
plt.show()

# 3) Total yearly sale for each product using pie chart
product_cols = ["facecream", "facewash", "toothpaste", "bathingsoap", "shampoo", "moisturizer"]
total_sales = sales_df[product_cols].sum()

plt.figure(figsize=(8, 8))
plt.pie(total_sales, labels=product_cols, autopct='%1.1f%%', startangle=140)
plt.title("Total Yearly Sales by Product")
plt.axis('equal')  # Equal aspect ratio ensures pie is drawn as a circle.
plt.show()




