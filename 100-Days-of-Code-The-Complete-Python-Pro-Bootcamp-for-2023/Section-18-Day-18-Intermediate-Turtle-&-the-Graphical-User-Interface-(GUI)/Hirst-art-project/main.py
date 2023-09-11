# import colorgram
import turtle as t
import random
import time


def circleful(colors):
    for i in range(10):
        hirst.pendown()
        color = random_color(colors)
        hirst.color(color)
        hirst.begin_fill()
        hirst.circle(20)
        hirst.end_fill()
        hirst.begin_fill()
        hirst.penup()
        if i != 9:
            hirst.forward(70)


def random_color(colors):
    return random.choice(colors)

def go_back():
    hirst.left(180)
    hirst.forward(630)
    hirst.right(90)
    hirst.forward(70)
    hirst.right(90)


t.colormode(255)
hirst = t.Turtle()
hirst.color('white')
hirst.shapesize(0.1)
hirst.speed(0)
hirst.shape('arrow')
color_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50),
(222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47,
121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77)]

print(hirst.position())

hirst.setposition(-330, -330)
time.sleep(0.5)
for _ in range(10):
    circleful(color_list)
    go_back()

# TODO 10 x 10 colorful circles
# TODO each circle with 20 radius. Keep a distance of 50 steps









screen = t.Screen()
screen.exitonclick()

# extract = colorgram.extract('image.jpg', 20)
#
# colors = list()
#
# for i in range(len(extract)):
#     rgb = extract[i].rgb
#     color = (rgb.r, rgb.g, rgb.b)
#     colors.append(color)
#
# print(colors)
