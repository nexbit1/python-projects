from turtle import Turtle, Screen, colormode
from random import choice, randint
t = Turtle()
s = Screen()
colormode(255)
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
direction = [0,90,180,270,]

t.pensize(10)
t.speed('fastest')

while True:
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    t.pencolor(r, g, b)
    t.forward(25)
    t.setheading(choice(direction))














s.exitonclick()
