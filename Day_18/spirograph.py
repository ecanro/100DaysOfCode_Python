import turtle as t
import random

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b) #->tuple colors rgb
    return color


tim = t.Turtle()
t.colormode(255)#->call the module and reseting the color mode

tim.pensize(1)
tim.speed("fastest")

#solution one(360 degrees/5 ->timmove right = 72 circles, but i need calculate this before run)
for n in range(72):
    tim.color(random_color())
    #tim.pensize(n+0.01)
    tim.circle(120)
    tim.right(5)#->move right to left


#functional solution->calculating the number of cicles t finish
def draw_spirograph(size_of_gap):
    for n in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(120)
        #tim.right(5)
        tim.setheading(tim.heading() + size_of_gap)#->method for move tim left to right

draw_spirograph(5)#->range = 72


screen = t.Screen()
screen.exitonclick()
