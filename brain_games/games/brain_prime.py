#!/usr/bin/env python3


from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_right_answer(num):
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return 'no'
    return 'yes'


def generate_round():
    min_possible_num = 1
    max_possible_num = 99

    num = randint(min_possible_num, max_possible_num)
    return str(num), get_right_answer(num)
