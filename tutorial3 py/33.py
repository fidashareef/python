import tkinter as tk

def calculate_distance():
    try:
        height = float(height_entry.get())
        index = float(index_entry.get())
        bounces = int(bounces_entry.get())

        if not (0 < index < 1):
            result_label.config(text="Bounciness index must be between 0 and 1.")
            return

        total_distance = height
        current_height = height

        for _ in range(bounces):
            current_height *= index
            total_distance += 2 * current_height  # up and down

        result_label.config(text=f"Total distance traveled: {total_distance:.2f} units")

    except ValueError:
        result_label.config(text="Please enter valid numeric inputs.")

# Create GUI window
root = tk.Tk()
root.title("Bouncy Ball Distance Calculator")

# Labels and Entries
tk.Label(root, text="Initial Height:").grid(row=0, column=0, padx=10, pady=5)
height_entry = tk.Entry(root)
height_entry.grid(row=0, column=1, pady=5)

tk.Label(root, text="Bounciness Index (0-1):").grid(row=1, column=0, padx=10, pady=5)
index_entry = tk.Entry(root)
index_entry.grid(row=1, column=1, pady=5)

tk.Label(root, text="Number of Bounces:").grid(row=2, column=0, padx=10, pady=5)
bounces_entry = tk.Entry(root)
bounces_entry.grid(row=2, column=1, pady=5)

# Calculate button
calc_button = tk.Button(root, text="Calculate", command=calculate_distance)
calc_button.grid(row=3, column=0, columnspan=2, pady=10)

# Result label
result_label = tk.Label(root, text="", fg="blue")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Run the GUI loop
root.mainloop()

