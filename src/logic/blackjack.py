#!/usr/bin/python3
"""A Blackjack player."""

from .player import Player

class BlackJack(object):
    """BlackJack rule set for dealer.

    """
    # Private Class Attributes
    _value = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
              "T": 10, "J": 10, "Q": 10, "K": 10, "A": 11}

    # Class methods
    def __init__(self, num_player=1):
        self._numPlayer = num_player
        super(Blackjack, self).__init__()