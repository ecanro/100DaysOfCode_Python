# TODO: Higher order functions and event listeners, objects states and instances

import turtle as t
#from turtle import Turtle, Screen
import random

tim = t.Turtle()
tim.shape("turtle")
tim.color("red")

screen = t.Screen()


def move_forwards():
    tim.forward(10)


screen.listen()
screen.onkey(fun=move_forwards, key="space")#->higher order function

screen.exitonclick()


