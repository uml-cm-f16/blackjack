#!/usr/bin/python3
""" This module tests the blackjack game logic class.

"""

# IMPORTS

import unittest

# Importing class to test

from app.src.logic.blackjack import Blackjack

from app.src.logic.card import Card

class TestBlackjack(unittest.TestCase):
    """ Tests the blackjack class methods.

    """

    def _stat_length(self, player, size):
        """ Each of the return values is also a list of size 7

        """
        self.assertEqual(isinstance(player, list), True)
        self.assertEqual(len(player), size)

    def _stat_0_length(self, player, size, obj_type):
        """ Player is a list of n size elements

        """
        self.assertEqual(isinstance(player, list), True)
        self.assertEqual(len(player), size)
        for item in player:
            self.assertEqual(isinstance(item, obj_type), True)

    def _stat_1(self, player, obj_type, low, high):
        """ Player is a list of items of obj_type within a range

        """
        self.assertEqual(isinstance(player, list), True)
        for item in player:
            self.assertEqual(isinstance(item, obj_type), True)
            # only one card is visible
            self.assertEqual(item in range(low, high + 1), True)

    def _stat_2(self, scores, score, maximum):
        """ Is is a number representing the score that is in the previous list
        It is under 21 if the list has a value under 21 else it is the smallest
        number in the list

        """
        self.assertEqual(isinstance(score, int), True)

        winning_values = list(filter(lambda x: x <= maximum, scores))
        loosing_values = list(filter(lambda x: x > maximum, scores))

        if len(winning_values) == 0:
            self.assertEqual(score, loosing_values[0])
        else:
            self.assertEqual(score, winning_values[-1])

    def test_player_next(self):
        """ Validate that a players turn is ended and moves to the next player.
        Testing both the property and player_end() as they are used in conjunction
        with each other.

        """
        blackjack = Blackjack(2)
        blackjack.round_start()

        blackjack.player_start()
        self.assertEqual(blackjack.player_current, 0)
        blackjack.player_end()

        blackjack.player_start()
        self.assertEqual(blackjack.player_current, 1)
        blackjack.player_end()

        blackjack.player_start()
        self.assertEqual(blackjack.player_current, -1)
        blackjack.player_end()

    def test_round_start(self):
        """ Starts a round of black jack by dealing all players and dealer their
        initial cards. First card face down, second card faceup

        """
        blackjack = Blackjack(1)
        ret = blackjack.round_start()

        # The return value is a list of size 2
        self.assertEqual(isinstance(ret, list), True)
        self.assertEqual(len(ret), 2)

        # Examining return stats
        self._stat_length(ret[0], 6)                           # Result size
        self.assertEqual(ret[0][0], 0)                         # Player number
        self._stat_0_length(ret[0][1], 2, Card)                # Hand type
        self._stat_1(ret[0][2], int, 1, 11)                    # Score range
        self._stat_2(ret[0][2], ret[0][3], 21)                 # Result calculation
        self.assertEqual(isinstance(ret[0][4], float), True)   # Percent is given
        self.assertEqual(ret[0][5], -2)                        # No calculated result

        # Examining return stats
        self._stat_length(ret[1], 6)                           # Result size
        self.assertEqual(ret[1][0], -1)                        # Player number
        self._stat_0_length(ret[1][1], 2, Card)                # Hand type
        self._stat_1(ret[1][2], int, 1, 11)                    # Score range
        self._stat_2(ret[1][2], ret[1][3], 21)                 # Result calculation
        self.assertEqual(isinstance(ret[1][4], float), True)   # Percent is given
        self.assertEqual(ret[1][5], -2)                        # No calculated result

        # First card is hidden
        self.assertEqual(ret[0][1][0].pip, False)
        self.assertEqual(ret[1][1][0].pip, False)

        # Second card is visible
        self.assertNotEqual(ret[0][1][1].pip, False)
        self.assertNotEqual(ret[1][1][1].pip, False)

    def test_player_start(self):
        """" When a player starts their turn, hidden cards are flipped over

        """
        blackjack = Blackjack(1)
        blackjack.round_start()
        ret = blackjack.player_start()

        # Examining return stats
        self._stat_length(ret, 6)                           # Result size
        self.assertEqual(ret[0], 0)                         # Player number
        self._stat_0_length(ret[1], 2, Card)                # Hand type
        self._stat_1(ret[2], int, 2, 22)                    # Score range
        self._stat_2(ret[2], ret[3], 21)                    # Result calculation
        self.assertEqual(isinstance(ret[4], float), True)   # Percent is given
        self.assertEqual(ret[5], -2)                        # No calculated result

        # Cards are visible
        self.assertNotEqual(ret[1][0].pip, False)
        self.assertNotEqual(ret[1][1].pip, False)

    def test_player_hit(self):
        """ A target hand can hit to get a card

        """
        blackjack = Blackjack(1)
        blackjack.round_start()
        blackjack.player_start()
        ret = blackjack.player_hit()

        # Examining return stats
        self._stat_length(ret, 6)                           # Result size
        self.assertEqual(ret[0], 0)                         # Player number
        self._stat_0_length(ret[1], 3, Card)                # Hand type
        self._stat_1(ret[2], int, 3, 33)                    # Score range
        self._stat_2(ret[2], ret[3], 21)                    # Result calculation
        self.assertEqual(isinstance(ret[4], float), True)   # Percent is given
        self.assertEqual(ret[5], -2)                        # No calculated result

        # Cards are visible
        self.assertNotEqual(ret[1][0].pip, False)
        self.assertNotEqual(ret[1][1].pip, False)
        self.assertNotEqual(ret[1][2].pip, False)

    def test_player_stay(self):
        """ A target hand cans stay

        """

        blackjack = Blackjack(1)
        blackjack.round_start()
        blackjack.player_start()
        ret = blackjack.player_hit()

        # Examining return stats
        self._stat_length(ret, 6)                           # Result size
        self.assertEqual(ret[0], 0)                         # Player number
        self._stat_0_length(ret[1], 3, Card)                # Hand type
        self._stat_1(ret[2], int, 3, 33)                    # Score range
        self._stat_2(ret[2], ret[3], 21)                    # Result calculation
        self.assertEqual(isinstance(ret[4], float), True)   # Percent is given
        self.assertEqual(ret[5], -2)                        # No calculated result

        # Cards are visible
        self.assertNotEqual(ret[1][0].pip, False)
        self.assertNotEqual(ret[1][1].pip, False)
        self.assertNotEqual(ret[1][2].pip, False)

        # No stat changes occur
        ret_2 = blackjack.player_stay()
        self.assertEqual(ret, ret_2)



    def test_dealer_stats(self):
        """ Gets the dealers stats through a round, once it is a dealers turn
        stats change due to card flip

        """
        players = 2

        blackjack = Blackjack(players)
        ret = blackjack.round_start()
        dealer = ret[players]

        blackjack.player_start()
        self.assertEqual(blackjack.player_current, 0)
        self.assertEqual(blackjack.dealer_stats(), dealer)
        blackjack.player_end()

        blackjack.player_start()
        self.assertEqual(blackjack.player_current, 1)
        self.assertEqual(blackjack.dealer_stats(), dealer)
        blackjack.player_end()

        blackjack.player_start()
        self.assertEqual(blackjack.player_current, -1)
        # Card has been flipped
        self.assertNotEqual(blackjack.dealer_stats(), dealer)
        blackjack.player_end()

    def test_round_end(self):
        """ Ends a round of blackjack by dealing the dealer, and getting results.

        """

        players = 1

        blackjack = Blackjack(players)
        blackjack.round_start()

        blackjack.player_start()
        blackjack.player_stay()
        blackjack.player_end()

        ret = blackjack.round_end()

        # Examining return stats
        self._stat_length(ret[0], 6)                           # Result size
        self.assertEqual(ret[0][0], 0)                         # Player number
        self._stat_0_length(ret[0][1], 2, Card)                # Hand type
        self._stat_1(ret[0][2], int, 2, 22)                    # Score range
        self._stat_2(ret[0][2], ret[0][3], 21)                 # Result calculation
        self.assertEqual(isinstance(ret[0][4], float), True)   # Percent is given
        self.assertNotEqual(ret[0][5], -2)                     # Calculated result

        # Examining return stats
        self._stat_length(ret[1], 6)                           # Result size
        self.assertEqual(ret[1][0], -1)                        # Player number
        self._stat_0_length(ret[1][1], len(ret[1][1]), Card)   # Hand type
        #self._stat_1(ret[1][2], int, 1, 11)                   # Score range
        self._stat_2(ret[1][2], ret[1][3], 21)                 # Result calculation
        self.assertEqual(isinstance(ret[1][4], float), True)   # Percent is given
        self.assertNotEqual(ret[0][5], -2)                     # Calculated result

    def test_round_reset(self):
        """ Round ends and cards returned, dealer is pointed back to player 0

        """
        players = 1

        blackjack = Blackjack(players)
        blackjack.round_start()

        blackjack.player_start()
        blackjack.player_stay()
        blackjack.player_end()

        blackjack.round_end()
        ret = blackjack.round_reset()

        # Examining return stats
        self._stat_length(ret[0], 6)                           # Result size
        self.assertEqual(ret[0][0], 0)                         # Player number
        self._stat_0_length(ret[0][1], 0, Card)                # Hand type
        self._stat_1(ret[0][2], int, 0, 0)                     # Score range
        self._stat_2(ret[0][2], ret[0][3], 21)                 # Result calculation
        self.assertEqual(isinstance(ret[0][4], float), True)   # Percent is given
        self.assertEqual(ret[0][5], -2)                        # No calculated result

        # Examining return stats
        self._stat_length(ret[0], 6)                           # Result size
        self.assertEqual(ret[0][0], 0)                         # Player number
        self._stat_0_length(ret[0][1], 0, Card)                # Hand type
        self._stat_1(ret[0][2], int, 0, 0)                     # Score range
        self._stat_2(ret[0][2], ret[0][3], 21)                 # Result calculation
        self.assertEqual(isinstance(ret[0][4], float), True)   # Percent is given
        self.assertEqual(ret[0][5], -2)                        # No calculated result

        # current player is player 0
        self.assertEqual(blackjack.player_current, 0)

if __name__ == '__main__':
    unittest.main()
