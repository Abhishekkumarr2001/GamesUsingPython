from turtle import Turtle

STARTING_POS=(0,-280)
MOVE_DISTANCE=10
FINISH_LINE_Y=300

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.starting_line()
        self.setheading(90)

    def moving(self):
        self.forward(MOVE_DISTANCE)

    def starting_line(self):
        self.goto(STARTING_POS)

    def finish_line(self):
        if self.ycor()>FINISH_LINE_Y:
            return True
        else:
            return False
