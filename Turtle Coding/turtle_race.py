import random
from turtle import Screen, Turtle

def no_of_turtles():
    count = 0 # initializing is a good prac, otherwise doesn't affect
    while True:
        count = int(input("How many turtles you want to run(2-9): "))
        if 2<=count<=9:
            return count
        else:
            print("Invalid Input. Enter again")

turtles = no_of_turtles() # storing the return int in variable(turtles)

s1 = Screen()
s1.setup(420, 420)
WIDTH, HEIGHT = 400, 400
color_list = ["red", "green", "purple", "black", "yellow", "blue", "brown", "cyan", "chocolate1"]

divide_base = WIDTH// (turtles+1) # for count = 3 ---> 400//4 = 100

turtle_list = []
for i in range(1, turtles+1):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.left(90)
    new_turtle.penup()
    new_turtle.color(color_list[i-1])
    new_turtle.goto(-WIDTH//2 + (i * divide_base) ,-180) #Screen: -200 bottom, +200 up, +200 right, -200 left
    turtle_list.append(new_turtle)
    
def race():
    is_race_on = True
    while is_race_on:
        for t in turtle_list:
            distance = random.randint(1, 10)
            t.forward(distance)
            if t.ycor() >= 180:  
                winner_color = t.fillcolor()  # Get the winner's color
                winner_message = f"The winner is {winner_color} turtle"  # Create the winner's message
                t.goto(0,0)
                t.write(winner_message, align="center", font=("Arial", 16, "bold"))  # Write msg on the screen
                is_race_on = False

race() 
s1.exitonclick()