#!/usr/bin/python3
""" Runs a black jack game using the Blackjack class

"""

from src.pygame.display_engine import Display_Engine

def main():
    """ main

    """
    # Load and start pygame engine
    engine = Display_Engine()
    engine.run()


if __name__ == '__main__':
    main()
