#!/usr/bin/python3

from string import Template

class Card(object):
	"""Generates a card and its property accesors.

	Cards have a pip and a suit, it is the responsibility of the logic
	interpreter to determine the value of a Card.

	"""
	def __init__(self, pip, suit) :
		""" Generate a Card

		Args:
			pip 	(String): The shown value of the card.
			suit 	(String): The shown suit of the card.

		"""
		self._pip = pip
		self._suit = suit
		self._hidden = True
		super(Card, self).__init__()

	def __str__(self):
		"""The representation of a Card.

		"""
		tmp = Template("[$pip$suit]")
		if self._hidden:
			return tmp.substitute(pip='<', suit='>')

		return tmp.substitute(pip=self.pip, suit=self.suit)

	def flip(self):
		self._hidden = not self._hidden

	@property
	def pip(self) :
		"""	Getter for card pip value.

		"""
		return self._pip

	@property
	def suit(self) :
		"""Getter for card suit value.

		"""
		return self._suit