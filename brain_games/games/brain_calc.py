#!/usr/bin/env python3

import operator
from random import randint, choice

DESCRIPTION = 'What is the result of the expression?'
OPERATORS = {'+': operator.add, '-': operator.sub,
             '*': operator.mul}


def get_right_answer(num1, num2, manipulation):
    necessary_func = OPERATORS.get(manipulation)
    return str(necessary_func(num1, num2))


def generate_round():
    min_possible_num = 1
    max_possible_num = 99

    num1 = randint(min_possible_num, max_possible_num)
    num2 = randint(min_possible_num, max_possible_num)
    manipulation = choice(list(OPERATORS.keys()))
    question = str(num1) + ' ' + str(manipulation) + ' ' + str(num2)
    right_answer = get_right_answer(num1, num2, manipulation)
    return question, right_answer
