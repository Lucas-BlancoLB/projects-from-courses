import tkinter as tk
from PIL import ImageTk

# THEME_COLOR = "#375362"
THEME_COLOR = "#3EAC9C"
class QuizInterface:

    def __init__(self, quiz):


        self.quiz = quiz

        self.root = tk.Tk()
        self.root.title("Quizler")
        self.root.config(bg=THEME_COLOR)


        self.score_num = self.quiz.score
        # self.q_num,self.next_quest = quiz.next_question()
        self.current_q_num = 0
        self.q_num = self.quiz.question_number
        # print(self.q_num)
        self.question = None
        self.score_label_tk = None
        self.canvas_tk = None
        self.green = ImageTk.PhotoImage(file="images/green.png")
        self.red = ImageTk.PhotoImage(file="images/red.png")
        self.wrong_ph = ImageTk.PhotoImage(file="images/false.png")
        self.right_ph = ImageTk.PhotoImage(file="images/true.png")

        
        self.score_label()
        self.canvas()
        self.buttons()

        self.root.mainloop()

    def score_label(self):
        if self.score_label_tk:
            self.score_label_tk.config(text=f"Score: {self.score_num}")
            # print(self.q_num)
        else:
            self.score_label_tk = tk.Label(text=f"Score: {self.score_num}", font=("Press Start 2P", 25), bg=THEME_COLOR)
            self.score_label_tk.grid(row=0,column=0, pady=20)
    def canvas(self):
        if self.canvas_tk:
            self.canvas_tk.itemconfig(self.question, text=f"Q.{self.q_num}: {self.question_data()}")
        else:
            canvas_tk = tk.Canvas(width=self.green.width(), height=self.green.height(), highlightthickness=0,)

            canvas_tk.create_image(0,0 ,anchor=tk.NW, image=self.green)
            self.question = canvas_tk.create_text(self.green.width()/2,self.green.height()/2,
                                          anchor=tk.CENTER, text=f"Q.{self.q_num}: {self.question_data()}", font=("Press Start 2P", 20))

            canvas_tk.grid(row=1,column=0,padx=20)

    def buttons(self):
        frame = tk.Frame(width=self.green.width(), height=self.right_ph.height(), highlightthickness=0, bg=THEME_COLOR)
        wrong_bt = tk.Button(master=frame,image=self.wrong_ph, highlightthickness=0,
                             activebackground=THEME_COLOR, border=0, command=lambda : self.check_answer(False))

        right_bt = tk.Button(master=frame, image=self.right_ph, highlightthickness=0,
                             activebackground=THEME_COLOR, border=0, command=lambda : self.check_answer(True))
        frame.grid(row=2, column=0, pady=25)
        wrong_bt.grid(row=0, column=0, padx=25)
        right_bt.grid(row=0, column=1, padx=25)


    def question_data(self):
        self.q_num, quest_txt =self.quiz.next_question(self.q_num)
        return quest_txt
    def check_answer(self,answer):
        if self.current_q_num < len(self.quiz.question_list) -1:
            results = self.quiz.check_answer(answer)
            # print(results)
            if results:
                self.score_num += 1
                self.score_label()
                self.canvas()
                self.current_q_num += 1

            else:
                self.canvas()
                self.current_q_num += 1
        elif self.score_num == len(self.quiz.question_list) - 1:
            self.score_num += 1
            self.score_label()

