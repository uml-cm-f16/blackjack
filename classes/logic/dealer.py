#!/usr/bin/python3

from .player import Player
from .deck import Deck

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
        self._deck = Deck()

        # Init to inherit classes
        super(Dealer, self).__init__()


    # Public methods
    def showDeck(self):
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

    def flip(self, card):
        """The dealer flips a card.

        Args:
            card: (Card): The card to flip.

        Returns:
            (Card): The card that was flipped.

        """
        return card.flip()

    # Properties
    @property
    def name(self):
        """The name given to a dealer.

        This method overides player.name for the dealer.

        Returns:
            (str): The name given to a dealer.

        """
        return 'Dealer'

    @property
    def isDealer(self):
        """If the player is a dealer.

        Overides the player.isDealer.

        Returns:
            (Boolean): False: A player is not a dealer.
            (Boolean): True: A player is a dealer.

        """
        return True