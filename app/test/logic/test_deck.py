#!/usr/bin/python3
"""This module tests the Deck class."""

import unittest

from app.src.logic.card import Card

# Importing class to test
from app.src.logic.deck import Deck

class Test_Deck(unittest.TestCase):
    """ Tests the Deck class methods.

    """
    # The expected order of cards
    fifty_two_cards_visible = ("[AC], [KC], [QC], [JC], [TC], [9C], [8C], [7C], "
                               "[6C], [5C], [4C], [3C], [2C], [AD], [KD], [QD], "
                               "[JD], [TD], [9D], [8D], [7D], [6D], [5D], [4D], "
                               "[3D], [2D], [AS], [KS], [QS], [JS], [TS], [9S], "
                               "[8S], [7S], [6S], [5S], [4S], [3S], [2S], [AH], "
                               "[KH], [QH], [JH], [TH], [9H], [8H], [7H], [6H], "
                               "[5H], [4H], [3H], [2H]")

    # The hidden expected order of cards
    fifty_two_cards_hidden = ("[<>], [<>], [<>], [<>], [<>], [<>], [<>], [<>], "
                              "[<>], [<>], [<>], [<>], [<>], [<>], [<>], [<>], "
                              "[<>], [<>], [<>], [<>], [<>], [<>], [<>], [<>], "
                              "[<>], [<>], [<>], [<>], [<>], [<>], [<>], [<>], "
                              "[<>], [<>], [<>], [<>], [<>], [<>], [<>], [<>], "
                              "[<>], [<>], [<>], [<>], [<>], [<>], [<>], [<>], "
                              "[<>], [<>], [<>], [<>]")

    # To allow large character comparisons
    maxDiff = None

    def test_str_representation(self):
        """ A decks string representation

        """

        # A default deck of 1
        self.assertEqual(str(Deck()),
                         self.__class__.fifty_two_cards_hidden)

        # An empty deck
        self.assertEqual(str(Deck(0)),
                         "")

        # A single deck of 52 cards
        deck_one = Deck(1)

        self.assertEqual(str(deck_one),
                         self.__class__.fifty_two_cards_hidden)

        self.assertEqual(str(deck_one.show(True)),
                         self.__class__.fifty_two_cards_visible)

        # A double deck of 104 cards
        self.assertEqual(str(Deck(2)), self.__class__.fifty_two_cards_hidden +
                         ', ' + self.__class__.fifty_two_cards_hidden)

    def test_shuffle(self):
        """ Test that a deck was shuffled. This test is not perfect because of
        the chance a shuffled deck can shuffle back into the same order 1 out of
        52! times.

        """
        # A deck can be created
        deck_untampered = Deck(1)
        deck_one = Deck(1)

        # Two deck are created equally
        self.assertEqual(str(deck_untampered.show(True)),
                         self.__class__.fifty_two_cards_visible)
        self.assertEqual(str(deck_one.show(True)),
                         self.__class__.fifty_two_cards_visible)

        # when a deck is shuffled the card order is different, this will fail 1
        # out of 52! or essentially never
        deck_one.shuffle()
        self.assertNotEqual(str(deck_one.show(True)),
                            self.__class__.fifty_two_cards_visible)

        # Check if all cards can be found in the untampered deck
        found = not_found = 0

        # Check each card in the deck
        for _ in range(0, 52):
            card = deck_one.draw()
            if str(deck_untampered.show(True)).find(str(card.peek(True))[1:-1]):
                found += 1
            else:
                print(card.peek(True))
                not_found += 1

        # All cards are found, without duplication
        self.assertEqual(not_found, 0)
        self.assertEqual(found, 52)

    def test_show(self):
        """ Shows the deck of cards, if cards are facedown it can be shown with
        them face up.

        """
        deck = Deck(1)
        self.assertEqual(deck.show(), self.__class__.fifty_two_cards_hidden)
        self.assertEqual(deck.show(True), self.__class__.fifty_two_cards_visible)

    def test_draw(self):
        """ Test if every card can can be drawn correctly from the deck and that
            if the deck is empty false is returned

        """
        deck = Deck(1)

        # Gets the right card
        card = deck.draw()
        self.assertEqual(card.peek(True), "[2H]")

        # Retrieves a card for all cards
        for _ in range(0, 51):
            card = deck.draw()
            self.assertEqual(bool(card.peek(True)), True)

        # When deck is empty there are no more cards to retrieve
        card = deck.draw()
        self.assertEqual(card, False)

    def test_burn(self):
        """ Test if a card can be added to the bottom of the deck.

        """
        deck_one = Deck(1)
        deck_two = Deck(1)

        # Unmodified decks are equal
        self.assertEqual(str(deck_one.show(True)),
                         self.__class__.fifty_two_cards_visible)

        self.assertEqual(str(deck_two.show(True)),
                         self.__class__.fifty_two_cards_visible)

        # Cards that are readded to the bottom cause the decks to be unequal
        for _ in range(0, 51):
            deck_one.burn(deck_one.draw())
            self.assertNotEqual(str(deck_one.show(True)), str(deck_two.show(True)))

        # Deck was rebuilt
        deck_one.burn(deck_one.draw())
        self.assertEqual(str(deck_one.show(True)), str(deck_two.show(True)))

    def test_marker(self):
        """ Make sure marker card was set and can be retrieved for comparison.

        """
        deck = Deck(1)
        self.assertEqual(str(deck.marker), "[--]")


    def test_deck_stats(self):
        """ Can retrieve a list of pip counts.

        """
        deck = Deck(1)
        count = {"2": 4, "3": 4, "4": 4, "5": 4, "6": 4, "7": 4,
                 "8": 4, "9": 4, "T": 4, "J": 4, "Q": 4, "K": 4,
                 "A": 4}

        self.assertEqual(deck.deck_stats, count)

if __name__ == '__main__':
    unittest.main()







