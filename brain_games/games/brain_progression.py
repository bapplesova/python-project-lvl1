#!/usr/bin/env python3


from random import randint


def brain_progression():
    first_num = randint(1, 99)
    step = randint(1, 9)
    num_ind = randint(1, 10)
    progression = [first_num + step * i for i in range(10)]
    question = ''
    for i in range(10):
        if i == num_ind - 1:
            question += '.. '
            result = progression[i]
        else:
            question += str(progression[i]) + ' '
    return question, result
