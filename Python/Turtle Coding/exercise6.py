import random
from turtle import Turtle as t

t.title("Dot Painting")
t.setup(600, 600)
colors = ["red", "green", "purple", "black", "yellow", "blue", "brown", "cyan", "chocolate1"]

for i in range(100):
    t.penup()
    t.goto(random.randint(-100,100), random.randint(-100,100))
    t.pencolor(random.choice(colors))
    t.dot(20)
    t.pendown()
    

t.exitonclick()