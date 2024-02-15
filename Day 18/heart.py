import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.setup(width=600, height=600)

t.speed(2)
t.color('red')
t.fillcolor('red')
t.begin_fill()

t.left(140)
t.forward(180)
t.circle(-90, 200)
t.setheading(60)
t.circle(-90, 200)
t.forward(180)
t.end_fill()

t.hideturtle()
turtle.done()
