from data import question_data, question_data_2
from quiz_brain import QuizBrain
from question_model import Question
from random import shuffle

is_game_on = True

question_bank = list()
shuffle(question_data)
for i in range(len(question_data_2["results"])):
    value = question_data_2['results'][i]['question']
    response = question_data_2['results'][i]["correct_answer"]
    question_data.append({"text": value, "answer": response})


for i in question_data:
    question_bank.append(Question(i['text'],i['answer']))


quiz_brain = QuizBrain(question_bank)

while is_game_on:
    if quiz_brain.check_for_end_of_quiz():
        print(f"\nSCORE: {quiz_brain.user_score()}\n{quiz_brain.score_brain()}")
        is_game_on = False
    else:
        answer = quiz_brain.question_module()
        if answer:
            print('You got it right!')
        else:
            print(f"It was {quiz_brain.current_answer}")
