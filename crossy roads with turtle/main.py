import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(fun=player.move, key= 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.creating_cars()
    cars.move_cars()

    for car in cars.allcars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()

   #detect successful crossing
    if player.is_at_finish_line():
        player.goto_start()
        cars.levelup()
        score.increase_score()



screen.exitonclick()