import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


def increase_speed():
    if score.score_num != 0:
        car_manager.move_increment = 10 * score.score_num


def collider_with_car():
    z, z2, z3 = 5, 55, 30
    for var in car_manager.cars:
        player_x, player_y = player.xcor(), player.ycor()
        var_x, var_y = var.xcor(), var.ycor()
        if var_y - z3 <= player_y + z and var_y + z3 >= player_y - z and var_x - z2 <= player_x + z and \
                var_x + z2 >= player_x - z:
            score.game_over()
            screen.title("Game Over Bitch")
            screen.update()
            return False
    else:
        return True


def restart():
    score.reset_score()

    score.__init__()
    car_manager.reset_cars()
    player.reset_player()
    running_game(True)


def running_game(is_game_on):
    while is_game_on:
        car_manager.cars_moving()
        time.sleep(0.001)
        screen.update()
        score.add_score(player.ycor())
        player.is_at_win_position()
        is_game_on = collider_with_car()
        car_manager.if_car_touches_border()
        increase_speed()


screen = Screen()
screen.title('Turtle Crossing')
screen.setup(width=600, height=600)
screen.bgcolor('#4b494a')
screen.tracer(0)
screen.listen()
player = Player()
score = Scoreboard()
car_manager = CarManager()
car_manager.cars_moving()

screen.onkeypress(fun=player.move_forwards, key='w')
screen.onkeypress(fun=player.move_forwards, key='W')
screen.onkeypress(fun=player.move_forwards, key='Up')
screen.onkey(fun=restart, key= "r")
screen.onkey(fun=restart, key= "R")

game_is_on = True
running_game(game_is_on)

screen.exitonclick()
