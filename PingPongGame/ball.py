from mimetypes import init
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.xaxis=10
        self.yaxis=10
        self.ball_speed=0.1

    def move(self):
        newx=self.xcor()+self.xaxis
        newy=self.ycor()+self.yaxis
        self.penup()
        self.goto(newx,newy)

    def bouncey(self):
        self.yaxis*=-1
        
    def bouncex(self):
        self.xaxis*=-1
        self.ball_speed*=0.9

    def reset_pos(self):
        self.goto(0,0)
        self.ball_speed=0.1
        self.bouncex()