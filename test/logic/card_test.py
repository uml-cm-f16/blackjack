#!/usr/bin/python3

import unittest

# Importing class to test
from ...src.logic.card import Card

class Test_Card(unittest.TestCase):
    """Tests the card class methods.

    """
    def test_Card_getterPip(self):
        """Pip aka Value retrieval.

        """
        pip = 'A'
        card = Card(pip, 'C')

        # Pip is retrievable
        self.assertEqual(card.pip, pip)

    def test_Card_getterSuit(self):
        """Suit retrieval.

        """
        suit = 'C'
        card = Card('A', suit)

        # Suit is retrievable
        self.assertEqual(card.suit, suit)

    def test_Card_strRepresentation(self):
        """String representation of a card.

        """
        self.assertEqual(str(Card('A', 'C')), "[AC]")
        self.assertEqual(str(Card('2', 'C')), "[2C]")
        self.assertEqual(str(Card('A', 'S')), "[AS]")
        self.assertEqual(str(Card('2', 'S')), "[2S]")

    def test_Card_flip(self):
        """Card flipping.

        """

        card = Card('A', 'C')
        self.assertEqual(str(card), "[AC]")

        card.flip()
        self.assertEqual(str(card), "[<>]")

        card.flip()
        self.assertEqual(str(card), "[AC]")

    def test_Card_peek(self):
        """Card peeking test.

        Checks to see if cards can be seen when in a visible state.
        Checks to see if cards can be forced to a temporary visible state.
        Checks that peek is temoporary and does not modify the card.

        """
        out1 = "[AC]"
        out2 = "[<>]"
        card = Card('A', 'C')

        # Visible state
        self.assertEqual(str(card), out1)
        self.assertEqual(str(card.peek()), out1)
        self.assertEqual(str(card.peek(True)), out1)

        card.flip()

        # Hidden State
        self.assertEqual(str(card), out2)
        self.assertEqual(str(card.peek()), out2)
        self.assertEqual(str(card.peek(True)), out1)
        self.assertEqual(str(card), out2) # not persisted

        card.flip()

        # Visible state return
        self.assertEqual(str(card), out1)
        self.assertEqual(str(card.peek()), out1)
        self.assertEqual(str(card.peek(True)), out1)