from turtle import Turtle,Screen
from carmanager import Carmanager
from player import Player
from scoreboard import Scoreboard
import time

screen=Screen()
screen.screensize()
screen.title("Turtle Crossing")
screen.tracer(0)
player=Player()
carmanager=Carmanager()
scoreboard=Scoreboard()
screen.listen()
screen.onkey(player.moving,"Up")

game_on=True

while game_on:
    screen.update()
    time.sleep(0.1)
    carmanager.cars()
    carmanager.moving()

    for cars in carmanager.all_cars:
        if cars.distance(player)<20:
            game_on=False
            scoreboard.game_over()

    if player.finish_line():
        player.starting_line()
        carmanager.levelup()
        scoreboard.increase_level()

screen.exitonclick()
