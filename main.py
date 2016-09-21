#!/usr/bin/python3

from classes.logic.player import Player
from classes.logic.dealer import Dealer

def label(txt):
    print("**********")
    print(txt)
    print("**********")

def table(dealer, p):
    for i in range(0, pCount):
        print('-', p[i].name, p[i])
        print('-', dealer.name, dealer)

dealer = Dealer()
p = [Player()]
pCount = len(p)
value = { "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 10, "Q": 10, "K": 10, "A": 11}

dealer.shuffle()
#dealer.showDeck()

p[0].add(dealer.draw())
dealer.add(dealer.draw())

p[0].add(dealer.flip(dealer.draw()))
dealer.add(dealer.flip(dealer.draw()))

# show hands
label("Dealing")
table(dealer, p)
label("Flipping")
p[0].flip(0)
table(dealer, p)
print(p[0].total(value))
label("Hit")
p[0].add(dealer.flip(dealer.draw()))
table(dealer, p)
print(p[0].total(value))
# Fold
for i in range(0, pCount) :
	dealer.burn(p[i].fold())

dealer.burn(dealer.fold())

for i in range(0, pCount) :
	print('-', p[i].name, p[i])

print('-', dealer.name, dealer)