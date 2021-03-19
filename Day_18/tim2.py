import turtle as t
import random
tim = t.Turtle()


directions = [0, 90, 180, 270]
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
tim.pensize(8)
tim.speed(8)
for n in range(200):
    tim.color(random.choice(colours))
    #tim.pensize(n+0.01)
    tim.forward(20)
    tim.setheading(random.choice(directions))



