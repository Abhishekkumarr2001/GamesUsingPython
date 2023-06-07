from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen=Screen()
screen.screensize(bg="black")
screen.title("Pong game")
screen.tracer(0)
ball=Ball()
scoreboard=Scoreboard()
game_on=True

right_paddle=Paddle((360,0))
left_paddle=Paddle((-370,0))

screen.listen()
screen.onkey(right_paddle.up,"Up")
screen.onkey(right_paddle.down,"Down")
screen.onkey(left_paddle.up,"w")
screen.onkey(left_paddle.down,"s")

while game_on:
    screen.update()
    ball.move()
    time.sleep(ball.ball_speed)

    if ball.ycor() > 300 or ball.ycor()< -280:
        ball.bouncey()

    if ball.distance(right_paddle)<50 and ball.xcor() > 320 or ball.distance(left_paddle)< 50 and ball.xcor() < -340:
        ball.bouncex()

    if ball.xcor() > 380:
        ball.reset_pos()
        scoreboard.l_score_update()
    
    if ball.xcor() < -380:
        ball.reset_pos()
        scoreboard.r_score_update()

screen.exitonclick()
