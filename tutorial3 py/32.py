
# Online Python - IDE, Editor, Compiler, Interpreter
import tkinter as tk

def fahrenheit_to_celsius():
    try:
        f = float(fahrenheit_entry.get())
        c = (f - 32) * 5 / 9
        celsius_entry.delete(0, tk.END)
        celsius_entry.insert(0, f"{c:.2f}")
    except ValueError:
        celsius_entry.delete(0, tk.END)
        celsius_entry.insert(0, "Invalid input")

def celsius_to_fahrenheit():
    try:
        c = float(celsius_entry.get())
        f = (c * 9 / 5) + 32
        fahrenheit_entry.delete(0, tk.END)
        fahrenheit_entry.insert(0, f"{f:.2f}")
    except ValueError:
        fahrenheit_entry.delete(0, tk.END)
        fahrenheit_entry.insert(0, "Invalid input")

# Set up the main window
root = tk.Tk()
root.title("Temperature Converter")

# First row: labels
tk.Label(root, text="Fahrenheit").grid(row=0, column=0, padx=10, pady=5)
tk.Label(root, text="Celsius").grid(row=0, column=1, padx=10, pady=5)

# Second row: entry fields
fahrenheit_entry = tk.Entry(root)
fahrenheit_entry.grid(row=1, column=0, padx=10, pady=5)
fahrenheit_entry.insert(0, "32")

celsius_entry = tk.Entry(root)
celsius_entry.grid(row=1, column=1, padx=10, pady=5)
celsius_entry.insert(0, "0.0")

# Third

