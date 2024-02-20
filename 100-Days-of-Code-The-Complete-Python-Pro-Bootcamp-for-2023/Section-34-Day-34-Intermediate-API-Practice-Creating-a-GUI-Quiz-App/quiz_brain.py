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
        # user_answer = input(f"Q.{self.question_number}: {q_text} (True/False): ")
        return  self.question_number, q_text
        # self.check_answer(user_answer)

    def check_answer(self, user_answer):
        correct_answer = bool(self.current_question.answer)
        print(user_answer, correct_answer)
        if bool(user_answer) == correct_answer:
            print(1)
            self.score += 1
            return True
        else:
            print(2)
            return  False

        # print(f"Your current score is: {self.score}/{self.question_number}")
        # print("\n")
