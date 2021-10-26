#!/usr/bin/env python3


from random import randint


def brain_gcd():
    num1 = randint(1, 99)
    num2 = randint(1, 99)
    gcd = min(num1, num2)
    question = 'Question: ' + str(num1) + ' ' + str(num2)
    while gcd != 0:
        if num1 % gcd == 0 and num2 % gcd == 0:
            return question, gcd
        else:
            gcd -= 1
