#!/usr/bin/python3
"""Playing card."""

from string import Template

class Card(object):
    """Generates a card and its property accesors.

    Cards have a pip and a suit, it is the responsibility of the logic
    interpreter to determine the value of a Card.

    """
    # Class methods
    def __init__(self, pip, suit):
        """Generate a Card

        Args:
            pip: (String): The shown value of the card.
            suit: (String): The shown suit of the card.

        """
        self._pip = pip
        self._suit = suit
        self._hidden = False

        # Init to inherit classes
        super(Card, self).__init__()

    def __str__(self):
        """The representation of a Card.

        """
        tmp = Template("[$pip$suit]")
        if self._hidden:
            return tmp.substitute(pip='<', suit='>')

        return tmp.substitute(pip=self.pip, suit=self.suit)

    # Private methods
    def flip(self):
        """Flips a view state of a card.

        Returns:
            (Card): The card that was manipulated.

        """
        self._hidden = not self._hidden
        return self

    def peek(self, force=False):
        """ Return the visible string value of a card, when flipped the value
        must be forced.

        Args:
            force: (Boolean): True: Force the visibility of a hidden card.
            force: (Boolean): False: Do not force the visibility of a card.

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
        """Getter for card pip value.

        Returns:
            (char): The pip value.
            (boolean): False: The pip value is hidden.

        """
        if self._hidden:
            return False
        return self._pip

    @property
    def suit(self):
        """Getter for card suit value.

        Returns:
            (char): The suit value.
            (boolean):  The suit value is hidden.

        """
        if self._hidden:
            return False
        return self._suit
