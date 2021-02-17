from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(coordinates)
        self.color("white")
        self.update_scoreboard()
        self.hideturtle()

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.write(arg=f"Score = {self.score}", align="center", font=("Arial", 16, "normal"))

