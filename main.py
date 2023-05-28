import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "green", "blue", "orange", "yellow", "purple"]
user_bet = screen.textinput(title="Welcome to Ninja Turtle Race!",
                            prompt=f"Which turtle will win the race? Enter a color: \n{colors}")
all_turtles = []
is_race_on = False
y = 90
for each_turtle_color in colors:
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.speed(1)
    turtle.color(each_turtle_color)
    turtle.goto(x=-240, y=y)
    y -= 30
    all_turtles.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 220:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! The {winning_color} turtle is the winner!")
            else:
                print(f"You have lost! The {winning_color} turtle is the winner!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
