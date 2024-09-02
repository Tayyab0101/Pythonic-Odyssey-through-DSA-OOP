from turtle import *
import random

getscreen()

colour = ["red", "green", "purple", "black", "yellow", "blue", "brown", "cyan", "chocolate1"]

for i in range(3, 9):
    angle = 360/ i
    pencolor(random.choice(colour))
    for j in range(i):
        forward(100)
        right(angle)

hideturtle()
exitonclick()
