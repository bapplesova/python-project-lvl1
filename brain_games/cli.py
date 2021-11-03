#!/usr/bin/env python3


import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello,', name)
    return name


def ask(question):
    print(question)
    return input('Your answer: ')
