# TODO 1: Create snake Body
# TODO 2: Move the snake
# TODO 3: Control the snake

from turtle import Turtle, Screen
from snake import Snake
from food import Food
#from scoreboard import scoreboard
import time

screen = Screen()
screen.setup(width=640, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()






screen.exitonclick()