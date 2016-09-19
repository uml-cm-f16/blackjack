#!/usr/bin/python3

from random import shuffle, randint

from .card import Card

class Deck(object) :
	"""A deck of cards and actions.

	A standard deck consists of 52 Cards from 2 - A of K, H, D, and S suits. This
	class allows for multiple decks to be used alongside a marker card to signify
	shuffling.

	Attributes:
        _pips	(List):	The list of pips to use.
		_suits	(List):	The list of suits to use.
		_marker (Card):	The marker card used to signify reshuffle point.

	"""
	_pips = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
	_suits = ['H', 'S', 'D', 'C']
	_marker = Card('-', '-')

	def __init__(self, qty = 1) :
		""" Creates deck.

		Attributes:
        	_qty	(int): Number of decks to generate.
			_deck	(int): The deck of cards.
			_count	(int): The number of cards of the pip value still in the deck.

		Args:
			qty 	(int) :	The number of decks to include.

		"""
		self._qty = qty
		self._deck = []
		self._count = []
		for i in range(0, self._qty) :
			for suit in self.__class__._suits :
				for pip in self.__class__._pips :
					self._insert(Card(pip, suit))
		print("Deck Made.")
		super(Deck, self).__init__()

	def __str__(self):
		"""The str representation of a Deck.

		"""
		return ', '.join(str(card) for card in self._deck)

	def _insert(self, card, position = 0) :
		"""Adds a card to the deck.

		Args:
			card 	(Card)		: The card to add to the deck.

		"""
		#self._count[card.pip] += 1
		self._deck.insert(position, card)

	def _has(self, card) :
		"""Checks to see if card is in the deck.

		Args:
			card 	(Card)		: The card to look for.

		Returns:
					(Boolean)	: If the card was found in the deck.

		"""
		return self._deck.count(card) > 0

	def _remove(self, card) :
		"""Removes a card from the deck.

		Args:
			card 	(Card)		: The card to remove.

		Returns:
			True	(Boolean) 	: Succesful operation status.
			False	(Boolean) 	: Failed operation status.

		"""
		count = self._deck.count(card)
		if count > 0 :
			self._deck.remove(card)
			#self._count[card.pip] -= 1
			if count - 1 == self._deck.count(card) :
				return True
		return False

	def _pop(self) :
		"""Retrieve a card from the top of the deck.

		Returns:
			card 	(Card)		: The card that was retrieved.
			False	(Boolean)	: The deck is empty.

		"""

		if self._deck :
			#self._count[card.pip] -= 1
			return self._deck.pop()
		return False

	def _mark(self, rFlag = False) :
		"""Marks a position in the deck to signal reshuffle.

		Args:
			rFlag	(Boolean) 	: False	: Marker is placed at bottom of deck.
								  True	: Randomize the location of the marker.

		"""
		# Remove marker if in deck
		if self._has(self.__class__._marker):
			self._remove(self.__class__._marker)

		# Add marker to deck
		if rFlag :
			position = randint(0, len(self._deck))
			self._insert(self.__class__._marker, position)
		else :
			self._insert(self.__class__._marker)

	def shuffle(self, mark = False, rFlag = True) :
		"""Shuffles a deck of cards.

		Has the capability of marking the next shuffle point randomly or once
		all cards have been used.

		Args:
			mark:	(Boolean)	: True  : Mark a deck.
								  False : Do not mark a deck.
			rFlag	(Boolean) 	: True	: Randomly mark deck.
								  False	: Mark bottom of deck.

		"""
		shuffle(self._deck)
		if mark:
			self._mark(rFlag)

	def show(self) :
		"""Shows the deck of cards.

		"""
		print('Deck:', self._deck)

	def draw(self) :
		"""Retrieves a card from the top of the deck.

		Returns:
			card 	(Card) 		: The card that was retrieved.
					(Boolean) 	: False	: The deck is empty.

		"""
		return self._pop()

	def burn(self, cards) :
		"""Return a used card to the deck.

		Args:
			card	(Card)		: The card to return.

		"""
		for card in cards :
			self._insert(card)

	@property
	def marker(self) :
		"""Returns a marker for comparison.

		"""
		return self._marker