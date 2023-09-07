from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.tracer(0)

r_paddle = Paddle(370, 0)
l_paddle = Paddle(-370, 0)
ball = Ball()
score = Score()


screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")


game_on = True
while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if (ball.ycor() > 280) or (ball.ycor() < -280):
        ball.y_bounce()

    if (ball.distance(r_paddle) < 50) and (ball.xcor() > 350) or (ball.distance(l_paddle) < 50) and \
            (ball.xcor() < -350):
        ball.x_bounce()

    if ball.xcor() > 380:
        ball.refresh()
        score.l_wins()

    if ball.xcor() < -380:
        ball.refresh()
        score.r_wins()


screen.exitonclick()
