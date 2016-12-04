#!/usr/bin/python3
""" Runs a black jack game using the Blackjack class

"""
from decimal import Decimal, ROUND_HALF_UP

from src.logic.blackjack import Blackjack

def main():
    """main"""
    def print_player(ret):
        """l"""
        number = ret[0]
        hand = str(ret[1])
        values = ret[2]
        closest = ret[3]
        percent = ret[4]

        print(number, hand, values, closest, percent)

    print("\nStart game")

    bj = Blackjack(1)

    print("\nDealing")
    for r in bj.round_start():
        print(r[0], r[1])

    play = True
    while play is True:
        ret = bj.player_start() # p0
        cont = True

        while cont is True:
            print_player(ret)
            prompt = input("\nWould you like another card?[y/n]: ")
            if prompt in ['y', 'Y']:
                cont = True
                ret = bj.player_hit()
            else:
                cont = False
                ret = bj.player_stay()

            if ret[3] > 21:
                print("bust")
                cont = False
                ret = bj.player_stay()

            if cont is False:
                print("player end turn")
                print_player(ret)
                ret = bj.player_end()

        if bj.player_current == -1:
            play = False
    print("\nRound results")
    ret = bj.round_end()

    for r in ret:
        if r[0] == -1:
            dealer = r[1]

    for r in ret:
        if r[0] == -1:
            return
        elif r[2] == 1:
            state = "WON"
        elif r[2] == -1:
            state = "LOST"
        elif r[2] == 0:
            state = "DRAW"
        print("player ", r[0], " ", state, " with ", r[1], " to dealers ", dealer)


if __name__ == '__main__':
    main()
