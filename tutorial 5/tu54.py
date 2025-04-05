
# Online Python - IDE, Editor, Compiler, Interpreter
import pandas as pd

# Load the employee CSV file
df = pd.read_csv("employee.csv")

# 1. Print first 7 records from employees file
print("1) First 7 Records:")
print(df.head(7))

# 2. Print all employee names in alphabetical order
print("\n2) Employee Names in Alphabetical Order:")
print(df["name"].sort_values().reset_index(drop=True))

# 3. Find the name of the employee with highest salary
highest_paid = df.loc[df["salary"].idxmax(), "name"]
print("\n3) Employee with Highest Salary:", highest_paid)

# 4. List the names of male employees
print("\n4) Male Employees:")
print(df[df["gender"].str.lower() == "male"]["name"])

# 5. Display all unique teams employees belong to
print("\n5) Teams Employees Belong To:")
print(df["team"].unique())





