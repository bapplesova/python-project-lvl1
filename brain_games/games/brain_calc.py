#!/usr/bin/env python3

import operator
from random import randint, choice

DESCRIPTION = 'What is the result of the expression?'
OPERATORS = {'+': operator.add, '-': operator.sub,
             '*': operator.mul}


def calc(num1, num2, operation):
    necessary_func = OPERATORS.get(operation)
    return necessary_func(num1, num2)


def generate_round():
    min_possible_num = 1
    max_possible_num = 99

    num1 = randint(min_possible_num, max_possible_num)
    num2 = randint(min_possible_num, max_possible_num)
    operation = choice(list(OPERATORS.keys()))
    question = str(num1) + ' ' + str(operation) + ' ' + str(num2)
    right_answer = calc(num1, num2, operation)
    return question, str(right_answer)
