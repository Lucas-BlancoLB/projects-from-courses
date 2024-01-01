from turtle import Screen, Turtle
from scores import Scores
from ball import Ball
from rackets import Rackets
import time
# TODO create rackets com n player on both ends
# TODO Create a ball that will be heading and while True moving forward
# TODO When the ball hits com or player gol score up and *-1   the headling angle
# TODO A point line right in the middle of the square - vertical. Com n player score on middle top shifted by some
#  minor PXs
# TODO com racket should follow the ball to defend it gol. but it should follow with wrong info
#  so player can mark a gol

screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor('black')
screen.tracer(0)
screen.listen()

scores = Scores()
rackets = Rackets()
ball = Ball()

def middle_point_line():
    point_line = Turtle("square")
    point_line.setpos(0, 260)
    point_line.setheading(270)
    point_line.pensize(10)
    point_line.color('grey')
    while point_line.ycor() >= -270:
        point_line.forward(25)
        point_line.penup()
        point_line.forward(30)
        point_line.pendown()
    point_line.hideturtle()


def winner_setting(conditon_2):

    if conditon_2 == "player":
        scores.win_text()
    else:
        scores.game_over_text()



screen.onkeypress(fun=rackets.player_move_forward, key='w')
screen.onkeypress(fun=rackets.player_move_forward, key='Up')
screen.onkeypress(fun=rackets.player_move_backwards, key="s")
screen.onkeypress(fun=rackets.player_move_backwards, key="Down")
middle_point_line()

is_game_on = True
while is_game_on:
    time.sleep(0.04)
    screen.update()
    ball.moving()
    ball.check_colision_with_rackets(rackets.player, rackets.comp)
    rackets.comp_movements(ball)
    scores.add_points(ball.player_points, ball.com_points)
    condition, condition2 = scores.win_condition()
    if condition:
        ball.goto_center()
        is_game_on = False

        winner_setting(condition2)


screen.update()
screen.exitonclick()
