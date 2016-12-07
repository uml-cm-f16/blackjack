#!/usr/bin/python3
""" A playing card.

"""

# IMPORTS

from string import Template

# CLASS

class Card(object):
    """ Generates a playing card that can be flipped over.

    Cards have a pip and a suit, it is the responsibility of the logic
    interpreter to determine the value of a Card.

    """
    # Class methods
    def __init__(self, pip, suit):
        """ Generate a Card

        Args:
            pip: (str): The shown value of the card.
            suit: (str): The shown suit of the card.

        Attributes:
            _pip: (str): The shown value of the card.
            _suit: (str): The shown suit of the card.
            _hidden: (bool): True: The card is flipped over with back visible
                             False: The card is value and suit are visible
        """
        self._pip = pip
        self._suit = suit
        self._hidden = False

        # Init to inherit classes
        super(Card, self).__init__()

    def __str__(self):
        """ The representation of a Card.

        Returns:
            (str): The string representation of a card [<>] | [$pip$suit]

        """
        tmp = Template("[$pip$suit]")
        if self._hidden:
            return tmp.substitute(pip='<', suit='>')

        return tmp.substitute(pip=self.pip, suit=self.suit)

    # Private methods
    def flip(self):
        """ Flips a view state of a card.

        Returns:
            (card): The card that was manipulated.

        """
        self._hidden = not self._hidden
        return self

    def peek(self, force=False):
        """ Return the visible string value of a card, when flipped the value
        must be forced.

        Args:
            force: (bool): True: Force the visibility of a hidden card.
            force: (bool): False: Do not force the visibility of a card.

        Returns:
            (str): The string representation of a card
        """
        flag = False

        if force and self._hidden:
            flag = True
            self._hidden = False

        str_self = str(self)

        if flag:
            self._hidden = True

        return str_self

    # Properties
    @property
    def pip(self):
        """ Getter for card pip value.

        Returns:
            (char): The pip value.
            (bool): False: The pip value is hidden.

        """
        if self._hidden:
            return False
        return self._pip

    @property
    def suit(self):
        """ Getter for card suit value.

        Returns:
            (char): The suit value.
            (bool): The suit value is hidden.

        """
        if self._hidden:
            return False
        return self._suit
