import colorgram


# colors = colorgram.extract('image.jpg', 30)   #for extracting colors from jpeg
# rgb = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb.append((r, g, b))
# print(rgb)
from turtle import Turtle, Screen, colormode
from random import choice


colormode(255)
t = Turtle()
s = Screen()
color_list = [(244, 225, 73), (180, 77, 28), (49, 37, 26), (220, 151, 75), (145, 28, 41), (44, 43, 120), (22, 25, 69), (170, 21, 16), (242, 235, 239), (49, 85, 158), (211, 85, 128), (158, 49, 85), (120, 161, 224), (28, 43, 28), (216, 80, 63), (138, 183, 137), (116, 106, 203), (66, 30, 35), (76, 118, 53), (157, 179, 231), (151, 211, 191), (202, 124, 162), (82, 151, 113), (86, 87, 34), (60, 147, 170), (199, 136, 46), (56, 100, 20)]
t. speed('fastest')
t.penup()
t.hideturtle()
t.setheading(225)
t.forward(400)
t.setheading(0)
number_of_dots = 120
for dot_count in range(1,number_of_dots + 1):
    t.dot(25, choice(color_list))
    t.forward(50)

    if dot_count % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)














s.exitonclick()
