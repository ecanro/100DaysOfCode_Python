from turtle import Turtle, Screen
import random

# TODO: a turtle race

#Screen configuration
screen = Screen()
screen.setup(width=680, height=680)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

#random colors for every turtle
colors = ["red", "orange", "blue", "purple", "green", "brown"]
#the start position for every tim
y_positions = [-250, -150, -50, 50, 150, 250 ]
#race is on
race_on = False
#names of turtles
all_turtles = []

#configure the turtl\es
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-330, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    race_on = True

while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 310:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        #move each turtle a random amount
        random_forward = random.randint(0, 10)
        turtle.forward(random_forward)

screen.exitonclick()