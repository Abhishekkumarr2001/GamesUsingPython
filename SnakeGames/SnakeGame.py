from turtle import Turtle,Screen, onkey, width
import time
from Snake import Snake
from Food import Food
from Scoreboard import Scoreboard

screen=Screen()
screen.screensize(600,600)
screen.bgcolor("Black")
screen.title("Snake Game")
screen.tracer(0)


snake=Snake()
food=Food()
score=Scoreboard()
game_on=True

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food)<20:
        food.refresh_food()
        snake.increase_snake()
        score.score_increment()

    if snake.head.xcor() > 375 or snake.head.xcor() < -380 or snake.head.ycor() > 320 or snake.head.ycor() < -300:
        game_on=False
        score.gameover()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            game_on=False
            score.gameover()


screen.exitonclick()