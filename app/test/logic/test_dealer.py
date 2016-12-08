#!/usr/bin/python3
""" This module tests the card Dealer class.

"""

# IMPORTS

import unittest

# Importing class to test

from app.src.logic.dealer import Dealer

from app.src.logic.player import Player
from app.src.logic.card import Card

class TestDealer(unittest.TestCase):
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

    """ Tests the card class methods.

    """
    def test_player_number(self):
        """ Test players were assigned sequentially a number >= 0 starting at 0

        """
        player_0 = Player(True)
        dealer = Dealer()
        player_1 = Player()

        # Dealer does not interrupt the count in Player
        self.assertEqual(player_0.number, 0)
        self.assertEqual(dealer.number, -1)
        self.assertEqual(player_1.number, 1)

    def test_inheritance(self):
        """ Make sure Player has inherited Hand

        """
        dealer = Dealer()
        self.assertEqual(isinstance(dealer, Player), True)

    def test_show_deck(self):
        """ Test that a dealer can show the deck

        """
        dealer = Dealer()
        self.assertEqual(dealer.show_deck(), self.__class__.fifty_two_cards_hidden)
        self.assertEqual(dealer.show_deck(True), self.__class__.fifty_two_cards_visible)

    def test_shuffle(self):
        """ Test that a deck was shuffled by the dealer.

        """
        # Two decks ate the same
        dealer_1 = Dealer()
        dealer_2 = Dealer()
        self.assertEqual(dealer_1.show_deck(True), dealer_2.show_deck(True))

        # Tho shuffled decks 1/!52 * 1/!52 chance of being the same -> not the same
        dealer_1.shuffle()
        dealer_2.shuffle()
        self.assertNotEqual(dealer_1.show_deck(True), dealer_2.show_deck(True))

    def test_draw(self):
        """ A Dealer can draw a card from the deck

        """
        # Deck is as expected
        dealer_1 = Dealer()
        self.assertEqual(dealer_1.show_deck(True), Test_Dealer.fifty_two_cards_visible)

        # A card has been removed from the deck
        self.assertEqual(isinstance(dealer_1.draw(), Card), True)
        self.assertNotEqual(dealer_1.show_deck(True), Test_Dealer.fifty_two_cards_visible)

    def test_burn(self):
        """ A Dealer can return a card to the deck

        """
        # Deck exists
        dealer_1 = Dealer()
        self.assertEqual(dealer_1.show_deck(True), Test_Dealer.fifty_two_cards_visible)

        # Card was drawn and deck has changes
        card = dealer_1.draw()
        self.assertEqual(isinstance(card, Card), True)
        self.assertNotEqual(dealer_1.show_deck(False), Test_Dealer.fifty_two_cards_hidden)

        # Single card was returned
        dealer_1.burn(card)
        self.assertEqual(dealer_1.show_deck(False), Test_Dealer.fifty_two_cards_hidden)

        # Multiple cards
        card_1 = dealer_1.draw()
        card_2 = dealer_1.draw()
        self.assertNotEqual(dealer_1.show_deck(False), Test_Dealer.fifty_two_cards_hidden)

        # Return a list of cards
        dealer_1.burn([card_1, card_2])
        self.assertEqual(dealer_1.show_deck(False), Test_Dealer.fifty_two_cards_hidden)

    def test_flip_deal(self):
        """ A deal can be given face up or face down.

        """
        dealer_1 = Dealer()
        card_1 = dealer_1.draw()

        # Dealt card can be flipped
        self.assertEqual(str(card_1), '[<>]')
        self.assertEqual(str(dealer_1.flip_deal(card_1)), '[2H]')

    def test_deck_stats(self):
        """ Gets deck statistics for probability calculations

        """
        dealer_1 = Dealer()
        stats = dealer_1.deck_stats

        # Deck stats were built correctly
        self.assertEqual(isinstance(stats, dict), True)
        for _, value in stats.items():
            self.assertEqual(value, 4)

        # Check dictionary was updated
        card = dealer_1.draw()
        card.flip()

        stats = dealer_1.deck_stats
        for key, value in stats.items():
            if card.pip == key:
                self.assertEqual(value, 3)
            else:
                self.assertEqual(value, 4)

if __name__ == '__main__':
    unittest.main()
