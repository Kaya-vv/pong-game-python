from turtle import Turtle

FONT = ("Courier", 48, "bold")


class Scoreboard(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(pos)
        self.write(self.score, align="center", font=FONT)

    def update_score(self):
        self.write(self.score, align="center", font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()
