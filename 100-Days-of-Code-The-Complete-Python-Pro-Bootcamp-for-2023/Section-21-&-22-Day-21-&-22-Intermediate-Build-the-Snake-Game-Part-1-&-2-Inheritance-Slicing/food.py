from turtle import Turtle
import random


class Food(Turtle):
# TODO wid=0.5, len=0.5
    def __init__(self):
        super().__init__()
        self.shape("circle")  # TODO I could use square or circle
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)  # takes the normal size 20 n turn to 10
        self.speed(0)  # Fastest speed
        self.color("white")
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(x=random_x, y=random_y)
        self.pendown()
        self.position()

    def new_position(self):
        self.reset()
        self.__init__()

    def clear_food(self):
        self.hideturtle()



print(random.randint(-300,300))