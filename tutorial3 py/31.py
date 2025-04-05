
# Online Python - IDE, Editor, Compiler, Interpreter

import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle
star = turtle.Turtle()
star.color("blue")
star.pensize(2)
star.speed(3)

# Draw a 5-pointed star
for _ in range(5):
    star.forward(100)       # Move forward
    star.right(144)         # Turn right by 144 degrees

# Hide the turtle and keep the window open
star.hideturtle()
turtle.done()
