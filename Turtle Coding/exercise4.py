from turtle import *
import random

getscreen()
speed(3)
width(15)
shape("turtle")
colors = ["red", "green", "purple", "black", "yellow", "blue", "brown", "cyan", "chocolate1"]
directions = [forward(50), back(90), left(90), right(90)]

for i in range(50):
    setheading(random.randrange(0, 360, 90)) # 0 90 180 270
    pencolor(random.choice(colors))
    forward(30)

hideturtle()
exitonclick()
