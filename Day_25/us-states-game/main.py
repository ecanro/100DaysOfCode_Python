import pandas
import turtle

# TODO 1:Convert the guess to Title case
# TODO 2:Chek if the guess is among 50 states
# TODO 3: Write the correct guesses in the map
# TODO 4: Use a loop to allow the user  to keep guessing
# TODO 5: Record the correct guess in a list
# TODO 6: Keep track  of the score

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.bgpic("blank_states_img.gif")

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states Correct",
                                    prompt="What's another state's name: ?").title()
    data = pandas.read_csv("50_states.csv")
    all_states = data.state.to_list()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())





# # get the mouse click coordinates
# def get_mouse_click_coor(x, y):
#     print(x, y)
# # this line of code only work without use a var turtle
# turtle.onscreenclick(get_mouse_click_coor)
#
# # this line is another form to keep open the screen
#turtle.mainloop()

#screen.exitonclick()