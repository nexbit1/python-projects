from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.allcars = []
        self.hideturtle()
        self.car_speed = STARTING_MOVE_DISTANCE

    def creating_cars(self):
        if random.randint(1,6) == 1:
           new_car = Turtle()
           new_car.shape('square')
           new_car.shapesize(stretch_wid=1, stretch_len=2)
           new_car.penup()
           new_car.color(random.choice(COLORS))
           random_y = random.randint(-230, 230)
           new_car.goto(x=300, y=random_y)
           self.allcars.append(new_car)

    def move_cars(self):
        for i in self.allcars:
            i.backward(self.car_speed)

    def levelup(self):
        self.car_speed += MOVE_INCREMENT