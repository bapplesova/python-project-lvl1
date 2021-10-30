#!/usr/bin/env python3


from random import randint, choice


def brain_game():
    first_number = 1
    second_number = 99

    num1 = randint(first_number, second_number)
    num2 = randint(first_number, second_number)
    manipulation = choice(['+', '-', '*'])
    question = str(num1) + ' ' + str(manipulation) + ' ' + str(num2)
    right_answer = eval(question)
    return question, str(right_answer)
