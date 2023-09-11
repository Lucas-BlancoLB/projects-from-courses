from turtle import Turtle,Screen, colormode
from random import randint, choice

# def forward():
#     jimm.forward(100)
#
#
# def right_turn():
#     jimm.right(90)


jimm = Turtle()
jimm.shape('arrow')
jimm.color('DarkOliveGreen4')
jimm.speed(0)
jimm.pensize(0)
colormode(255)

for _ in range(36):
    jimm.pencolor(randint(0,255), randint(0,255), randint(0,255))
    jimm.circle(100)
    jimm.left(10)






# colors = ['red', 'brown', 'DarkGreen', 'black', 'orange', 'purple', 'pink', 'gold4', 'DarkBlue', "DarkGrey"]
# directions = [0, 90, 180, 270]
# for _ in range(1000):
#     jimm.pencolor(randint(0,255), randint(0,255), randint(0,255))
#     jimm.forward(25)
#     jimm.seth(choice(directions))

# TODO random walk
# TODO trick lines
# TODO random colors























# for i in range(3,11):
#     jimm.pencolor(random.choice(colors))
#     for _ in range(i):
#         angle = 360 / i
#         jimm.forward(100)
#         jimm.right(angle)





# for _ in range(6):
#     jimm.pendown()
#     jimm.forward(25)
#     jimm.penup()
#     jimm.forward(25)





# forward()
# right_turn()
#
# forward()
# right_turn()
# forward()
# right_turn()
# forward()

# for _ in range(4):
#     jimm.right(90)
#     jimm.forward(100)

""""From random import EVERYTHING = from random import * """
# from random import *

import prettytable as table

import villains

print(villains.gen())













screen = Screen()
screen.exitonclick()