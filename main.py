#!/usr/bin/python3
""" Runs a black jack game using the Blackjack class

"""

# IMPORTS

from app.src.engine import Engine

# APPLICATION

def main():
    """ Kicks off a GUI Blackjack game

    """

    # Load and start pygame engine
    engine = Engine()
    engine.run()

# start main function
if __name__ == '__main__':
    main()
