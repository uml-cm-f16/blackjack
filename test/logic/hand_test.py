#!/usr/bin/python3
"""This module tests the hand class."""

import unittest

from ...src.logic.card import Card

# Importing class to test
from ...src.logic.hand import Hand

class Test_Hand(unittest.TestCase):
    """Tests the card class methods.

    """
    def test_str_representation(self):
        """A hand can be represented.

        """
        # An empty hand
        self.assertEqual(str(Hand()), "")

        # A hand with one card
        hand1 = Hand()
        hand1.add(Card('A', 'C'))
        self.assertEqual(str(hand1), "[AC]")

        # A hand with more than one card
        hand2 = Hand()
        hand2.add(Card('A', 'C'))
        hand2.add(Card('2', 'C'))
        self.assertEqual(str(hand2), "[AC], [2C]")

    def test_add(self):
        """A hand can be added to.

        """
        # Empty hand
        hand = Hand()
        self.assertEqual(str(Hand()), "")

        # One Card
        hand.add(Card('A', 'C'))
        self.assertEqual(str(hand), "[AC]")

        # Two Card
        hand.add(Card('2', 'C'))
        self.assertEqual(str(hand), "[AC], [2C]")

        # Three Card
        hand.add(Card('3', 'C'))
        self.assertEqual(str(hand), "[AC], [2C], [3C]")

    def test_remove(self):
        """A hand can have a card removed.

        """
        card1 = Card('A', 'C')

        hand = Hand()
        hand.add(card1)
        hand.add(Card('2', 'C'))
        hand.add(Card('3', 'C'))

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

    def test_total(self):
        """Can sum up a hand of cards.

        """
        # Card value dictionary
        value = {False: 0, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
                 "8": 8, "9": 9, "T": 10, "J": 10, "Q": 10, "K": 10, "A": 11}

        hand = Hand()
        card2 = Card('2', 'C')

        # Build hand
        hand.add(Card('A', 'C'))
        hand.add(card2)
        hand.add(Card('3', 'C'))

        # Test hand
        self.assertEqual(str(hand), "[AC], [2C], [3C]")
        self.assertEqual(hand.total(value), 16)

        # Change hand by adding 4
        hand.add(Card('4', 'C'))
        self.assertEqual(str(hand), "[AC], [2C], [3C], [4C]")
        self.assertEqual(hand.total(value), 20)

        # Change hand by subtracting 2
        hand.remove(card2)
        self.assertEqual(str(hand), "[AC], [3C], [4C]")
        self.assertEqual(hand.total(value), 18)

    def test_flip(self):
        """Can flip a card in the hand.

        """
        # Build hand
        hand = Hand()
        hand.add(Card('A', 'C'))
        hand.add(Card('2', 'C'))
        hand.add(Card('3', 'C'))

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
        """Can fold a hand of cards and give them back to the dealer.

        """
        # Build hand
        hand = Hand()
        hand.add(Card('A', 'C'))
        hand.add(Card('2', 'C'))
        hand.add(Card('3', 'C'))

        # Test hand
        self.assertEqual(str(hand), "[AC], [2C], [3C]")

        # hand is empty
        tmp_hand = hand.fold()
        self.assertEqual(str(hand), "")

        # Hand was returned
        self.assertEqual(str(tmp_hand[0]), "[AC]")
        self.assertEqual(str(tmp_hand[1]), "[2C]")
        self.assertEqual(str(tmp_hand[2]), "[3C]")
