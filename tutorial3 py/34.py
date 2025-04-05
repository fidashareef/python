import tkinter as tk
import random

# Generate the secret number
secret_number = random.randint(1, 100)
guess_count = 0

# Function to check the user's guess
def check_guess():
    global guess_count
    try:
        guess = int(guess_entry.get())
        guess_count += 1
        if guess < secret_number:
            feedback_label.config(text="Too small, try again.")
        elif guess > secret_number:
            feedback_label.config(text="Too large, try again.")
        else:
            feedback_label.config(
                text=f"Congratulations! You guessed it in {guess_count} tries!"
            )
            guess_button.config(state=tk.DISABLED)
    except ValueError:
        feedback_label.config(text="Please enter a valid number.")

# Reset game (optional feature)
def reset_game():
    global secret_number, guess_count
    secret_number = random.randint(1, 100)
    guess_count = 0
    feedback_label.config(text="")
    guess_entry.delete(0, tk.END)
    guess_button.config(state=tk.NORMAL)

# GUI setup
root = tk.Tk()
root.title("Guess the Number Game")

# Widgets
tk.Label(root, text="Guess a number between 1 and 100:").pack(pady=10)

guess_entry = tk.Entry(root)
guess_entry.pack()

guess_button = tk.Button(root, text="Guess", command=check_guess)
guess_button.pack(pady=5)

feedback_label = tk.Label(root, text="")
feedback_label.pack(pady=10)

reset_button = tk.Button(root, text="Play Again", command=reset_game)
reset_button.pack()

# Run the GUI event loop
root.mainloop()
