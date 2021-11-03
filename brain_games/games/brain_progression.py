#!/usr/bin/env python3


from random import randint

DESCRIPTION = 'What number is missing in the progression?'


def get_question_answer(progression, hidden_index):
    question = ''
    for i in range(len(progression)):
        if i == hidden_index - 1:
            question += '.. '
            result = str(progression[i])
        else:
            question += str(progression[i]) + ' '
    return question, result


def generate_round():
    min_possible_num = 1
    max_possible_num = 99
    max_step = 9
    progression_length = 10

    first_num = randint(min_possible_num, max_possible_num)
    step = randint(1, max_step)
    hidden_index = randint(1, progression_length)
    progression = [first_num + step * i for i in range(progression_length)]
    return get_question_answer(progression, hidden_index)
