#!/usr/bin/python3

from .player import Player
from .deck import Deck

class Dealer(Player):
	"""A card dealer.

	A player that also can deal cards.
	"""
	def __init__(self):
		self._dealer = True
		self._deck = Deck()
		super(Dealer, self).__init__()

	def showDeck(self):
		print(self._deck)

	def shuffle(self):
		return self._deck.shuffle()

	def draw(self):
		return self._deck.draw()

	def burn(self, cards):
		return self._deck.burn(cards)

	def flip(self, card):
		card.flip()
		return card

	@property
	def name(self):
		return 'Dealer'

	@property
	def isDealer(self):
		"""If the player is a dealer.

		Returns:
			(Boolean): False: A player is not a dealer.
			(Boolean): True: A player is a dealer.

		"""
		return True