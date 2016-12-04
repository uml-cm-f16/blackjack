#!/usr/bin/python3
"""A Blackjack player."""

from decimal import Decimal, ROUND_HALF_UP

from .player import Player
from .dealer import Dealer

class Blackjack(object):
    """BlackJack rule set for dealer.

    """
    # Private Class Attributes
    _values = {False: 0, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
               "9": 9, "T": 10, "J": 10, "Q": 10, "K": 10, "A": 11}
    _terms = {"DEALER": -1, "WIN": 1, "DRAW": 0, "LOSS": -1, "UNKNOWN": -2,
              "SCORE_MAX": 21}

    # Class methods
    def __init__(self, num_player=1):
        """ Create a black jack game.

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

        super(Blackjack, self).__init__()

    # Private properties
    @property
    def _target_hand(self):
        """ Determine who's hand is the focus on.

        Returns:
            <Player>                The player | dealer who is in focus
        """
        # if dealer is in focus

        if self._player_current == self._terms["DEALER"]:
            return self._dealer

        # The player in focus
        return self._player[self._player_current]

    @property
    def _target_hand_total(self):
        return self._target_hand.total(self._values)

    @property
    def _target_hand_total_closest(self):
        return self._target_hand.total_closest(self._values, self._terms["SCORE_MAX"])

    @property
    def _target_hand_stats(self):
        """ The stats of the player | Dealer

        Returns:
            <list>  [<bool>,        If the round is in play
                     [<int>,        The player | Dealer number
                      <int>,        The hands score
                      <float>]]     Chance to stay in game with next hit
        """
        return [self._player_current,
                self._target_hand,
                self._target_hand_total,
                self._target_hand_total_closest,
                self._percent]

    @property
    def _percent(self):
        """Percentage chance to win from next card.

        Returns:
            (float): The percentage to win off next card.

        """
        def playable_cards(key, score):
            """ A card is playable id the card does not push the score past the
            max.

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

            """

            for val in score:
                if val + self._values[key] <= self._terms["SCORE_MAX"]:
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

        """
        if visible is True:
            self._target_hand.append(self._dealer.flip_deal(self._dealer.draw()))
        else:
            self._target_hand.append(self._dealer.draw())

    def _target_hand_next(self):
        """ Iterate through player index, with DEALER | -1 meaning dealer.

        Returns:
            <int>   -1 | DEALER     The index of the dealer
            <int>   positive        The index of the player

        """
        # Get next player
        self._player_current += self._player_count
        if self._player_current == self._player_count:
            self._player_current = self._terms["DEALER"]

        return self._player_current


    # Public properties
    @property
    def player_current(self):
        return self._player_current
    # Public Methods
    def round_start(self):
        """ Starts a round of black jack by dealing all players and dealer their
        initial cards.

        Returns:
            <list>  [<bool>,        If the round is in play
                     [<int>,        The player | Dealer number
                      <int>,        The hands score
                      <float>]]     Chance to stay in game with next hit
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
        """Flip hidden cards to visible

        Returns:
            <list>  [<bool>,        If the round is in play
                     [<int>,        The player | Dealer number
                      <int>,        The hands score
                      <float>]]     Chance to stay in game with next hit
        """
        # Move to the current player
        for card in self._target_hand:
            if card.pip is False:
                self._dealer.flip_deal(card)

        # Is now the dealer turn
        if self._player_current == self._terms['DEALER']:
            for card in self._target_hand:
                if card.pip is False:
                    self._dealer.flip_deal(card)
            return self._target_hand_stats

        # Is a player
        return self._target_hand_stats

    def player_hit(self):
        """ Add a card to the target

        Returns:
            <list>  [<bool>,        If the round is in play
                     [<int>,        The player | Dealer number
                      <int>,        The hands score
                      <float>]]     Chance to stay in game with next hit
        """
        self._deal_card(True)
        return self._target_hand_stats

    def player_stay(self):
        """ Stays a targets hand

        Returns:
            <list>  [<bool>,        If the round is in play
                     [<int>,        The player | Dealer number
                      <int>,        The hands score
                      <float>]]     Chance to stay in game with next hit
        """
        return self._target_hand_stats

    def player_end(self):
        return self._target_hand_next()
    def round_end(self):
        """ Ends a round of blackjack by dealing the dealer, and getting results.

        Returns:
            <list>  [<bool>,        If the round is in play
                        [[<int>,    The player | Dealer number
                          <int>,    The hands score
                          <int>],   -2 | -1 | 0 | 1 <=> LOSS | DRAW | WIN | UNKNOWN
                         ...]
        """
        # get closest possible value to and under self._terms["SCORE_MAX"], if not the lowest value
        dealer_result = self._target_hand.total_closest(self._values, self._terms["SCORE_MAX"])

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

                score = self._target_hand.total_closest(self._values, self._terms["SCORE_MAX"])

                #   Win loss draw conditions
                if dealer_result > self._terms["SCORE_MAX"] and score > self._terms["SCORE_MAX"]:
                    state = self._terms["LOSS"]
                elif dealer_result > self._terms["SCORE_MAX"]:
                    state = self._terms["WIN"]
                elif score > self._terms["SCORE_MAX"] or score < dealer_result:
                    state = self._terms["LOSS"]
                elif score > dealer_result:
                    state = self._terms["WIN"]
                elif score == dealer_result:
                    state = self._terms["DRAW"]

                ret.append([self._player_current, score, state])
            ret.append([self._player_current, dealer_result, house])

            # Fold all hands
            while self._target_hand_next() != self._terms["DEALER"]:
                self._target_hand.fold()
            self._target_hand.fold()

            self._target_hand_next()

            # return win loss results
            return ret

        else:
            self._deal_card(True)
            return self.round_end()







