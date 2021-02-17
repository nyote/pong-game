from turtle import Turtle

class Table(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        self.shape("square")
        self.penup()
        self.goto(coordinates)
        self.turtlesize(stretch_wid=4, stretch_len=1)
        self.color("white")

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

