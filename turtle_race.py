from turtle import Turtle, Screen
import random


s = Screen()
s.setup(width= 800, height= 400)
is_race_on = False
user_bet = s.textinput(title = 'Turtle Race', prompt = 'Choose colour of turtle')
colour = ['red', 'orange', 'yellow', 'blue', 'green', 'purple']
y_posi = [-70, -40, -10, 20, 50, 80]
turtles = []

for turtle_no in range(0,6):
    t = Turtle('turtle')
    t.penup()
    t.color(colour[turtle_no])
    t.goto(x = -380, y = y_posi[turtle_no])
    turtles.append(t)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 370:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f'you\'re {winning_turtle} turtle has won')
            else:
                print(f'you\'re {user_bet} turtle has lost')
        dist = random.randint(0,10)
        turtle.forward(dist)


















s.exitonclick()