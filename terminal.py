#!/usr/bin/python3
""" Terminal application
"""

from app.src.logic.blackjack import Blackjack

def print_ret(msg, ret):
    """ prints out a player return statement

    Args:
        msg: (str): The player or dealer label
        ret: (list 5): The return statement of the blackjack game steps

    """
    print("")
    print("   ---", msg, "---")
    print("\t", str(ret[1]))
    print("\t", "Scores: ", ret[2])
    if msg == 'Player':
        print("\t", "Bust on hit %: ", ret[4])

def main():
    """ The terminal version of the application, Runs blackjack

    """
    # Load Blackjack game
    blackjack = Blackjack(1)

    # Begin application
    game = True
    while game is True:

        # DEALING

        ret = blackjack.round_start()
        print_ret('Dealer', ret[1])

        # Player game loop for a round
        play = True
        while play is True:

            cont = True
            ret = blackjack.player_start()
            print_ret('Player', ret)

            # Player game loop for a hand
            while cont is True:

                prompt = input("\nDo you want another card?: [Y/y] ")

                # hit
                if prompt in ['Y', 'y']:
                    cont = True
                    ret = blackjack.player_hit()

                # stand
                else:
                    cont = False
                    ret = blackjack.player_stay()

                # bust
                if ret[3] > 21:
                    cont = False
                    ret = blackjack.player_stay()
                    print("\n   --- Busted ---")

                print_ret('Player', ret)

            # End players turn
            blackjack.player_end()

            # If dealer end round game loop
            if blackjack.player_current == -1:
                play = False

        # Dealers turn
        round_result = blackjack.round_end()

        # Update dealers information
        ret = blackjack.dealer_stats()

        # Draw frame
        print_ret('Dealer', ret)

        # Calculate winner
        dealer = round_result[1]
        player = round_result[0]

        state = "DRAW"
        if player[5] == 1:
            state = "WON"
        elif player[5] == -1:
            state = "LOST"

        print("\n   ---player ", state, " with ", player[1], " <=> ", player[3],
              "\n      to dealers ", dealer[1], " <=> ", dealer[3], "---\n")

        prompt = input("\nDo you want to play Again card?: [Y/y] ")
        if prompt in ['Y', 'y']:
            game = True
        else:
            game = False

        blackjack.round_reset()

# start main function
if __name__ == "__main__":
    main()
