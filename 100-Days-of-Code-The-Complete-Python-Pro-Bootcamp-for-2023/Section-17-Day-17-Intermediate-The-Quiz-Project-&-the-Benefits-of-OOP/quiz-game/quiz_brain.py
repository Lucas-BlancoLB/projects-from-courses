class QuizBrain:

    def __init__(self, q_bank):
        self.q_number = 0
        self.q_list = q_bank
        self.score = 0
        self.current_answer = ''

    def question_module(self):

        question_approach = self.q_list[self.q_number]
        while True:
            self.current_answer = question_approach.answer
            user_input = input(f"Q.{self.q_number + 1}: {question_approach.text} (True/False): ").capitalize()
            if user_input == 'T': user_input = 'True'
            elif user_input == "F": user_input = "False"
            if user_input in ('True', 'False'): break
        self.q_number += 1

        if user_input.lower() == question_approach.answer.lower():
            self.score += 1
            return True
        else: return False


    def check_for_end_of_quiz(self):
        return self.q_number > len(self.q_list)- 1


    def user_score(self):
        return str(f"{self.score}/{self.q_number}")


    def score_brain(self):
        if (self.score / self.q_number) == 1:
            return "congrats champ, u won. 🦈"
        elif (self.score / self.q_number) >= 0.75:
            return  "It was almost there champ, did great.🗿"
        elif (self.score / self.q_number) >= 0.50:
            return "damn you're on the line, could do better. 🤧"
        elif (self.score / self.q_number) >= 0.25:
            return "Dud u suck, that was so bad. 💀"
        else:
            return "If you are playing like that, failure may be your style. 😎"



