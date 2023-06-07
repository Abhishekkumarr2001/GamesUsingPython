from turtle import Turtle, colormode
import random

colormode(255)
COLOR=["red","green","blue","yellow","black","pink","orange","indigo"]
STARTING_MOVE_DISTANCE=5
SPEED_INC=10

class Carmanager:
    def __init__(self):
        self.all_cars=[]
        self.carspeed=STARTING_MOVE_DISTANCE
    
    def cars(self):
        chance=random.randint(1,5)
        if chance==1:
            car=Turtle("square")
            car.shapesize(stretch_wid=1,stretch_len=2)
            car.penup()
            car.color(random.choice(COLOR))
            rand_y=random.randint(-250,250)
            car.goto(300,rand_y)
            self.all_cars.append(car)
    
    def moving(self):
        for cars in self.all_cars:
            cars.backward(self.carspeed)

    def levelup(self):
        self.carspeed+=SPEED_INC

    

    