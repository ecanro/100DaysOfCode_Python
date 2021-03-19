import turtle as t
import random

"""in this exercise we generated a random color(r,g,b) for the lines shape by tim
    using tuples
"""
tim = t.Turtle()
t.colormode(255)#->call the module and reseting the color mode
directions = [0, 90, 180, 270]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b) #->tuple colors rgb
    return random_color
"""
the tuples are inmutables, so if we need alter we can transform in a list
list(tupla)
"""
tim.pensize(8)
tim.speed(8)
for n in range(200):
    tim.color(random_color())
    #tim.pensize(n+0.01)
    tim.forward(20)
    tim.setheading(random.choice(directions))