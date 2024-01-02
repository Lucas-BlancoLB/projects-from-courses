from turtle import Turtle
from car_manager import CarManager

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

car_manager = CarManager

class Player(Turtle):

    def __init__(self):
        super().__init__("turtle")
        self.color('black', 'green')
        self.penup()
        self.setheading(90)
        self.sety(-280)



    #move forward one press
    def move_forwards(self):
        self.forward(MOVE_DISTANCE)


    def is_at_win_position(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.sety(-280)


    def reset_player(self):
        self.sety(-280)
6666666666666666666666666666666666666666666