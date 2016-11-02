import unittest
import logging

from src.logic.card import Card

class TestCard(unittest.TestCase):

    def test_getterPip(self):
        pip = '1'
        card = Card(pip, 'C')

        self.assertEqual(card.pip, pip)

    def test_getterSuit(self):
        suit = 'C'
        card = Card('1', suit)

        self.assertEqual(card.suit, suit)

    def test_strRepresentation(self):
        card = Card('1', 'C')

        out = "[1C]"
        self.assertEqual(str(card), out)

    def test_flip(self):
        out1 = "[1C]"
        out2 = "[<>]"
        card = Card('1', 'C')

        self.assertEqual(str(card), out1)

        card.flip()
        self.assertEqual(str(card), out2)

        card.flip()
        self.assertEqual(str(card), out1)

if __name__ == '__main__':
    unittest.main()