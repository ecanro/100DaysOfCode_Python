from tkinter import * # only import class
import pandas
import random

# Vars
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# ----- Random cards ------ #
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    windows.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    current_card["French"]
    print(current_card["French"])
    canvas.itemconfig(car_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = windows.after(3000, func=flip_card)

# ------ Flip cards -----#


def flip_card():
    canvas.itemconfig(car_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

# ---- save cards ----#
def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# ------UI------ #

# create the main windows
windows = Tk()
windows.title("Flash Card Frequency words")
windows.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# timer for flip card
flip_timer = windows.after(3000, func=flip_card)

# create canvas
canvas = Canvas(width=800, height=526,  bg=BACKGROUND_COLOR, highlightthickness=0)

# load image
card_back_img = PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")

card_background = canvas.create_image(410, 263, image=card_front_img)
car_title = canvas.create_text(400, 133, text="", font=("Ariel", 35, "italic"))
card_word = canvas.create_text(400, 266, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# create buttons
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(column=1, row=1)


next_card()

windows.mainloop()
