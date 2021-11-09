#!/usr/bin/env python3

from random import randint

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    return num % 2 == 0


def generate_round():
    min_possible_num = 1
    max_possible_num = 99
    num = randint(min_possible_num, max_possible_num)
    if is_even(num) is True:
        return str(num), 'yes'
    else:
        return str(num), 'no'
