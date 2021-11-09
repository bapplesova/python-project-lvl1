#!/usr/bin/env python3

from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True


def generate_round():
    min_possible_num = 1
    max_possible_num = 99

    num = randint(min_possible_num, max_possible_num)
    if is_prime(num) is True:
        return str(num), 'yes'
    else:
        return str(num), 'no'
