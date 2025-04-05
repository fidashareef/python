
# Online Python - IDE, Editor, Compiler, Interpreter
import pandas as pd

# Load the student data
df = pd.read_csv("student.csv")

# 1. Find the average CGPA of the students
average_cgpa = df["CGPA"].mean()
print("1) Average CGPA of Students:", average_cgpa)

# 2. Display the details of all students having CGPA > 9
print("\n2) Students with CGPA > 9:")
print(df[df["CGPA"] > 9])

# 3. Display the details of all CSE students with CGPA > 9
print("\n3) CSE Students with CGPA > 9:")
print(df[(df["Branch"].str.upper() == "CSE") & (df["CGPA"] > 9)])

# 4. Display the details of student with maximum CGPA
print("\n4) Student with Maximum CGPA:")
print(df[df["CGPA"] == df["CGPA"].max()])

# 5. Display average CGPA of each branch
print("\n5) Average CGPA of Each Branch:")
print(df.groupby("Branch")["CGPA"].mean())





