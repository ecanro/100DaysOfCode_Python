from turtle import Turtle, Screen

tim = Turtle() #->separete instance of tommy and any other turtle
screen = Screen()

tim.shape("turtle")#->states of tim
tim.color("red")

# tommy = Turtle()#->separate instance of tim and any other turtle
# tommy.color("blue")#->states of tommy
# tommy.goto(-400,0)

def tim_forwards():
    tim.forward(10)

def tim_right():
    new_heading = tim.heading() -10
    tim.setheading(new_heading)

def tim_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def tim_backwards():
    tim.back(10)

def tim_clear_screen():
    tim.clear()
    tim.penup()
    #tim.goto(0,0)
    tim.home()
    tim.pendown()

#tim will move every time a key is push
screen.onkey(fun=tim_forwards, key="w")
screen.onkey(fun=tim_backwards, key="s")
screen.onkey(fun=tim_right, key="d")
screen.onkey(fun=tim_left, key="a")

screen.onkey(fun=tim_clear_screen, key="c")

screen.listen()
screen.exitonclick()