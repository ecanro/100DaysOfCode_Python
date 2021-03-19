from turtle import Turtle

AlIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 0
        self.goto(0, 260)
        self.update_levelboard()

    def update_levelboard(self):
        self.clear()
        self.goto(-220, 260)
        self.write(f"Level: {self.level}", False, align=AlIGNMENT, font=FONT)

    def level_up(self):
        self.clear()
        self.level += 1
        self.update_levelboard()


    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=AlIGNMENT, font=FONT)
