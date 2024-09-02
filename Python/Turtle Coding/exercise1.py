from turtle import *

getscreen()  # Using this or not doesn't affect as it is auto called when u call a screen method...
penup()
back(180)
pendown()

def basics():
    shape("turtle")
    speed(3)
    color("green", "pink") # Pen followed by fill color
    bgcolor("Black")
    
def octagon():   
    for i in range(8):
        left(45)
        forward(50)
        
        
basics()
circle(70)
penup()
forward(350)
pendown()
octagon()

exitonclick()