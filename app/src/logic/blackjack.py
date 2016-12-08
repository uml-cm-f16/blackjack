#!/usr/bin/python3
""" A Blackjack player game API

"""

#   IMPORTS

from decimal import Decimal, ROUND_HALF_UP

from .player import Player
from .dealer import Dealer

#   CLASS

class Blackjack(object):
    """ BlackJack rule set for dealer.

    Attributes:
        _values:    (Dict): The pips and corresponding values.
        _terms:     (Dict): Dictionary of defined terms
    """
    _values = {False: 0, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
               "9": 9, "T": 10, "J": 10, "Q": 10, "K": 10, "A": [1, 11]}
    _terms = {"DEALER": -1, "WIN": 1, "DRAW": 0, "LOSS": -1, "UNKNOWN": -2,
              "SCORE_MAX": 21}

    # Class methods
    def __init__(self, num_player=1):
        """ Create a black jack game.

        Args:
            num_player: (int): 1: The number of players

        """
        # Create dealer
        self._dealer = Dealer()

        # Create players
        self._player = []
        self._player_count = num_player
        self._player_current = self._terms["DEALER"]

        # Create players
        while self._target_hand_next() != self._terms["DEALER"]:
            self._player.append(Player())

        super().__init__()

    # Private properties
    @property
    def _target_hand(self):
        """ Determine who's hand the focus is on.

        Returns:
            (player): The player | dealer that is in focus
        """
        # If dealer is in focus
        if self._player_current == self._terms["DEALER"]:
            return self._dealer

        # The player in focus
        return self._player[self._player_current]

    @property
    def _target_hand_total(self):
        """ A list of The target hands possible totals.

        Returns:
            (list): A list of the possible hand totals.
        """
        return self._target_hand.total(self._values)

    @property
    def _target_hand_total_closest(self):
        """ The highest hand value under SCORE_MAX if possible otherwise the
        lowest value

        Returns:
            (int): The highest hand value under SCORE_MAX if possible otherwise
                the lowest value

        """
        return self._target_hand.total_closest(self._values,
                                               self._terms["SCORE_MAX"])

    @property
    def _target_hand_stats(self):
        """ The stats of the player | Dealer

        Returns:
            (list): [(int):,         The player | Dealer number
                     (int):,         The hands score
                     (float):,       Chance to stay in game with next hit
                     (int):]         Hand win state

        """
        return [self._player_current,
                self._target_hand,
                self._target_hand_total,
                self._target_hand_total_closest,
                self._percent,
                self._terms["UNKNOWN"]]

    @property
    def _percent(self):
        """ Percentage chance to win from next card.

        Returns:
            (float): The percentage to win off next card.

        """
        def playable_cards(key, score):
            """ A card is playable if the card does not push the score past the
            max.

            Args:
                key: (str): The card pip to search for
                score: (list): List of possible scores

            Returns:
                (int): The number of cards left with the key

            """
            # Ignore false key
            if key is False:
                return 0

            # find dict value if the card is playable
            if playable(key, score) is True:
                return self._dealer.deck_stats[key]

            # not playable, return nothing
            return 0

        def playable(key, score):
            """ Checks if the score outcome can leads to a possible win value.

            Args:
                key: (str): The pip of the card to add

            Returns:
                (bool): True: The card is playable
                (bool): False: The card is not playable

            """
            tmp = self._values[key]
            if not isinstance(tmp, list):
                tmp = [tmp]

            for k in tmp:
                for val in score:
                    if val + k <= self._terms["SCORE_MAX"]:
                        return True

            return False

        remaining_cards_dict = self._dealer.deck_stats

        # Get all possible scores
        score = self._target_hand.total(self._values)

        # Instances of playable scores = The numerator
        total_playable_cards = 0
        total_remaining_cards = 0

        for key in remaining_cards_dict:
            total_playable_cards += playable_cards(key, score)
            total_remaining_cards += remaining_cards_dict[key]

        # The percentage calculation
        percent = Decimal(100 * total_playable_cards / total_remaining_cards)

        # Rounded up to the .001 place
        return float(Decimal(percent.quantize(Decimal('.001'), ROUND_HALF_UP)))

    # Private methods
    def _deal_card(self, visible=False):
        """ Deals a card to the current target

        Args:
            visible: (bool): False: The visibility state of deal card.

        """
        card = self._dealer.draw()

        if visible is True:
            self._target_hand.append(self._dealer.flip_deal(card))
        else:
            self._target_hand.append(card)

    def _target_hand_next(self):
        """ Iterate through player index, with DEALER | -1 meaning dealer.

        Returns:
            (int): -1: The index of the dealer
            (int): The index of the player

        """
        # Get next player
        self._player_current += 1
        if self._player_current == self._player_count:
            self._player_current = self._terms["DEALER"]

        return self._player_current

    # Public properties
    @property
    def player_current(self):
        """ The current players number

        Returns:
            (int): The current players number

        """
        return self._player_current

    # Public Methods
    def round_start(self):
        """ Starts a round of black jack by dealing all players and dealer their
        initial cards.

        Returns:
            (list): [self._target_hand_stats: (list):,   The hand stat of the player
                    ...,
                    self._target_hand_stats: (list):]    The hand stat of the dealer

        """
        # Shuffling.
        self._dealer.shuffle()

        # Dealing Initial Hand
        while self._target_hand_next() != self._terms["DEALER"]:
            self._deal_card()
        self._deal_card()

        while self._target_hand_next() != self._terms["DEALER"]:
            self._deal_card(True)
        self._deal_card(True)

        # Build initial table data
        ret = []
        while self._target_hand_next() != self._terms["DEALER"]:
            ret.append(self._target_hand_stats)
        ret.append(self._target_hand_stats)

        self._target_hand_next()

        # return table initial stats
        return ret

    def player_start(self):
        """" Flip hidden cards to visible

        Returns:
            self._target_hand_stats: (list): current player

        """
        for card in self._target_hand:
            if card.pip is False:
                self._dealer.flip_deal(card)
        return self._target_hand_stats


    def player_hit(self):
        """ Add a card to the target

        Returns:
            self._target_hand_stats: (list): current player

        """
        self._deal_card(True)
        return self._target_hand_stats

    def player_stay(self):
        """ Stays a targets hand

        Returns:
            self._target_hand_stats: (list): current player

        """
        return self._target_hand_stats

    def player_end(self):
        """ Ends a players turn and moves to the next player.

        Returns:
            self._target_hand_stats: (list): for the dealer

        """
        return self._target_hand_next()
    def dealer_stats(self):
        """ Gets the dealers stats

        Returns:
            self._target_hand_stats: (list): for the dealer

        """
        # Store current player
        tmp = self._player_current

        # Get the dealers stats
        self._player_current = self._terms["DEALER"]
        stats = self._target_hand_stats

        # Return to current player
        self._player_current = tmp

        # Return stats
        return stats

    def round_end(self):
        """ Ends a round of blackjack by dealing the dealer, and getting results.

        Returns:
            (list): [self._target_hand_stats: (list):,   The hand state of the player
                    ...,
                    self._target_hand_stats: (list):]    The hand state of the dealer

        """
        # Start dealers turn
        self.player_start()

        # get closest possible value to and under self._terms["SCORE_MAX"], if not the lowest value
        dealer_result = self._target_hand.total_closest(self._values,
                                                        self._terms["SCORE_MAX"])

        # If the dealer has reached their 17 max hit point
        if dealer_result >= 17:
            # The return list
            ret = []

            #   Win loss draw conditions
            if dealer_result == self._terms["SCORE_MAX"]:
                house = self._terms["WIN"]
            if dealer_result > self._terms["SCORE_MAX"]:
                house = self._terms["LOSS"]
            if dealer_result < self._terms["SCORE_MAX"]:
                house = self._terms["UNKNOWN"]

            # Check all player results
            while self._target_hand_next() != self._terms["DEALER"]:

                score = self._target_hand.total_closest(self._values,
                                                        self._terms["SCORE_MAX"])

                # Win loss draw conditions
                # print(score, dealer_result)
                # player busts
                if score > self._terms["SCORE_MAX"]:
                    # print("player bust")
                    state = self._terms["LOSS"]
                # dealer busts
                elif dealer_result > self._terms["SCORE_MAX"]:
                    # print("dealer bust")
                    state = self._terms["WIN"]
                    # player busts
                    if score > self._terms["SCORE_MAX"]:
                        state = self._terms["LOSS"]

                # No one busts
                else:
                    # print("no bust")
                    # player ties dealer
                    if score == dealer_result:
                        # print("no bust - DRAW")
                        state = self._terms["DRAW"]
                    # player beats dealer
                    elif score > dealer_result:
                        # print("no bust - WIN")
                        state = self._terms["WIN"]
                    # player does not beat dealer
                    elif score < dealer_result:
                        # print("no bust - LOSS")
                        state = self._terms["LOSS"]

                # Append current player data
                player = self._target_hand_stats
                player[-1] = state
                ret.append(player)

            # Append dealer data
            dealer = self._target_hand_stats
            dealer[-1] = house
            ret.append(dealer)

            # return win loss results
            return ret

        else:
            self._deal_card(True)
            return self.round_end()

    def round_reset(self):
        """ Resets the table, and returns all hands back to the dealer to add
        into the deck.

        Returns:
            (list): [self._target_hand_stats: (list):,   The hand stat of the player
                    ...,
                    self._target_hand_stats: (list):]    The hand stat of the dealer
        """
        # Fold all hands
        ret = []
        while self._target_hand_next() != self._terms["DEALER"]:
            self._target_hand.fold()
            ret.append(self._target_hand_stats)
        self._target_hand.fold()
        ret.append(self._target_hand_stats)

        # Points round at player 0
        self._target_hand_next()

        return ret

