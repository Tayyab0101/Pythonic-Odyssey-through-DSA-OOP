from turtle import Turtle, Screen

t = Turtle()
s = Screen()


def up():
    t.setheading(90)
def down():
    t.setheading(270)
def left():
    t.setheading(180)
def right():
    t.setheading(0)
def move():
    t.forward(20)
    
def move_forward():
    t.forward(10)
def move_backward():
    t.back(10)
def move_left():
    t.setheading(t.heading()+20)
    t.forward(10)
def move_right():
    t.setheading(t.heading()-20)
    t.forward(10)

def clear_screen():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

s.listen() # also s.listen() is same
s.onkey(up, "w") # simmilarly t.onkey() is also same
s.onkey(down, "s")
s.onkey(left, "a")
s.onkey(right, "d")

s.onkey(move_forward, "Up")
s.onkey(move_backward, "Down")
s.onkey(move_left, "Left")
s.onkey(move_right, "Right")

s.onkey(clear_screen, "BackSpace")
s.onkey(move, "space")

s.exitonclick()