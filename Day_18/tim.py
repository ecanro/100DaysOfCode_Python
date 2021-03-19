from turtle import Turtle, Screen
import random
"""create a turtle that drawing diferente shapes geometrics"""
tim = Turtle()
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


def draw_shapes(num_sides):
    angle = 360 / num_sides
    for n in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for shape_side_n in range(3, 12):
    tim.color(random.choice(colours))
    draw_shapes(shape_side_n)


# screen = Screen()
# screen.exitonclick()