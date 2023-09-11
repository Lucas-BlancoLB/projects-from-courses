from turtle import Turtle, Screen

filian = Turtle()
screen = Screen()
filian.shape('arrow')
filian.speed('fast')


def move_forwards():
    filian.forward(20)


def move_backwards():
    filian.forward(-20)


def move_clockwise():
    filian.right(10)


def move_counter_clockwise():
    filian.lt(10)

def reset_turtle():
    filian.reset()


screen.listen()
screen.onkey(key='w', fun=move_forwards)
screen.onkey(key='s', fun=move_backwards)
screen.onkey(key='d', fun=move_clockwise)
screen.onkey(key='a', fun=move_counter_clockwise)
screen.onkey(key='c', fun=reset_turtle)


screen.exitonclick()
