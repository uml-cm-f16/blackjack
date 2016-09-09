#!/usr/bin/python3

from classes.deck import Deck
from classes.hand import Hand
from classes.card import Card


deck = Deck()
hand = Hand()

deck.shuffle()

print(deck)

for i in range(0, 5) :
	card = deck.draw()
	hand.add(card)

print(deck)
print(hand)

cards = hand.fold()
deck.burn(cards)

print(deck)
print(hand)