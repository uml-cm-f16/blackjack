#!/usr/bin/python3
""" Defines a card dealer.

    A Card dealer is a player that manages the deck.

"""

# IMPORTS

from .player import Player
from .deck import Deck

# CLASS

class Dealer(Player):
    """ A card dealer.

    A player that also can deal cards.

    """
    # Class methods
    def __init__(self):
        """ Creates a dealer.

        Attributes:
            _id: (int): Overrides the players number to that of a dealer.
            _deck: (deck): Deck of cards.

        """
        # Remove dealer from player count
        Player._player_counter -= 1
        self._id = -1

        self._deck = Deck()

        # Init to inherit classes
        super().__init__()

    # Public methods
    def show_deck(self, state=False):
        """ Shows the deck of cards.

        Args:
            state: (bool): False: Show the deck in hidden state
            state: (bool): True: Show the deck in visible state

        """
        return self._deck.show(state)

    def shuffle(self):
        """ Shuffles the deck of cards.

        """
        self._deck.shuffle()

    def draw(self):
        """ Retrieves a card from the top of the deck.

        Returns:
            (card): The top card of the deck.
        """
        return self._deck.draw()

    def burn(self, cards):
        """ Returns cards to the bottom of the deck.

        Args:
            cards: (list (card)): The cards to return.

        """
        self._deck.burn(cards)

    def flip_deal(self, card):
        """ The dealer flips a card.

        Args:
            card: (card): The card to flip.

        Returns:
            (card): The card that was flipped.

        """
        return card.flip()

    @property
    def deck_stats(self):
        """ Returns a decks stats dictionary

        Returns:
            (dict): The key count left in the deck.

        """
        return self._deck.deck_stats
