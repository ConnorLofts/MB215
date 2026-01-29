# Activity 7
# Import Turtle graphics library
import turtle

# Set up your drawing parameters
ITERATIONS = 10 # The number of times to repeat the pattern
ANGLE = 36 # The angle to turn after each shape is drawn
SIZE = 100 # The size parameter for the shapes

# Set up the Turtle screen and turtle
screen = turtle.Screen()
pattern_turtle = turtle.Turtle()
# Loop to draw the pattern
for i in range(ITERATIONS):
    # Draw your geometric shape here
    # E.g., to draw a square:
    for _ in range(4):
        pattern_turtle.forward(SIZE)
        pattern_turtle.right(90)  # Right angle for a square

    # Rotate the turtle to prepare for the next shape
    pattern_turtle.right(ANGLE)

# Complete the program with a command to keep the window open
turtle.done()
