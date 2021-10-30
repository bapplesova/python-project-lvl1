#!/usr/bin/env python3

from random import randint


def brain_game():
    first_number = 1
    second_number = 99
    num = randint(first_number, second_number)
    if num % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return str(num), right_answer
