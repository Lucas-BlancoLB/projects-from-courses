from turtle import Turtle, Screen
import random

race_on = False

def y_position():
    global y
    hold_y_position = y
    y -= 25
    return hold_y_position


def random_color():
    global colors
    color = random.choice(colors)
    colors.remove(color)
    return color
def make_turtles(n, color):
    object_name = Turtle('turtle')
    object_name.color(color)
    object_name.penup()
    object_name.goto(x=-230, y=n )
    return object_name


''''firebrick1 = red /  blueviolet = purple / deeppink2 = pink /  forestgreen = green / dodgerblue2 = blue'''
y = 55
colors = ['firebrick1', 'blueviolet', 'deeppink2', 'forestgreen', 'dodgerblue2']
colors_backup = ['firebrick1', 'blueviolet', 'deeppink2', 'forestgreen', 'dodgerblue2']
correct_colors = ['red', 'purple', 'pink', 'green', 'blue']
screen = Screen()
screen.setup(width=500, height=175)

while True:
    user_bet = screen.textinput(title="Make your bet", prompt='choose a color (Red/Purple/Pink/Green/Blue)').lower()
    if user_bet in correct_colors: break

turtles = []
for _ in range(5):
    turtle = make_turtles(n=y_position(), color=random_color())
    turtles.append(turtle)
if user_bet:
    race_on = True


while race_on:
    var = random.randint(0, 4)
    turtles[var].setx(turtles[var].xcor() + random.randint(-1, 5))

    if turtles[var].xcor() >= 238:
        turtle_winner = turtles[var]
        wrong_color = turtle_winner.color()[0]

        index = colors_backup.index(wrong_color)
        if user_bet == correct_colors[index]:
            print(f'You guessed right, {correct_colors[index]} won!')
        else:
            print(f'You guessed it wrong, it was {correct_colors[index]}! ')
        race_on = False


screen.exitonclick()
