# TODO 1: Move the turtle with keypress
# TODO 2: Create and move the cars
# TODO 3: Detect Collision with cars
# TODO 4: Detect when turtle reached the other side
# TODO 5: Create a Scoreboard

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing game")
screen.tracer(0)

scoreboard = Scoreboard()
player = Player()
cars = CarManager()

screen.onkeypress(player.go_up, "Up")


screen.listen()
time.sleep(0.1)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    cars.create_car()
    cars.move_cars()

    # detecting if turtle finish
    if player.is_at_finish_lane():
        scoreboard.level_up()
        player.go_to_start()

    # detecting when it is rolled
    for car in cars.all_cars:
        if car.distance(player) < 15:
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()