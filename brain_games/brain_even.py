#!/usr/bin/env python3


from random import randint


def brain_even(name):
    count_test = 0
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")
    while count_test < 3:
        num = randint(1, 1000)
        print('Question:', num)
        print('Your answer:', end='')
        answ = input().lower()
        if (answ == 'yes' and num % 2 == 0) or (answ == 'no' and num % 2 == 1):
            print('Correct!')
            count_test += 1
        else:
            print("Let's try again, " + name + '!')
            count_test = 4
    if count_test == 3:
        print('Congratulations, ' + name + '!')
