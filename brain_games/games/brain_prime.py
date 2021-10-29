#!/usr/bin/env python3


from random import randint


def brain_prime():
    num = randint(1, 100)
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return num, 'no'
    return num, 'yes'
