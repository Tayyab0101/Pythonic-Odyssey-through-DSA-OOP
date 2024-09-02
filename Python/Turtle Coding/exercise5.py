from turtle import *
import random

speed(10)
color("red", "yellow")

begin_fill()
while True:
    forward(200)
    left(170)
    if distance(0, 0) < 1:  # or heading()=0
        break   
end_fill()

exitonclick()