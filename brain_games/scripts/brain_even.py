#!/usr/bin/env python

from brain_games.brain_games_develop import main_develop
from brain_games.games.brain_even import brain_game


def main():
    description = 'Answer "yes" if the number is even, otherwise answer "no".'

    main_develop(brain_game, description)


if __name__ == '__main__':
    main()
