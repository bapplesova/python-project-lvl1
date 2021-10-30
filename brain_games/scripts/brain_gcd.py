#!/usr/bin/env python
from brain_games.brain_games_develop import main_develop
from brain_games.games.brain_gcd import brain_game


def main():
    description = 'Find the greatest common divisor of given numbers.'
    main_develop(brain_game, description)


if __name__ == '__main__':
    main()
