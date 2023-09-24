from turtle import Turtle

FONT = ('Courier', 20, 'normal')
ALIGNMENT = 'center'
class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.delete_score()
        self.color('white')
        self.penup()
        self.pensize(40)
        self.setposition(0, 270)
        self.score_num = 0
        self.score()

    def score(self):
        self.delete_score()
        self.write(f'Score : {self.score_num}', False, align=ALIGNMENT, font=FONT)


    def delete_score(self):
        self.hideturtle()
        self.clear()

    def reset_score(self):
        self.reset()
