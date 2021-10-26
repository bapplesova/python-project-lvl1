#!/usr/bin/env python3


from random import randint


def brain_even():
    num = randint(1, 99)
    question = 'Question: ' + str(num)
    if num % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return question, right_answer
