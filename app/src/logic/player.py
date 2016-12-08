#!/usr/bin/python3
""" A card player

"""

# IMPORTS

from .hand import Hand

# CLASS

class Player(Hand):
    """ An individual card player.

    A player is identifiable and holds a hand of cards.

    Attributes:
        _number: (int): The number of players.

    """
    # Private Class Attributes
    _player_counter = 0

    def __init__(self, reset=False):
        """ Initializes a player

        Generates a player name, and initializes a hand.

        Args:
            reset: (bool): False: Used by test class to test counter

        """
        if reset:
            Player._player_counter = 0

        #Generate player number
        self._id = Player._player_counter

        # Increment player number
        Player._player_counter += 1

        # Init to inherit classes
        super().__init__()

    # Public properties
    @property
    def number(self):
        """ The identifying name of the player.

        Returns:
            (intstr): The player identifier.

        """
        return self._id
