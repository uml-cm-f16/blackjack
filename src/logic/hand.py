#!/usr/bin/python3
"""A players hand of cards."""

class Hand(list):
    """A hand of cards.

    """
    # Class methods
    def __init__(self):
        """Generates an empty hand of cards.

        """

        # Init to inherit classes
        super(Hand, self).__init__()

    def __str__(self):
        """The string representation of a Hand.

        Returns:
            (str): A string representation of a hand.

        """
        return ", ".join(str(card) for card in self)

    # Private methods
    def flip(self, index):
        """Flip a card by index.

        Args:
            index: (Integer): The index of the the card to flip.

        """
        self[index].flip()

    def fold(self):
        """Folds a hand of cards.

        Returns:
            (Card ...): The cards in the hand.

        """
        cards = self
        self.clear()
        return cards


    def total(self, values):
        """ A list of possible scores.

        """
        def flatten(lst):
            """ Flattens a multi level lest to one level.

            """
            return sum(([x] if not isinstance(x, list) else flatten(x) for x in [lst]), [])

        def get_val(key, score):
            """ Get the card value added to the score.

            """
            # If an ace
            if isinstance(values[key], list):
                return [elem + score for elem in values[key]]

            # Not an ace
            return values[key] + score

        def branch_scores(key, score):
            """ dir
            """
            # If the total is a list because of multiple valued cards
            if isinstance(score, list):
                return [branch_scores(key, i) for i in score]

            # if the score is a single value
            return get_val(key, score)

        # Get all possible scores
        score = 0
        for card in self:
            score = branch_scores(card.pip, score)

        # Return an non nested list of scores
        return flatten(score)

    def total_closest(self, values, max_score):
        """ Get highest score up to max score if possible, otherwise get the
        lowest score

        """
        # Get all possible scores
        score = self.total(values)

        # no score meets criteria
        minimum = min(score)
        if minimum > max_score:
            return minimum

        # get score at or under max score
        score = filter(lambda x: x <= max_score, score)
        return max(score)

