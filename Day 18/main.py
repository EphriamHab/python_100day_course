from turtle import Turtle, Screen
import random

tim = Turtle()

for _ in range(4):
    tim.forward(100)
    tim.left(90)

for _ in range(8):
    tim.forward(10)
    tim.color("white")
    tim.forward(10)
    tim.color("black")

for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color_hex = "#{:02x}{:02x}{:02x}".format(r, g, b)
    return color_hex
    


directions = [0, 90, 180, 270]
tim.pensize(5)
tim.speed("fastest")

def draw_shape(num_sides):
    angle = 360/ num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for shape_side_n in range(3,10):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)
    
for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + 10)

draw_spirograph(5)

    
screen = Screen()
screen.exitonclick()