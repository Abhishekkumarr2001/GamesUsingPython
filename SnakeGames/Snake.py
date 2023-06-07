from turtle import Turtle

STARTING_POSITION=[(0, 0), (-20, 0), (-40, 0)]
MOVE=20
RIGHT=0
UP=90
LEFT=180
DOWN=270

class Snake:

    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]
    
    def create_snake(self):  
        for position in STARTING_POSITION:
            self.add_snake(position)
           
    def increase_snake(self):
        self.add_snake(self.segments[-1].position())

    def add_snake(self,position):
        new_turtle=Turtle("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.segments.append(new_turtle)

    def move(self):
        for segment in range(len(self.segments)-1,0,-1):
            newx=self.segments[segment-1].xcor()
            newy=self.segments[segment-1].ycor()
            self.segments[segment].goto(newx,newy)
    
        self.segments[0].forward(MOVE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)