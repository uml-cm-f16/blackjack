#!/usr/bin/python3

from src.logic.player import Player
from src.logic.dealer import Dealer

def label(txt):
    print("\n---" + txt)

def table(dealer, p):
    for i in range(0, pCount):
        print("Player: ", p[0].total(value), " : ", p[i])
    print("Dealer: ", dealer.total(value), " : ", dealer)


dealer = Dealer()
p = [Player()]
pCount = len(p)

value = { False: 0, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 10, "Q": 10, "K": 10, "A": 11}
positive = ['y', 'Y']
bj = {0: False, 'dealer': False}

def getWinKeys(total):
    return list(filter(lambda x: 21 - total == value[x], value))

label("Shuffling.")
dealer.shuffle()

label("Dealing.")
p[0].add(dealer.draw())
dealer.add(dealer.draw())
p[0].add(dealer.flipDeal(dealer.draw()))
dealer.add(dealer.flipDeal(dealer.draw()))
table(dealer, p)

label("Players turn.")
label("Flipping player hidden card.")
p[0].flip(0)
table(dealer, p)

if p[0].total(value) == 21:
    bj[0] = True
else:

    def play():
        print("Hit again percent: ",
            dealer.percent(21 - p[0].total(value), value))
        prompt = "\nWould you like another card?[y/n]: "
        return input(prompt)

    while p[0].total(value) < 21 and play() in positive :
        print("")
        p[0].add(dealer.flipDeal(dealer.draw()))
        table(dealer, p)


    if p[0].total(value) <= 21:
        label("Dealers turn.")

        label("Flipping dealer hidden card.")
        dealer.flip(0)
        table(dealer, p)

        if dealer.total(value) == 21:
            bj['dealer'] = True
        else:
            while dealer.total(value) <= 16:
                label("Dealer hitting.")
                dealer.add(dealer.flipDeal(dealer.draw()))
                table(dealer, p)

if bj['dealer'] and bj[0]:
    print("***Both Blackjack - Draw***")
elif bj['dealer']:
    print("***Blackjack - Dealer Wins***")
elif bj[0]:
    print("***Blackjack - Player Wins***")
elif p[0].total(value) > 21 and dealer.total(value) > 21:
    print("***Both busted - Draw***")
elif p[0].total(value) > 21 and dealer.total(value) <= 21:
    print("***Player busted - Dealer wins***")
elif p[0].total(value) <= 21 and dealer.total(value) > 21:
    print("***Dealer busted - Player wins***")
elif p[0].total(value) == dealer.total(value):
     print("***Tie score - Draw***")
elif p[0].total(value) > dealer.total(value):
    print("***Higher score - Player Wins***")
elif p[0].total(value) < dealer.total(value):
    print("***Higher score - Dealer Wins***")
else:
    print("??? Missing Condition ???")

label("Folding hands")
dealer.burn(p[0].fold())
dealer.burn(dealer.fold())