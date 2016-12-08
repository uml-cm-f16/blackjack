#!/usr/bin/python3
"""This module tests the hand class."""

import unittest

from app.src.logic.card import Card

# Importing class to test
from app.src.logic.hand import Hand

class Test_Hand(unittest.TestCase):
    """ Tests the card class methods.

    """
    def test_str_representation(self):
        """A hand can be represented.

        """
        # An empty hand
        self.assertEqual(str(Hand()), "")

        # A hand with one card
        hand1 = Hand()
        hand1.append(Card('A', 'C'))
        self.assertEqual(str(hand1), "[AC]")

        # A hand with more than one card
        hand2 = Hand()
        hand2.append(Card('A', 'C'))
        hand2.append(Card('2', 'C'))
        self.assertEqual(str(hand2), "[AC], [2C]")

    def test_append(self):
        """A hand can be added to.

        """
        # Empty hand
        hand = Hand()
        self.assertEqual(str(Hand()), "")

        # One Card
        hand.append(Card('A', 'C'))
        self.assertEqual(str(hand), "[AC]")

        # Two Card
        hand.append(Card('2', 'C'))
        self.assertEqual(str(hand), "[AC], [2C]")

        # Three Card
        hand.append(Card('3', 'C'))
        self.assertEqual(str(hand), "[AC], [2C], [3C]")

    def test_remove(self):
        """ A hand can have a card removed.

        """
        hand = Hand()

        card1 = Card('A', 'C')

        hand.append(card1)
        hand.append(Card('2', 'C'))
        hand.append(Card('3', 'C'))

        # All cards are in hand
        self.assertEqual(str(hand), "[AC], [2C], [3C]")

        # Card not in hand
        self.assertEqual(hand.remove(Card('J', 'J')), False)

        # All cards in hand are still there
        self.assertEqual(str(hand), "[AC], [2C], [3C]")

        # Appropriate responses for card being removed first its there, second its not
        self.assertEqual(hand.remove(card1), True)
        self.assertEqual(hand.remove(card1), False)

        # All remaining cards in hand are still there
        self.assertEqual(str(hand), "[2C], [3C]")

    def test_flip(self):
        """ Can flip a card in the hand.

        """
        # Build hand
        hand = Hand()
        hand.append(Card('A', 'C'))
        hand.append(Card('2', 'C'))
        hand.append(Card('3', 'C'))

        # Test hand
        self.assertEqual(str(hand), "[AC], [2C], [3C]")

        hand.flip(0)
        self.assertEqual(str(hand), "[<>], [2C], [3C]")

        hand.flip(0)
        self.assertEqual(str(hand), "[AC], [2C], [3C]")

        hand.flip(1)
        self.assertEqual(str(hand), "[AC], [<>], [3C]")

        hand.flip(1)
        self.assertEqual(str(hand), "[AC], [2C], [3C]")

        hand.flip(2)
        self.assertEqual(str(hand), "[AC], [2C], [<>]")

        hand.flip(2)
        self.assertEqual(str(hand), "[AC], [2C], [3C]")

    def test_fold(self):
        """ Can fold a hand of cards and give them back to the dealer.

        """
        # Build hand
        hand = Hand()
        hand.append(Card('A', 'C'))
        hand.append(Card('2', 'C'))
        hand.append(Card('3', 'C'))

        # Test hand
        self.assertEqual(str(hand), "[AC], [2C], [3C]")

        # hand is empty
        tmp_hand = hand.fold()
        self.assertEqual(str(hand), "")

        # Hand was returned
        self.assertEqual(str(tmp_hand[0]), "[AC]")
        self.assertEqual(str(tmp_hand[1]), "[2C]")
        self.assertEqual(str(tmp_hand[2]), "[3C]")

    def test_total(self):
        """ Can sum up a hand of cards.

        """
        # Card value dictionary
        value = {False: 0, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
                 "8": 8, "9": 9, "T": 10, "J": 10, "Q": 10, "K": 10, "A": [1, 11]}

        hand = Hand()
        hand2 = Hand()

        # Build hand
        hand.append(Card('A', 'C'))
        hand.append(Card('2', 'C'))
        hand.append(Card('3', 'C'))

        # Test hand
        self.assertEqual(str(hand), "[AC], [2C], [3C]")
        self.assertEqual(hand.total(value), [6, 16])

        # Change hand by adding 4
        hand.append(Card('4', 'C'))
        self.assertEqual(str(hand), "[AC], [2C], [3C], [4C]")
        self.assertEqual(hand.total(value), [10, 20])

        # Change hand by subtracting 2
        hand.remove(Card('2', 'C'))
        self.assertEqual(str(hand), "[AC], [3C], [4C]")
        self.assertEqual(hand.total(value), [8, 18])

        # Test multi level flatten
        hand2.append(Card('A', 'C'))
        hand2.append(Card('A', 'C'))
        hand2.append(Card('A', 'C'))
        hand2.append(Card('A', 'C'))
        self.assertEqual(str(hand2), "[AC], [AC], [AC], [AC]")
        self.assertEqual(hand2.total(value), [4, 14, 24, 34, 44])

    def test_total_closest(self):
        """ Get highest score up to max score if possible, otherwise get the
        lowest score.

        """
        # Card value dictionary
        value = {False: 0, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
                 "8": 8, "9": 9, "T": 10, "J": 10, "Q": 10, "K": 10, "A": [1, 11]}

        hand = Hand()
        hand2 = Hand()

        # Build hand
        hand.append(Card('A', 'C'))
        hand.append(Card('2', 'C'))
        hand.append(Card('3', 'C'))

        # Test hand
        self.assertEqual(str(hand), "[AC], [2C], [3C]")
        self.assertEqual(hand.total_closest(value, 21), 16)

        # Change hand by adding 4
        hand.append(Card('4', 'C'))
        self.assertEqual(str(hand), "[AC], [2C], [3C], [4C]")
        self.assertEqual(hand.total_closest(value, 21), 20)

        # Change hand by subtracting 2
        hand.remove(Card('2', 'C'))
        self.assertEqual(str(hand), "[AC], [3C], [4C]")
        self.assertEqual(hand.total_closest(value, 21), 18)

        # Testing past 21 and with multiple values
        hand.append(Card('3', 'C'))
        self.assertEqual(str(hand), "[AC], [3C], [4C], [3C]")
        self.assertEqual(hand.total_closest(value, 21), 21)

        hand.append(Card('3', 'C'))
        self.assertEqual(str(hand), "[AC], [3C], [4C], [3C], [3C]")
        self.assertEqual(hand.total_closest(value, 21), 14)

        hand.append(Card('T', 'C'))
        self.assertEqual(str(hand), "[AC], [3C], [4C], [3C], [3C], [TC]")
        self.assertEqual(hand.total_closest(value, 21), 24)

        hand2.append(Card('A', 'C'))
        hand2.append(Card('A', 'C'))
        hand2.append(Card('A', 'C'))
        hand2.append(Card('A', 'C'))
        hand2.append(Card('A', 'C'))
        self.assertEqual(str(hand2), "[AC], [AC], [AC], [AC], [AC]")
        self.assertEqual(hand2.total_closest(value, 21), 15)

if __name__ == '__main__':
    unittest.main()
