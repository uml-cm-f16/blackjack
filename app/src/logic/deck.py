#!/usr/bin/python3
""" A deck of playing cards.

"""

# IMPORTS

from random import shuffle, randint

from .card import Card

# CLASS

class Deck(object):
    """ A deck of playing cards.

    A standard deck consists of 52 Cards from 2 - A of K, H, D, and S suits. This
    class allows for multiple decks to be used alongside a marker card to signify
    shuffling points.

    Attributes:
        _pips: (list): The list of pips to use.
        _suits: (list): The list of suits to use.
        _marker: (card): The marker card used to signify reshuffle point.

    """
    # Private Class Attributes
    _pips = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    _suits = ['H', 'S', 'D', 'C']
    _marker = Card('-', '-')

    # Class methods
    def __init__(self, qty=1):
        """ Creates deck.

        Attributes:
            _qty: (int): Number of decks to generate.
            _deck: (int): The deck of cards.
            _count: (int): The number of cards of the pip value still in the deck.

        Args:
            qty: (int): The number of decks to include.

        """
        self._qty = qty
        self._deck = []
        self._count = dict()

        # Build deck
        for _ in range(0, self._qty):
            for suit in Deck._suits:
                for pip in Deck._pips:
                    self._insert(Card(pip, suit))

        # Init to inherit classes
        super().__init__()

    def __str__(self):
        """ The str representation of a Deck.

        Returns:
            (str): The string representation of a deck

        """
        return self.show()

    # Private methods
    def _insert(self, card, position=0):
        """ Adds a card to the deck.

        Args:
            card: (card): The card to add to the deck.
            position: (int): 0: The index position of insertion.

        """
        self._inc_count(card)

        # False is the hidden state
        if not card.pip is False:
            card.flip()

        self._deck.insert(position, card)

    def _inc_count(self, card):
        """ Increments the pip count

        Args:
            card: (card): The card pip to increment.

        """
        pip = card.pip

        # If card was facedown flip to see pip
        if pip is False:
            card.flip()
            pip = card.pip
            card.flip()

        # Increment card
        self._count[pip] = self._count.get(pip, 0) + 1

    def _dec_count(self, card):
        """ Decrements the pip count

        Args:
            card: (Card): The card pip to decrement.

        """
        pip = card.pip

        # If card was facedown flip to see pip
        if pip is False:
            card.flip()
            pip = card.pip
            card.flip()

        self._count[pip] = self._count.get(pip, 0) - 1

    def _has(self, card):
        """ Checks to see if card is in the deck.

        Args:
            card: (card): The card to look for.

        Returns:
            (bool): True: The card was found in the deck.
            (bool): False: The card was not found in the deck.

        """
        return self._deck.count(card) > 0

    def _remove(self, card):
        """ Removes a card from the deck.

        Args:
            card: (card): The card to remove.

        Returns:
            (bool): True: Successful operation status.
            (bool): False: Failed operation status.

        """
        count = self._deck.count(card)
        if count > 0:
            # Card count in deck is wrong
            if self._count[card.pip] <= 0:
                return False
            # Update card.pip counter
            self._dec_count(card)
            if count - 1 == self._deck.count(card):
                self._deck.remove(card)
                return True
        return False

    def _pop(self):
        """ Retrieve a card from the top of the deck.

        Returns:
            (card): The card that was retrieved.
            (bool): False: The deck is empty.

        """
        if self._deck:
            card = self._deck.pop()
            # Update card.pip counter
            self._dec_count(card)
            return card
        return False

    def _mark(self, r_flag=False):
        """Marks a position in the deck to signal reshuffle.

        Args:
            r_flag: (bool): False: Marker is placed at bottom of deck.
            r_flag: (bool): True: Randomize the location of the marker.

        """
        # Remove marker if in deck
        if self._has(Deck._marker):
            self._remove(Deck._marker)

        # Add marker to deck
        if r_flag:
            position = randint(0, len(self._deck))
            self._insert(Deck._marker, position)
        else:
            self._insert(Deck._marker)

    # Public methods
    def shuffle(self, mark=False, r_flag=False):
        """ Shuffles a deck of cards.

        Has the capability of marking the next shuffle point randomly or once
        all cards have been used.

        Args:
            mark: (bool): True: Mark a deck.
            r_flag: (bool): True: Randomly mark deck.

        """
        shuffle(self._deck)

        if mark:
            self._mark(r_flag)

    def show(self, force=False):
        """ Shows the deck of cards.

        Args:
            force: (bool): True: Forces visibility of the cards.

        Returns:
            (str): The deck representation
        """
        if force:
            return ', '.join(card.peek(force) for card in self._deck)

        return ', '.join(card.peek() for card in self._deck)


    def draw(self):
        """ Retrieves a card from the top of the deck.

        Returns:
            (card): The card that was retrieved.
            (bool): False: The deck is empty.

        """
        return self._pop()

    def burn(self, cards):
        """ Return a used card to the deck.

        Args:
            card: (card): The card to return.

        """
        if isinstance(cards, Card):
            self._insert(cards)
        elif isinstance(cards, list):
            for card in cards:
                self._insert(card)

    # Properties
    @property
    def marker(self):
        """ Returns a marker for comparison.

        Returns:
            (card): The marker card

        """
        return self._marker

    @property
    def deck_stats(self):
        """ The list of pip counts

        Returns:
            self._count: (dict):    The dictionary of pip counts

        """
        return self._count
