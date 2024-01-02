from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

        self.color('white')
        self.score_num = 0
        self.score()


    def score(self):
        self.setpos(-295, 265)
        self.write(f'Score: {self.score_num}', True, font=FONT)

    def add_score(self, player_y):
        """ use ycor() from turtle or any value for y coordinates """
        if player_y >= 280:
            self.score_num += 1
            self.reset_score()
            self.score()

    def reset_score(self):
        self.hideturtle()
        self.clear()



    def game_over(self):
        self.setposition(-86, 0)
        self.write("GAME OVER", move=False, font=FONT)