#!/usr/bin/env python3


from random import randint, choice


def brain_calc():
    num1 = randint(1, 99)
    num2 = randint(1, 99)
    manipulation = choice(['+', '-', '*'])
    question = str(num1) + str(manipulation) + str(num2)
    right_answer = eval(question)
    return question, right_answer
