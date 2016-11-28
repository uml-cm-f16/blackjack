#!/usr/bin/python3
"""A deck of cards."""

from random import shuffle, randint
from decimal import Decimal, ROUND_HALF_UP
from .card import Card

class Deck(object):
    """A deck of cards and actions.

    A standard deck consists of 52 Cards from 2 - A of K, H, D, and S suits. This
    class allows for multiple decks to be used alongside a marker card to signify
    shuffling.

    Attributes:
        _pips: (List): The list of pips to use.
        _suits: (List): The list of suits to use.
        _marker: (Card): The marker card used to signify reshuffle point.

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

        for _ in range(0, self._qty):
            for suit in self.__class__._suits:
                for pip in self.__class__._pips:
                    self._insert(Card(pip, suit))
        # Init to inherit classes
        super(Deck, self).__init__()

    def __str__(self):
        """The str representation of a Deck.

        """
        return ', '.join(str(card) for card in self._deck)

    # Private methods
    def _insert(self, card, position=0):
        """Adds a card to the deck.

        Args:
            card: (Card): The card to add to the deck.
            position: (int): 0: The index position of insertion.

        """
        self._incCount(card)
        card.flip()
        self._deck.insert(position, card)

    def _incCount(self, card):
        """Increments the pip count

        Args:
            card: (Card): The card pip to increment.

        """
        flag = False
        if card.pip == False:
            flag = True
            card.flip()
        self._count[card.pip] = self._count.get(card.pip, 0) + 1
        if flag:
            card.flip()

    def _decCount(self, card):
        """Decrements the pip count

        Args:
            card: (Card): The card pip to decrement.

        """
        flag = False
        if card.pip is False:
            flag = True
            card.flip()
        self._count[card.pip] = self._count.get(card.pip, 0) - 1
        if flag:
            card.flip()
    def _has(self, card):
        """Checks to see if card is in the deck.

        Args:
            card: (Card): The card to look for.

        Returns:
            (Boolean): True: The card was found in the deck.
            (Boolean): False: The card was not found in the deck.

        """
        return self._deck.count(card) > 0

    def _remove(self, card):
        """Removes a card from the deck.

        Args:
            card: (Card): The card to remove.

        Returns:
            (Boolean): True: Succesful operation status.
            (Boolean): False: Failed operation status.

        """
        count = self._deck.count(card)
        if count > 0:
            # Card count in deck is wrong
            if self._count[card.pip] <= 0:
                return False
            # Update card.pip counter
            self._decCount(card)
            if count - 1 == self._deck.count(card):
                self._deck.remove(card)
                return True
        return False

    def _pop(self):
        """Retrieve a card from the top of the deck.

        Returns:
            (Card): The card that was retrieved.
            (Boolean): False: The deck is empty.

        """
        if self._deck:
            card = self._deck.pop()
            # Update card.pip counter
            self._decCount(card)
            return card
        return False

    def _mark(self, r_flag=False):
        """Marks a position in the deck to signal reshuffle.

        Args:
            r_flag: (Boolean): False: Marker is placed at bottom of deck.
            r_flag: (Boolean): True: Randomize the location of the marker.

        """
        # Remove marker if in deck
        if self._has(self.__class__._marker):
            self._remove(self.__class__._marker)

        # Add marker to deck
        if r_flag:
            position = randint(0, len(self._deck))
            self._insert(self.__class__._marker, position)
        else:
            self._insert(self.__class__._marker)

    # Public methods
    def shuffle(self, mark=False, r_flag=True):
        """Shuffles a deck of cards.

        Has the capability of marking the next shuffle point randomly or once
        all cards have been used.

        Args:
            mark: (Boolean): True: Mark a deck.
                            False: Do not mark a deck.
            r_flag: (Boolean): True: Randomly mark deck.
                            False: Mark bottom of deck.

        """
        shuffle(self._deck)
        if mark:
            self._mark(r_flag)

    def show(self, force=False):
        """Shows the deck of cards.

        Args:
            force: (Boolean): True: Forces visibility of the cards.
                            False: Shows the cards in their natural state.

        """
        if force:
            return ', '.join(card.peek(force) for card in self._deck)
        else:
            return self._deck


    def draw(self):
        """Retrieves a card from the top of the deck.

        Returns:
            (Card): The card that was retrieved.
            (Boolean): False: The deck is empty.

        """
        return self._pop()

    def burn(self, cards):
        """Return a used card to the deck.

        Args:
            card: (Card): The card to return.

        """
        if isinstance(cards, Card):
             self._insert(cards)
        if isinstance(cards, list):
            for card in cards:
                self._insert(card)


    # Properties
    @property
    def marker(self):
        """Returns a marker for comparison.

        Returns:
            (Card): The marker card

        """
        return self._marker

    def percent(self, lst, values):
        """Percentage chance to win from next card.

        Args:
            lst: (list): A list of cards that will win the hand.

        Returns:
            (float): The percentage to win off next card.

        """
        def winnable_cards(key, score):
            if key is False:
                return 0
            if self.possible_win(Card(key, '-'), values, 21, score) is True:
                return self._count[key]
            return 0


        score = 0
        for card in lst:
            score = self.total(score, card, values)

        total_winable_cards = 0
        for k in self._count.keys():
            total_winable_cards = total_winable_cards + winnable_cards(k, score)

        total_playable_cards = sum(self._count.values())

        tmp = Decimal(100 * total_winable_cards/ total_playable_cards)
        return float(Decimal(tmp.quantize(Decimal('.001'), rounding=ROUND_HALF_UP)))

    def possible_win(self, card, values, score_max, score):
        """ checks if the core otutcomes leads to a winabel value.
        """
        winnable = False
        def map_win(s):
            """
            checks if any of the leaves are wins
            """
            nonlocal winnable
            if winnable is True:
                return
            elif isinstance(s, list):
                [map_win(i) for i in s]
            elif s <= score_max:
                winnable = True
            else:
                return

        map_win(self.total(score, card, values))

        return winnable

    def total(self, score, card, values):
        """ get possible totals.
        """
        def get_val(val):
            if isinstance(values[card.pip], list):
                return [elem + val for elem in values[card.pip]]
            return values[card.pip] + val

        if isinstance(score, list):
            return [self.total(i, card, values) for i in score]
        return get_val(score)






