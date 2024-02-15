import turtle

# Setup
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("lightpink")

# Create a turtle
rose = turtle.Turtle()
rose.speed(10)
rose.color("red")

# Draw the stem
rose.penup()
rose.goto(0, -200)
rose.pendown()
rose.left(90)
rose.forward(300)

# Draw the petals
for _ in range(36):
    rose.circle(50, 70)
    rose.left(110)
    rose.circle(50, 70)
    rose.left(110)

# Draw the center of the rose
rose.color("yellow")
rose.begin_fill()
rose.circle(20)
rose.end_fill()

# Hide the turtle
rose.hideturtle()

# Keep the window open
screen.mainloop()
