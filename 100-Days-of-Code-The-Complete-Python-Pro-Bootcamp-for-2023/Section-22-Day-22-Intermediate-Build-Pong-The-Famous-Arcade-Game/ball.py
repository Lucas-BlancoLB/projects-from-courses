from turtle import Turtle
from random import randint, choice


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setpos(0, 5)
        self.setheading(choice([x for x in range(0, 360) if not 60 < x < 120 and not 240 < x < 300]))
        self.moving()
        self.com_points = 0
        self.player_points = 0
        print(self.player_points, self.com_points)

    def moving(self):
        xc, yc, z, bory, borx = self.xcor(), self.ycor(), 10, 280, 480

        if -borx - z - 10 <= xc <= borx + z and -bory - z <= yc <= bory + z:
            if xc - z <= -borx or xc + z > borx:
                self.check_goal_position()
            elif yc - z <= -bory or yc + z >= bory:
                self.seth(-self.heading())
            self.forward(15)

        else:
            self.forward(15)

    def check_goal_position(self):

        if self.xcor() <= -490:
            self.setpos(0, 0)
            self.setheading(choice([x for x in range(0, 361) if 120 <= x <= 240]))
            self.com_points += 1

        elif self.xcor() >= 480:
            self.setpos(0, 0)
            self.setheading(choice([x for x in range(0, 361) if 0 <= x <= 60 or 300 <= x <= 360]))
            self.player_points += 1

            # print(angle_com)

    def check_colision_with_rackets(self, player, computer):
        x, y, = self.xcor(), self.ycor()

        if (player.xcor() - 20 <= x <= player.xcor() + 20) and (player.ycor() - 90 <= y <= player.ycor() + 90):
            self.seth(-self.heading())
            self.seth(180 - self.heading() * -1)

        elif (computer.xcor() - 20 <= x <= computer.xcor() + 20) and (computer.ycor() - 90 <= y <= computer.ycor() + 90):
            self.seth(-self.heading())
            self.seth(180 - self.heading() * -1)
            distance = computer.ycor() - computer.ycor()
            computer.forward(distance)

    def goto_center(self):
        self.setpos(0, 0)
