# import module
# # import turtle
# print(module.module_var)
#
# from turtle import Turtle, Screen
# # yo = turtle.Turtle()
# some = Turtle()
# print(some)
# some.shape("turtle")
# some.color("red")
# some.speed(1)
#
# some.forward(100)
#
# my_screen = Screen()
# #using dot notation
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Pokemon Name", ["Pickach", "Squirtle", "Charmender"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)

