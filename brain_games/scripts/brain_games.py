#!/usr/bin/env python

from brain_games.cli import welcome_user
from brain_games.games.brain_even import brain_even
from brain_games.games.brain_calc import brain_calc
from brain_games.games.brain_gcd import brain_gcd
from brain_games.games.brain_progression import brain_progression
from brain_games.games.brain_prime import brain_prime


def main():
    print("Welcome to the Brain Games!")
    user_name = welcome_user()
    print("Choose a game for playing: 1: even 2: calc 3: gcd 4: progression 5: prime ")
    game_id = int(input())
    count_test = 0
    if count_test == 0 and game_id == 1:
        print("Answer 'yes' if the number is even, otherwise answer 'no'.")
    elif count_test == 0 and game_id == 2:
        print("What is the result of the expression?")
    elif count_test == 0 and game_id == 3:
        print("Find the greatest common divisor of given numbers.")
    elif count_test == 0 and game_id == 4:
        print("What number is missing in the progression?")
    elif count_test == 0 and game_id == 5:
        print('Answer "yes" if given number is prime. Otherwise answer "no".')

    while count_test < 3:
        if game_id == 1:
            question, right_answer = brain_even()
        elif game_id == 2:
            question, right_answer = brain_calc()
        elif game_id == 3:
            question, right_answer = brain_gcd()
        elif game_id == 4:
            question, right_answer = brain_progression()
        elif game_id == 5:
            question, right_answer = brain_prime()

        print(question)
        user_answer = input('Your answer:')

        if str(right_answer) == str(user_answer).lower():
            print('Correct!')
            count_test += 1
        else:
            print("" + str(user_answer) + "' is wrong answer ;(.", end='')
            print(" Correct answer was '" + str(right_answer) + "'")
            print("Let's try again, " + user_name + '!')
            count_test = 4

    if count_test == 3:
        print('Congratulations, ' + user_name + '!')


if __name__ == '__main__':
    main()
