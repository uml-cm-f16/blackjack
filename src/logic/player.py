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
    _number = 0

    # Class methods
    def __init__(self):
        """Initializes a player

        Generates a player name, and initializes a hand.

        """
        if not self.isDealer:
            # Generate player number
            self.__class__._number += 1
            self._number = self.__class__._number

        # Init to inherit classes
        super(Player, self).__init__()

    # Properties
    @property
    def name(self):
        """The identifying name of the player.

        Returns:
            (str): The player identifier.

        """
        tmp = Template("P_$num")
        return tmp.substitute(num=self._number)

    @property
    def isDealer(self):
        """If the player is a dealer.

        Returns:
            (Boolean): False: A player is not a dealer.
            (Boolean): True: A player is a dealer.

        """
        return False
