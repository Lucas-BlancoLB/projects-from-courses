import html
class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self, q_num):
        self.current_question = self.question_list[q_num]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)

        return  self.question_number, q_text


    def check_answer(self, user_answer):

        if str(user_answer) == self.current_question.answer:
            self.score += 1
            return True
        else:
            return  False
