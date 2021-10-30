#!/usr/bin/env python
from brain_games.brain_games_develop import main_develop
from brain_games.games.brain_prime import brain_game


def main():
    desciption = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    main_develop(brain_game, desciption)


if __name__ == '__main__':
    main()
