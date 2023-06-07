from msilib.schema import Font
from turtle import Turtle

ALLIGNMENT="center"
FONT=("Ariel",20,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,280)
        self.hideturtle()
        self.update_score()
       
    def update_score(self):
        self.write(f"Score : {self.score}", align=ALLIGNMENT, font=FONT)

    def gameover(self):
        self.goto(0,0)
        self.write("Game Over", align=ALLIGNMENT, font=FONT)

    def score_increment(self):
        self.score+=1
        self.clear()
        self.update_score()