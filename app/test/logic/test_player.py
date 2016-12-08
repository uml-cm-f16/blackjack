#!/usr/bin/python3
""" This module tests the card Player class.

"""

# IMPORTS

import unittest

# Importing class to test

from app.src.logic.player import Player

from app.src.logic.hand import Hand

class TestPlayer(unittest.TestCase):
    """ Tests the card class methods.

    """

    def test_player_number(self):
        """ Test players were assigned sequentially a number >= 0 starting at 0

        """
        player = [Player(True), Player(), Player()]

        self.assertEqual(player[0].number, 0)
        self.assertEqual(player[1].number, 1)
        self.assertEqual(player[2].number, 2)

        self.assertEqual(player[0].number, 0)
        self.assertEqual(player[1].number, 1)
        self.assertEqual(player[2].number, 2)

    def test_inheritance(self):
        """ Make sure Player has inherited Hand

        """
        player = Player()
        self.assertEqual(isinstance(player, Hand), True)

if __name__ == '__main__':
    unittest.main()
