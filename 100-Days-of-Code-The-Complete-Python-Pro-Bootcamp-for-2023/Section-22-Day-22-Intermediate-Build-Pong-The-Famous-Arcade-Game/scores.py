from turtle import Turtle

FONT = ('Courier', 15, 'bold')

class Scores(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.p_score_num = 0
        self.c_score_num = 0
        self.user_score()
        self.com_score()

    def win_condition(self):
        if self.p_score_num == 5:
            return True, 'player'
        elif self.c_score_num == 5:
            return True, "Com"
        else:
            return False, None

    def add_points(self, user_points, com_points):
        if user_points != self.p_score_num:
            self.p_score_num += 1
        if com_points != self.c_score_num:
            self.c_score_num += 1
        self.reset_scores()

    def user_score(self):
        self.setpos(-130, 270)
        self.write(f"Score: {self.p_score_num}", align="left", font=FONT)

    def com_score(self):
        self.setpos(130, 270)
        self.write(f"Score: {self.c_score_num}", align="right", font=FONT)

    def win_text(self):
        self.setpos(0, 36)
        self.write("Win", align="center", font=('Courier', 25, 'bold'))

    def game_over_text(self):
        self.setpos(0, 36)
        self.write("Loser", align="center", font=('Courier', 25, 'bold'))

    def reset_scores(self):
        self.clear()
        self.hideturtle()
        self.user_score()
        self.com_score()



