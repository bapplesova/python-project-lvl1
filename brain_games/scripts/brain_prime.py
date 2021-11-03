#!/usr/bin/env python
from brain_games.brain_games_engine import main_engine
from brain_games.games.brain_prime import generate_round


def main():
    main_engine(generate_round)


if __name__ == '__main__':
    main()
