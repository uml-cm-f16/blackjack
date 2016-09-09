class Hand():
	'''
	A hand of cards.
	'''

	def __init__(self):
		'''
		Generates an empty hand of cards.
		'''
		self._hand = []

	def __repr__(self):
		return ', '.join(str(card) for card in self._hand)

	def _has(self, card) :
		'''
		Checks to see if card is in the hand.

		Args:
			card 	(Card)		: The card to look for.

		Returns:
					(Boolean)	: If the card was found in the hand.
		'''
		return self._hand.count(card) > 0

	#	PUBLIC METHODS

	def add(self, card) :
		self._hand.append(card)

	def remove(self, card):
		if self._has(card):
			self._hand.remove(card)
			return True
		return False

	def fold(self):
		'''
		Folds a hand of cards.

		Returns:
			cards	(Card)		: The cards in the _hand.
		'''
		cards = self._hand
		self._hand = []
		return cards

	def show(self) :
		'''
		Shows the _hand of cards.
		'''
		print(self._hand)
