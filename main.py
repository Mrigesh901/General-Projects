from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time
screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")

paddle_l = Paddle((350, 0))
paddle_r = Paddle((-350, 0))
ball = Ball()
sb = ScoreBoard()


screen.tracer(0)
screen.listen()
screen.onkey(paddle_l.up, "Up")
screen.onkey(paddle_l.down, "Down")

screen.onkey(paddle_r.up, "w")
screen.onkey(paddle_r.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # collision with walls
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce()

    # collision with paddle
    if ball.distance(paddle_l) < 50 and ball.xcor() > 340 or ball.distance(paddle_r) < 50 and ball.xcor() < -340:
        ball.paddle_bounce()

    if ball.xcor() > 360:
        sb.l_point()
        ball.reset_position()

    if ball.xcor() < -360:
        sb.r_point()
        ball.reset_position()


screen.exitonclick()
