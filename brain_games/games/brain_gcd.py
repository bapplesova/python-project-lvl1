#!/usr/bin/env python3


from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_right_answer(num1, num2):
    min_num = min(num1, num2)
    for i in range(min_num, 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            return str(i)


def generate_round():
    min_possible_num = 1
    max_possible_num = 99
    num1 = randint(min_possible_num, max_possible_num)
    num2 = randint(min_possible_num, max_possible_num)
    question = str(num1) + ' ' + str(num2)
    return question, get_right_answer(num1, num2)
