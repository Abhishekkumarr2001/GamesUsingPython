from distutils.command.clean import clean
from turtle import Turtle

FONT=("Courier",20,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.penup()
        self.hideturtle()
        self.goto(-370,280)
        self.level_board()
    
    def level_board(self):
        self.clear()
        self.write(f"Level : {self.level}", align="left", font=FONT)
    
    def increase_level(self):
        self.level+=1
        self.level_board()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over.", align="center", font=FONT)