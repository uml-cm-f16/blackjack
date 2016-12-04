#!/usr/bin/python3
""" Defines a card dealer.

    A Card dealer is a player that manages the deck.

"""

# Import the player base class of the dealer
from .player import Player

# Importing the deck class
from .deck import Deck

# Defining the dealer
class Dealer(Player):
    """A card dealer.

    A player that also can deal cards.

    """
    # Class methods
    def __init__(self):
        """Creates a dealer.

        Attributes:
            _deck: (Deck): Deck of cards.

        """
        self._id = -1

        # Remove dealer from player count
        Player._player_counter -= 1

        self._deck = Deck()

        # Init to inherit classes
        super(Dealer, self).__init__()

    # Public methods
    def show_deck(self):
        """Shows the deck of cards.

        """

        self._deck.show(True)

    def shuffle(self):
        """Shuffles the deck of cards.

        Returns:
            (Deck): A shuffled deck.
        """
        return self._deck.shuffle()

    def draw(self):
        """Retrieves a card from the top of the deck.

        Returns:
            (Card): The top card of the deck.
        """
        return self._deck.draw()

    def burn(self, cards):
        """Returns cards to the bottom of the deck.

        Args:
            cards: [Card, ...]: The cards to return.

        """
        self._deck.burn(cards)

    def flip_deal(self, card):
        """The dealer flips a card.

        Args:
            card: (Card): The card to flip.

        Returns:
            (Card): The card that was flipped.

        """
        return card.flip()

    @property
    def deck_stats(self):
        """ Returns a decks stats dictionary

        Returns:
            (Dictionary)    The amount of cards left in the deck of each suit.
        """
        return self._deck.deck_stats
