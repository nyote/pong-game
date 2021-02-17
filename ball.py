from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.x_movement = 3
        self.y_movement = 3

    def move(self):
        new_x = self.xcor() + self.x_movement
        new_y = self.ycor() + self.y_movement
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_movement *= -1

    def bounce_table(self):
        self.x_movement *= -1
        self.x_movement *= 0.8

    def reset_game(self):
        self.goto(0, 0)
        self.speed("slow")
        self.bounce_table()
