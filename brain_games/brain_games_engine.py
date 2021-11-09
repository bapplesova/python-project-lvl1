#!/usr/bin/env python

from brain_games.cli import welcome_user, ask

TOTAL_COUNT_ROUNDS = 3


def run_engine(game):
    print("Welcome to the Brain Games!")
    user_name = welcome_user()
    print(game.DESCRIPTION)
    for i in range(TOTAL_COUNT_ROUNDS):
        question, right_answer = game.generate_round()
        user_answer = ask(question)

        if right_answer == str(user_answer).lower():
            print('Correct!')
        else:
            print("'" + str(user_answer) + "' is a wrong answer ;(.", end='')
            print(" Correct answer was '" + right_answer + "'")
            print("Let's try again, " + user_name + '!')
            return
    else:
        print('Congratulations, ' + user_name + '!')
