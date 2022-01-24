from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

s = Screen()
s.bgcolor('black')
s.setup(width=800, height=600)
s.title('PONG')
s.tracer(0)

paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350,0))

s.listen()
s.onkey(fun= paddle_r.go_up, key= 'Up')
s.onkey(paddle_r.go_down,'Down')
s.onkey(paddle_l.go_up, 'w')
s.onkey(paddle_l.go_down, 's')

ball = Ball()
scoreboard = ScoreBoard()


game_on = True

while game_on:
    time.sleep(ball.move_speed)
    s.update()
    ball.move()

    #detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collison with paddle_r
    if (ball.distance(paddle_r) < 50 and ball.xcor() > 320) or(ball.distance(paddle_l) < 50 and ball.xcor() < -320) :
        ball.bounce_x()

    #ball not hitiing paddle_r
    if ball.xcor() > 380:
        ball.reset_position()
        time.sleep(1)
        scoreboard.l_point()


    #ball not hiting paddle_l
    if ball.xcor() < -380:
        ball.reset_position()
        time.sleep(1)
        scoreboard.r_point()


s.exitonclick()

