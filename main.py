from turtle import Screen
from table import Table
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

x_table = Table((350,0))
y_table = Table((-350,0))
ball = Ball()
scoreboard_x = Scoreboard((150, 250))
scoreboard_y = Scoreboard((-150, 250))

screen.listen()
screen.onkey(x_table.up, "Up")
screen.onkey(x_table.down, "Down")
screen.onkey(y_table.up, "w")
screen.onkey(y_table.down, "s")

playing = True
while playing:
    screen.update()
    ball.move()

    #detect the upper and lower walls
    if ball.ycor() >= 300 or ball.ycor() <= -300:
        ball.bounce()

    #Detect the tables

    if ball.distance(x_table) < 50 and ball.xcor() > 340 or ball.distance(y_table) < 50 and ball.xcor() < -340:
        ball.bounce_table()


    #Ball is missed
    if ball.xcor() > 350:
        ball.reset_game()
        scoreboard_y.add_score()

    if ball.xcor() < -350:
        ball.reset_game()
        scoreboard_x.add_score()

screen.exitonclick()