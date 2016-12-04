#!/usr/bin/python3
"""A player."""

from string import Template

from .hand import Hand

class Player(Hand):
    """An individual player in the game.

    A player is identifiable and holds a hand of cards.

    Attributes:
        _number: (int): The number of players.

    """
    # Private Class Attributes
    _player_counter = 0

    # Class methods
    def __init__(self):
        """Initializes a player

        Generates a player name, and initializes a hand.

        """

        #Generate player number
        self._id = Player._player_counter

        # Increment player number
        Player._player_counter += 1

        # Init to inherit classes
        super(Player, self).__init__()

    # Properties
    @property
    def number(self):
        """The identifying name of the player.

        Returns:
            (str): The player identifier.

        """
        return self._id
