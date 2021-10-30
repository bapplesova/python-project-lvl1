#!/usr/bin/env python3


from random import randint


def brain_game():
    first_number = 1
    second_number = 99

    num1 = randint(first_number, second_number)
    num2 = randint(first_number, second_number)
    gcd = min(num1, num2)
    question = str(num1) + ' ' + str(num2)
    while gcd != 0:
        if num1 % gcd == 0 and num2 % gcd == 0:
            return question, str(gcd)
        else:
            gcd -= 1
