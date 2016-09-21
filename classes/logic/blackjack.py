#!/usr/bin/python3

from .player import Player


class BlackJack(object):
    """
    """
    # Private Class Attributes
    _value = { "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10. "J": 10, "Q": 10, "K": 10, "A": 11}
    # Class methods
    def __init__(numPlayer = 1):
        self._numPlayer = numPlayer
        super(Blackjack, self).__init__()