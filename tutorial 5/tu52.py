
# Online Python - IDE, Editor, Compiler, Interpreter
import pandas as pd
import matplotlib.pyplot as plt

# a) Read and display the file contents
df = pd.read_csv("stud.csv")
print("a) File Contents:\n", df)

# b) Set rollno as index
df.set_index("rollno", inplace=True)
print("\nb) Set rollno as index:\n", df)

# c) Display name and mark
print("\nc) Name and Mark:\n", df[["name", "mark"]])

# d) rollno, Name and mark in the order of name
print("\nd) Sorted by Name:\n", df.sort_values(by="name")[["name", "mark"]])

# e) Display rollno, name, mark in descending order of mark
print("\ne) Sorted by Mark (Descending):\n", df.sort_values(by="mark", ascending=False)[["name", "mark"]])

# f) Find the average mark, median and mode
print("\nf) Statistics:")
print("Average mark:", df["mark"].mean())
print("Median mark:", df["mark"].median())
print("Mode mark:", df["mark"].mode().values)

# g) Find minimum and maximum marks
print("\ng) Min and Max Marks:")
print("Minimum:", df["mark"].min())
print("Maximum:", df["mark"].max())

# h) Variance and standard deviation
print("\nh) Variance and Std Deviation:")
print("Variance:", df["mark"].var())
print("Standard Deviation:", df["mark"].std())

# i) Display histogram of marks
plt.figure(figsize=(8, 5))
plt.hist(df["mark"], bins=5, color='skyblue', edgecolor='black')
plt.title("Histogram of Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.grid(True)
plt.show()

# j) Remove the place column
df.drop("place", axis=1, inplace=True)
print("\nj) After removing 'place' column:\n", df)



