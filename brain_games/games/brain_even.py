#!/usr/bin/env python3

from random import randint

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_right_answer(num):
    if num % 2 == 0:
        return 'yes'
    else:
        return 'no'


def generate_round():
    min_possible_num = 1
    max_possible_num = 99
    num = randint(min_possible_num, max_possible_num)
    return str(num), get_right_answer(num)
