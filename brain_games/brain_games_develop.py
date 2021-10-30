#!/usr/bin/env python

from brain_games.cli import greeter, welcome_user


def main_develop(game, description):
    all_rounds = 3
    current_test = 0

    greeter()
    user_name = welcome_user()

    if current_test == 0:
        print(description)

    while current_test < all_rounds:
        question, right_answer = game()

        print('Question:', question)
        user_answer = input('Your answer: ')

        if right_answer == str(user_answer).lower():
            print('Correct!')
            current_test += 1
        else:
            print("'" + str(user_answer) + "' is wrong answer ;(.", end='')
            print(" Correct answer was '" + right_answer + "'")
            print("Let's try again, " + user_name + '!')
            return

    if current_test == 3:
        print('Congratulations, ' + user_name + '!')
