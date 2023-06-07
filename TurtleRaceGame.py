from turtle import *
import random

israceon = False
all_turtle = []

screen = Screen()
screen.title("Turtle Race")
screen.setup(height=500, width=700)

colour = ["pink", "red", "orange", "yellow", "green", "blue", "indigo"]

user_bet = screen.textinput("Your Choice", "Which turtle would win ?\nChoices:\n1.Pink\n2.Red\n3.Orange\n4.Yellow\n5.Green\n6.Blue\n7.Indigo")

y_position = [-180, -120, -60, 0, 60, 120, 180]

for index in range(0, 7):
    new_turtle = Turtle("turtle")
    new_turtle.color(colour[index])
    new_turtle.penup()
    new_turtle.goto(-330, y_position[index])
    all_turtle.append(new_turtle)

if user_bet:
    israceon = True

while israceon:
    for turt in all_turtle:
        if turt.xcor() > 330:
            israceon = False
            winnerturt = turt.pencolor()
            if winnerturt == user_bet:
                print(f"Your Turtle Won! the Winner turtle is {winnerturt} Turtle.")
            else:
                print(f"Your Turtle Lost! the Winner turtle is {winnerturt} Turtle.")

        random_distance = random.randint(0, 10)
        turt.forward(random_distance)

screen.exitonclick()
