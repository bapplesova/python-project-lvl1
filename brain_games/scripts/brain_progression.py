#!/usr/bin/env python
from brain_games.brain_games_develop import main_develop
from brain_games.games.brain_progression import brain_game


def main():
    description = 'What number is missing in the progression?'
    main_develop(brain_game, description)


if __name__ == '__main__':
    main()
