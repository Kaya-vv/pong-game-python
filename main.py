from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
STARTING_BALL_SPEED = 0.03

t = Turtle()
screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("The Pong Game")
screen.tracer(0)
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
l_score = Scoreboard((-100, 220))
r_score = Scoreboard((100, 220))
ball = Ball()
ball_speed = STARTING_BALL_SPEED
screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

game_on = True

while game_on:
    ball.move()
    screen.update()
    time.sleep(ball_speed)

    # Detect collision and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        if ball_speed > 0.01:
            ball_speed -= 0.003

    if ball.xcor() > 400:
        l_score.increase_score()
        ball_speed = STARTING_BALL_SPEED
        ball.reset()

    if ball.xcor() < -400:
        r_score.increase_score()
        ball_speed = STARTING_BALL_SPEED
        ball.reset()


screen.exitonclick()
