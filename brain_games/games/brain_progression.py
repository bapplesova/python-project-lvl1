#!/usr/bin/env python3


from random import randint


def brain_game():
    first_number = 1
    second_number = 99
    max_step = 9
    progression_length = 10

    first_num = randint(first_number, second_number)
    step = randint(first_number, max_step)
    num_ind = randint(first_number, progression_length)
    progression = [first_num + step * i for i in range(10)]
    question = ''

    for i in range(progression_length):
        if i == num_ind - 1:
            question += '.. '
            result = str(progression[i])
        else:
            question += str(progression[i]) + ' '
    return question, result
