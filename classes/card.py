#!/usr/bin/python3

# 	@author Jose Flores

#	IMPORTS
from string import Template

class Card:
	'''Generates a card and its property accesors.

	Cards have a pip and a suit, it is the responsibility of the logic
	interpreter to determine the value of a Card.

	'''
	def __init__(self, pip, suit) :
		''' Generate a Card

		Args:
			pip 	(String): The shown value of the card.
			suit 	(String): The shown suit of the card.

		'''
		self._pip = pip
		self._suit = suit

	def __repr__(self):
		'''The representation of a Card.

		'''
		tmp = Template('$pip $suit')
		return tmp.substitute(pip=self.pip, suit=self.suit)

	@property
	def pip(self) :
		'''	Getter for card pip value.

		'''
		return self._pip

	@property
	def suit(self) :
		'''Getter for card suit value.

		'''
		return self._suit