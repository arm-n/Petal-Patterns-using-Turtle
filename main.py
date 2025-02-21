import turtle

# Set up the screen and turtle
tom = turtle.Turtle()
screen = turtle.Screen()
screen.screensize(canvwidth=400, canvheight=400)
screen.bgcolor("black")

tom.speed(0)
tom.hideturtle()
screen.tracer(0, 0)  # Speed up rendering


# Define bright colors to highlight against black background
Colors = [
    "white", "yellow", "cyan", "lime", "magenta", "orange", "pink", "turquoise", "violet"
]

# Number of iterations
x = 100

for i in range(x):
    for col in Colors:
        tom.color(col)  # Set pen color
        tom.circle(200 - i, 100)  # Draw arc
        tom.left(90)  # Turn left
        tom.circle(200 - i, 100)  # Draw arc
        tom.right(60)  # Turn right
        screen.update()  # Refresh screen after each step

screen.exitonclick()  # Wait for user to click to exit
