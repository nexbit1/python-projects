from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):


    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(x = -235, y = 270)
        self.write(f'LEVEL: {self.level}', align= 'center', font= FONT)

    def update_score(self):
        self.clear()
        self.write(f'LEVEL: {self.level}', align='center', font=FONT)

    def increase_score(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write('GAME OVER', align='center', font=FONT)
