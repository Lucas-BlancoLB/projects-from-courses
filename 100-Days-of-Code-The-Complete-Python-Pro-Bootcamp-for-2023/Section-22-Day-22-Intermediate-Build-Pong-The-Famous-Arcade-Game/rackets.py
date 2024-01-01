from turtle import Turtle
from random import uniform, randint, random
from time import sleep
class Rackets:
    def __init__(self):
        self.player = Turtle("square")
        self.comp = Turtle("square")
        self.player.setpos(-483, 0)
        self.player.seth(90)
        self.player.color("white")
        self.player.penup()
        self.player.resizemode("user")
        self.player.shapesize(0.4, 8.7, 3)

        self.comp = Turtle("square")
        self.comp.setpos(475, 0)
        self.comp.seth(90)
        self.comp.color("white")
        self.comp.penup()
        self.comp.resizemode("user")
        self.comp.shapesize(0.4, 8.7, 3)

    def player_move_forward(self):
        if not self.player.ycor() >= 210:
            self.player.forward(15)

    def player_move_backwards(self):
        if not self.player.ycor() <= -210:
            self.player.forward(-15)


    def comp_movements(self, ball):
        # if -203 <= ball.ycor() <= 211:


        speed_factor = 0.1
        distance = ball.ycor() - self.comp.ycor()
        if random() < 0.4:
            error = randint(-30, 30)
            distance += error
            print(error)
        self.comp.sety(self.comp.ycor() + distance * speed_factor)
        max_speed = 25
        if self.comp.speed() > max_speed:
            self.comp.speed(max_speed)
        #~~~~

        # if self.comp.ycor() < 211:
        #     if self.comp.ycor() > ball.ycor():
        #         self.comp.forward(randint(10,25))
        # if self.comp.ycor() > -203:
        #     if self.comp.ycor() < ball.ycor():
        #         self.comp.forward(-randint(10,25))

            #~~~~

            # self.comp.sety(ball.ycor() + uniform(10, 30))
            # if self.comp.ycor() < ball.ycor():
            #     self.comp.sety(uniform(0, ball.ycor()))
            # elif self.comp.ycor() > ball.ycor():
            #     self.comp.sety(( uniform(0, ball.ycor())))
