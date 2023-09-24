from turtle import Screen, ontimer
from food import Food
from sneak import Sneak
from score_board import Score

def game_brain():
    if not sneak.is_moving:
        global food, score
        screen.onkeypress(fun=lambda: sneak.move("w"), key="w")
        screen.onkeypress(fun=lambda: sneak.move("s"), key="s")
        screen.onkeypress(fun=lambda: sneak.move("a"), key="a")
        screen.onkeypress(fun=lambda: sneak.move("d"), key="d")
        food = Food()
        check_position()
        self_consuming()
        check_if_on_board()

        score = Score()

        sneak.move_forward()



def check_position():
    x_head, y_head = sneak.head.position()
    x_food, y_food = food.position()
    z_head = 20
    if (x_head - z_head < x_food < x_head + z_head) and (y_head - z_head < y_food < y_head + z_head):
        food.new_position()
        score.score_num += 1
        score.score()

        sneak.add_segment()

    screen.ontimer(fun=check_position, t=100)

def self_consuming():

        for i in range(1, len(sneak.segments)):
            xh_pos, yh_pos = sneak.head.position()
            x_pos, y_pos = sneak.segments[i].position()
            z_len = 20
            if x_pos - z_len < xh_pos < x_pos + z_len and y_pos - z_len < yh_pos < y_pos + z_len:
                food.clear_food()
                score.delete_score()
                sneak.restart()
        screen.ontimer(fun=self_consuming, t=10)

def check_if_on_board():
    x_position, y_position = sneak.head.position()
    z_len = 10

    if -300 - z_len >= x_position or 300 <= x_position + z_len or 290 + 1.5 * z_len <= y_position or -290 >= y_position :
        sneak.is_moving = False


        food.clear_food()
        score.delete_score()
        sneak.restart()

    screen.ontimer(fun=check_if_on_board, t=100)


from time import sleep

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)  # animation 0 means auto_animation = False
screen.title("My sneak game")  # Window name
screen.bgcolor('olivedrab4')  # Window background color
screen.listen()  # Listen to keys

sneak = Sneak()



# key action inputs | fun=lambda: will let pre-input pass to sneak.move | key= is the key pressed

screen.onkey(key='space', fun=game_brain)
# TODO esc key fechar o programa  e R pra resetar o turtle
# ontimer()
# check_position()
# Detect collision when it gets the food


sneak.screen.exitonclick()
