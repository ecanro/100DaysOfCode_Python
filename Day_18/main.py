"""TODO 1:Import the turtle module and screen module"""
"""We have some ways to import a module:
1-> import turtle
    tim = turtle.Turtle()
2-> from turtle import *
    color("red")
and we will use:
from module_name import module_class--->
"""
#aliasing-> import module_name as alias_name(maybe when the module name is too long)


from turtle import Turtle, Screen

"""using the module"""
tim = Turtle()
tim.shape("turtle")
tim.color("dark sea green")
tim.pencolor("blue")

# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.speed(1)
"""drawing a box"""
# for n in range(10):
#     tim.forward(15)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
tim.color('red', 'yellow')
tim.begin_fill()
while True:
    tim.forward(200)
    tim.left(170)
    if abs(tim.pos()) < 1:
        break
tim.end_fill()
tim.done()


tim.speed(1)
#
# """using the screen module for display the turtle"""
# screen = Screen()
# screen.exitonclick()


"""some modules is not are by default in the python library, we need install"""
#import heroes->dont work, but pycharm can install click in the bubble
