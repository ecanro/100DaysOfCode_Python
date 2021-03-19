from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_create = random.randint(1,5)
        if random_create == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.setheading(180)
            self.all_cars.append(new_car)
            random_y_position = random.randint(-245, 250)
            new_car.goto(300, random_y_position)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def lvl_up(self):
        self.car_speed += MOVE_INCREMENT
