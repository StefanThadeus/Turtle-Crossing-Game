from turtle import Turtle

FONT = ("Courier", 18, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.level = 0
        self.update()

    def update(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", False, align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", False, align="center", font=FONT)
