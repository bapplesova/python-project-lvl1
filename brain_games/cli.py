#!/usr/bin/env python3


import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello,', name)
    return name


def greeter():
    print("Welcome to the Brain Games!")
