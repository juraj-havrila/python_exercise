FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100,250)
        self.write(f"Level: {self.score}", align="center", font=FONT)

    def add_point(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        #self.clear()
        self.color("red")
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)
