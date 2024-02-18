from turtle import Turtle
import random
color_list = ["blue", "yellow","red","orange"]
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        random_color = random.choice(color_list)
        self.color(random_color)
        self.goto(random_x, random_y)  
        self.showturtle()