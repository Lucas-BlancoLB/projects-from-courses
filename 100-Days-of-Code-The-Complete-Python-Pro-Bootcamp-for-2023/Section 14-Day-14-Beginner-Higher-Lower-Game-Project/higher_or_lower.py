from art import logo
from art import vs
from game_data import data
from random import choice
from time import sleep
import os


def clear_terminal():
    os.system('clear')


def is_user_right(person_a, person_b, user_choice):
    if person_a['follower_count'] == person_b['follower_count']:
        print("U lucky bastard 😂")
        sleep(1)
        return 1
    if user_choice == 'a':
        if person_a['follower_count'] > person_b['follower_count']:
            return 1
        else:
            return 0
    else:
        if person_b['follower_count'] > person_a['follower_count']:
            return 1
        else:
            return 0


def higher_or_lower():
    score = 0
    person_a = choice(data)
    # print person A name, thier description, where their are from
    while True:
        print(logo)
        if score != 0:
            print(f"You're right! Score: {score}")
        print(f"A has:", str(person_a['follower_count']) + 'M followers')
        print("Compare A:", person_a['name'], person_a['description'], "from", person_a['country'])
        print(vs)
        # print person B name, thier description, where their are from
        person_b = choice(data)
        print(f"B has:", str(person_b['follower_count']) + 'M followers')
        print("Compare B:", person_b['name'], person_b['description'], "from", person_b['country'])

        # User input and correction
        while True:
            user_choice = input("Who has more followers? Type 'A' or 'B':").lower()[0]
            if user_choice in ('a', 'b'):
                clear_terminal()
                break

        answer_check = is_user_right(person_a, person_b, user_choice)
        if answer_check == 1:
            score += 1
            person_a = person_b
        else:
            print(logo, f"\nSorry, you're wrong. Score: {score}.")
            break


higher_or_lower()
while True:
    again = input("\nDo you wish to play higher again? type yes or no: ").lower()[0]
    if again == 'y':
        higher_or_lower()
    else:
        break

# def clear_then_logo():
#   clear()
#   print(logo)


# def compare_a_b(a_data, b_data, user_answer):
#   # if 1 A is higher else 0 A is Lower
#   if user_answer == 'a':
#     print("a_data['follower_count'] > b_data['follower_count']")
#     if a_data['follower_count'] > b_data['follower_count']:

#       return 1
#     else:
#       return 0
#   else:
#     print(b_data['follower_count'] > a_data['follower_count'])
#     if b_data['follower_count'] > a_data['follower_count']:
#       return 1
#     else: 
#       return 0


# def higher_or_lower():
#   score = 0
#   if score == 0:
#     print(logo)


#   a_data = choice(data)

#   # print(a_data)
#   print(f"Person A has: {a_data['follower_count']}")
#   print("Compare A:", a_data['name'], a_data['description'], "from",a_data['country'] )
#   while True:
#     b_data = choice(data)
#     print(vs)
#     print(f"Person B has: {b_data['follower_count']}")
#     print("Compare B:", b_data['name'], b_data['description'], "from",b_data['country'] )


#     while True:
#       user_answer = input("Who has more followers? Type 'A' or 'B': ").lower()[0]
#       if user_answer in ('a', 'b'): break
#     print(user_answer)

#     #compare function if 1 A is higher else 0 A is lower
#     user_value = compare_a_b(a_data, b_data, user_answer)
#     print(user_value)

#     clear()
#     if user_value == 1:
#       score += 1

#       # print(logo)
#       a_data = b_data
#       print(f"You are right, score: {score}")
#       print(f"Person A has: {a_data['follower_count']}")
#       print("Compare A:", a_data['name'], a_data['description'], "from",a_data['country'] )
#     if user_value == 0: break


# higher_or_lower()

