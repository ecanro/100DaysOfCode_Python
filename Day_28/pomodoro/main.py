from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 10
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def time_reset():
    global reps
    reps = 0
    windows.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    pomodoro_title.config(text="Timer")
    pomodoro_stages.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_time():
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN*60)
        pomodoro_title.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN*60)
        pomodoro_title.config(text="Break", fg=PINK)
    else:
        count_down(WORK_MIN*60)
        pomodoro_title.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

# we have a problem, and is that time displayed is 5:0 instead 5:00
# and other problem is if count_sec < 10->display 9-8-7-6.. but no 09,08,07,06...
# we will use dynamic typing
    if count_sec == 0 or count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = windows.after(1000, count_down, count - 1)
    else:
        start_time()
        marks = ""
        work_sessions = math.floor(reps/2)
        for n in range(work_sessions):
            marks += "✔"
        pomodoro_stages.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #


windows = Tk()
windows.title("Pomodoro clock")
windows.config(padx=100, pady=50, bg=YELLOW)

# create canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
pomodoro_img = PhotoImage(file="tomato.png")

# display image bg
canvas.create_image(100, 112, image=pomodoro_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=2)


# create label
pomodoro_title = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
pomodoro_title.grid(column=1, row=0)

# create buttons
start_btn = Button(text="Start", command=start_time)
start_btn.grid(column=0, row=4)

reset_btn = Button(text="Reset", command=time_reset)
reset_btn.grid(column=2, row=4)

# create stages
pomodoro_stages = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15))
pomodoro_stages.grid(column=1, row=6)

windows.mainloop()
