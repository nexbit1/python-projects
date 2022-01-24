from turtle import Turtle, Screen, colormode
from random import randint


colormode(255)
t = Turtle()
s = Screen()
s.bgcolor('black')
t.speed('fastest')

colour = ('yellow','red', 'pink', 'cyan', 'lightgreen', 'blue')

for i in range(150):
    # r = randint(0, 255)
    # g = randint(0, 255)
    # b = randint(0, 255)
    # color = (r, g, b)
    # t.pencolor(color)
    t.pencolor(colour[i % 6])
    t.circle(190 - (i / 2) , 90)
    t.left(90)
    t.circle(190 - (i / 3), 90)
    t.left(60)










s.exitonclick()