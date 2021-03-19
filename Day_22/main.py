"""Ping pong arcade game"""
# TODO 1: Create the screen
# TODO 2: Create a move paddle player1
# TODO 3: Create another paddle player 2
# Todo 4: Create the ball and make move it
# Todo 5: Detect collision with the wall and bounce
# Todo 6: Detect collision with paddle
# Todo 7: Detect when paddle misses
# Todo 8: Keep Score

from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Arcade Pong Game")
screen.tracer(0)


paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))


scoreboard = Scoreboard()
# score_player_r = Scoreboard((180, 270))
# score_player_l = Scoreboard((-180, 270))

ball = Ball()

screen.listen()
screen.onkeypress(paddle_r.move_up, "Up")
screen.onkeypress(paddle_r.move_down, "Down")

screen.onkeypress(paddle_l.move_up, "w")
screen.onkeypress(paddle_l.move_down, "s")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move_ball()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # need to bounce
        ball.bounce_y()

    # detect collision with paddle
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        # print("the ball bounce in paddle")
        ball.bounce_x()

    # detect when paddle misses
    # we need every one
    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.l_point()
    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
