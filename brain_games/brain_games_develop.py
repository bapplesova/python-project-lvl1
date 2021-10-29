#!/usr/bin/env python

from brain_games.cli import greeter, welcome_user
from brain_games.games.brain_even import brain_even
from brain_games.games.brain_calc import brain_calc
from brain_games.games.brain_gcd import brain_gcd
from brain_games.games.brain_progression import brain_progression
from brain_games.games.brain_prime import brain_prime


def main_develop(game_id):
    task = ['Answer "yes" if the number is even, otherwise answer "no".',
            'What is the result of the expression?',
            'Find the greatest common divisor of given numbers.',
            'What number is missing in the progression?',
            'Answer "yes" if given number is prime. Otherwise answer "no".']
    module = ['brain_even()', 'brain_calc()', 'brain_gcd()',
              'brain_progression()', 'brain_prime()']

    count_test = 0

    greeter()
    user_name = welcome_user()

    if count_test == 0:
        print(task[game_id - 1])

    while count_test < 3:
        question, right_answer = eval(module[game_id - 1])

        print('Question:', question)
        user_answer = input('Your answer: ')

        if str(right_answer) == str(user_answer).lower():
            print('Correct!')
            count_test += 1
        else:
            print("'" + str(user_answer) + "' is wrong answer ;(.", end='')
            print(" Correct answer was '" + str(right_answer) + "'")
            print("Let's try again, " + user_name + '!')
            count_test = 4

    if count_test == 3:
        print('Congratulations, ' + user_name + '!')
