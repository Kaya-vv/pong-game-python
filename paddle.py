from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270


class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.shapesize(5, 1)
        self.color("white")
        self.penup()
        self.goto(pos)

    def up(self):
        self.setpos(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def down(self):
        self.setpos(self.xcor(), self.ycor() - MOVE_DISTANCE)
