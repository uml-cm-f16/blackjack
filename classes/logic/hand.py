#!/usr/bin/python3

class Hand(object):
    """A hand of cards.

    """
    # Class methods
    def __init__(self):
        """Generates an empty hand of cards.

        """
        self._hand = []

        # Init to inherit classes
        super(Hand, self).__init__()

    def __str__(self):
        """The string representation of a Hand.

        Returns:
            (str): A string representation of a hand.

        """
        return ", ".join(str(card) for card in self._hand)

    # Private methods
    def _has(self, card):
        """Checks to see if card is in the hand.

        Args:
            card: (Card): The card to look for.

        Returns:
            (Boolean): True: The card was found in the hand.
            (Boolean): False: The card was not found in the hand.

        """
        return self._hand.count(card) > 0

    # Public methods
    def add(self, card):
        """Add a card to the hand.

        Args:
            card: (card): The card to add tp the hand.
        """
        self._hand.append(card)

    def remove(self, card):
        """Remove a card from the hand.import

        Returns:
            (Boolean): True: The card was removed.
            (Boolean): False: The card was not removed.

        """
        if self._has(card):
            self._hand.remove(card)
            return True
        return False

    def fold(self):
        """Folds a hand of cards.

        Returns:
            (Card ...): The cards in the hand.

        """
        cards = self._hand
        self._hand = []
        return cards

