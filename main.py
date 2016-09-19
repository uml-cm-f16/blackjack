#!/usr/bin/python3

from classes.player import Player
from classes.dealer import Dealer

dealer = Dealer()
p = [Player()]
playerCount = len(p)

dealer.shuffle()
dealer.showDeck()


p[0].add(dealer.draw())
dealer.add(dealer.draw())

p[0].add(dealer.flip(dealer.draw()))
dealer.add(dealer.flip(dealer.draw()))

for i in range(0, playerCount) :
	print('-', p[i].name, p[i])

print('-', dealer.name, dealer)

for i in range(0, playerCount) :
	dealer.burn(p[i].fold())

dealer.burn(dealer.fold())

for i in range(0, playerCount) :
	print('-', p[i].name, p[i])

print('-', dealer.name, dealer)