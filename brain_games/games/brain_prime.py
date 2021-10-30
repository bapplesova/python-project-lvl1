#!/usr/bin/env python3


from random import randint


def brain_game():
    first_number = 1
    second_number = 99

    num = randint(first_number, second_number)
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return str(num), 'no'
    return str(num), 'yes'
