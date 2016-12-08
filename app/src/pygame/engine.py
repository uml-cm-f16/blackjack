#!/usr/bin/python3
""" Pygame driven game engine

"""
# IMPORTS

import sys
import os
from decimal import Decimal, ROUND_HALF_UP

import pygame

from ..logic.blackjack import Blackjack

# CLASS

class Engine(object):
    '''  Class that drives the displayed window and interactions with the window.

        Attributes
    '''

    _pips = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    _suits = ['H', 'S', 'D', 'C']


    def __init__(self):
        """ Initialize engine

        """

        pygame.init()

        # click instructions
        self._action = 0

        # Cards
        self.card_images = {}
        self.table_images = {}
        self.card_dir = os.path.join(os.path.dirname(__file__), "..", "..", "img", "cards")
        self.table_dir = os.path.join(os.path.dirname(__file__), "..", "..", "img", "table")
        self.card_dimensions = (190, 320)
        self.card_back = '-_-'


        # Players
        self.dealer_cards = []
        self.dealer_values = []
        self.player_cards = []
        self.player_values = []
        self.dealer_closest = self.player_closest = 0
        self.dealer_percentage = self.player_percentage = 100.00
        self.result_active = False
        self.player_result = 0
        self.player_stats = []
        self.dealer_stats = []

        self.person_x = [32, 242, 472, 512, 552, 592, 632, 672, 712, 752, 792]
        self.dealer_y = 40
        self.player_y = 440

        # Buttons
        self.button_list = []
        self.button_active = [False, False, False, False]
        self.percent_active = False
        self.button_text_str = ["Hit",
                                "Stay",
                                "Double Down",
                                "Replay"]
        self.button_text_func = [self._flag_hit,
                                 self._flag_stand,
                                 self._flag_double_down,
                                 self._flag_replay]
        self.button_x = [77, 289, 541, 823]
        self.button_y = 380
        self.button_w = [100, 100, 100, 100]
        self.button_h = 35

        # Screen
        self.screen = pygame.display.set_mode((1000, 800))
        self.screen_title = "BlackJack"

        # colors
        self.color_black = 0, 0, 0
        self.color_white = 255, 255, 255
        self.color_green = 46, 139, 87
        self.color_blue = 0, 83, 160
        self.color_333 = 51, 51, 51
        self.color_red = 210, 0, 0
        self.color_orange = 255, 128, 0

        # object styling
        self.font = pygame.font.Font(pygame.font.match_font('Verdana'), 20)
        self.color_background_button = self.color_blue
        self.color_background_table = self.color_333

         # Build person coordinates
        self.player_cards_coordinates = list(map(lambda x: (x, self.player_y), self.person_x))
        self.dealer_cards_coordinates = list(map(lambda x: (x, self.dealer_y), self.person_x))

        # Building card images
        for pip in self._pips:
            for suit in self._suits:
                self._add_card(pip, suit)
        self._add_card('-', '-')

        # Building table images
        self._add_table("table_dealer", (530, 340))
        self._add_table("table_player", (530, 340))
        self._add_table("splash", (530, 340))
        self._add_table("single", (210, 340))


        # Building buttons
        for button in list(map(lambda s, func, x, w:
                               (s, func, (x, self.button_y), (w, self.button_h)),
                               self.button_text_str, self.button_text_func,
                               self.button_x, self.button_w)):
            self._add_button(button)

    # Private methods
    def _format(self, val, format='.001', method=ROUND_HALF_UP):
        """ Formats to specific decimal spaces

        Args:
            val: (decimal): The number to truncate
            format: (str): ".001": The decimal spot to show up to.
            method: (enum): ROUND_HALF_UP: How to truncate val

        Returns:
            (float): The truncated float

        """
        return float(Decimal(val.quantize(Decimal('.001'), method)))

    def _add_table(self, table_file_name, size):
        """ Table images

        """
        table = os.path.join(self.table_dir, table_file_name + ".png")
        img_src = pygame.image.load(table)
        img_src_sized = pygame.transform.scale(img_src, size)
        self.table_images.update({table_file_name: img_src_sized})

    def _add_card(self, pip, suit):
        """ Adds a card file to the images

        """
        card_name = pip + "_" + suit
        card_filepath = os.path.join(self.card_dir, card_name + ".png")
        img_src = pygame.image.load(card_filepath)
        img_src_sized = pygame.transform.scale(img_src, self.card_dimensions)
        self.card_images.update({card_name: img_src_sized})

    def _add_button(self, button):
        self._b_terms = {
            "BUTTON_STR": 0,
            "BUTTON_FUNC": 1,
            "BUTTON_COORDINATES": 2,
            "BUTTON_DIM": 3,
            "BUTTON_PY_RECT": 4,
            "BUTTON_PY_TEXT": 5,
            "BUTTON_PY_TEXT_COORDS": 6
        }

        text = self.font.render(button[self._b_terms["BUTTON_STR"]],
                                True, self.color_white)

        size = self.font.size(button[self._b_terms["BUTTON_STR"]])
        centering = (50 + button[self._b_terms["BUTTON_COORDINATES"]][0] - (size[0] / 2),
                     18 + button[self._b_terms["BUTTON_COORDINATES"]][1] - (size[1] / 2))


        rect = pygame.Rect(button[self._b_terms["BUTTON_COORDINATES"]],
                           button[self._b_terms["BUTTON_DIM"]])

        self.button_list.append([button[self._b_terms["BUTTON_STR"]],
                                 button[self._b_terms["BUTTON_FUNC"]],
                                 button[self._b_terms["BUTTON_COORDINATES"]],
                                 button[self._b_terms["BUTTON_DIM"]],
                                 rect,
                                 text,
                                 centering])

    def _card_name(self, card):
        """ The string name of a card file

        """
        if card.pip is False:
            return self.card_back
        return card.pip + '_' + card.suit

    def _flag_hit(self):
        """ Hit request made

        """
        print("hit")
        self._action = 1

    def _flag_stand(self):
        """ Stand request made

        """
        print("stay")
        self._action = 2

    def _flag_clear(self):
        """ Clear request made

        """
        print("clear")
        self._action = 3

    def _flag_double_down(self):
        """ Double down request made

        """
        print("D_D")
        self._action = 4

    def _flag_replay(self):
        """ Replay request made

        """
        print("replay")
        self._action = 5

    # Public properties
    @property
    def action(self):
        """ Retrieve pending request and reset request

        """
        ret = self._action
        self._action = 0
        return ret

    # Public methods
    def update(self, stats):
        """ Updates a players hand

        """
        if stats[0] == -1:
            self.dealer_cards = stats[1]
            self.dealer_values = stats[2]
            self.dealer_closest = stats[3]
            self.dealer_percentage = stats[4]
        else:
            self.player_cards = stats[1]
            self.player_values = stats[2]
            self.player_closest = stats[3]
            self.player_percentage = stats[4]

    def clear_board(self):
        """ Sets the card display values to false

        """
        self.dealer_cards = []
        self.dealer_values = []
        self.player_cards = []
        self.player_values = []
        self.dealer_closest = self.player_closest = 0
        self.dealer_percentage = self.player_percentage = 100.00

        print("Clear Board")

    def update_frame(self, delay=0):
        """ Game frame
        """
        coordinate = -1, -1

        # Check for button clicks and user exiting the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                coordinate = event.pos

        # Draw Table
        self.screen.fill(self.color_background_table)

        # Drawing the four buttons on the screen and checking for click
        for index, button in enumerate(self.button_list):
            if self.button_active[index] is True:
                pygame.draw.rect(self.screen,
                                 self.color_background_button,
                                 button[self._b_terms["BUTTON_PY_RECT"]])

                self.screen.blit(button[self._b_terms["BUTTON_PY_TEXT"]],
                                 button[self._b_terms["BUTTON_PY_TEXT_COORDS"]])

                if button[self._b_terms["BUTTON_PY_RECT"]].collidepoint(coordinate):
                    button[self._b_terms["BUTTON_FUNC"]]()

        # Draw the necessary cards on the screen
        self.screen.blit(self.table_images["table_dealer"],
                         (self.person_x[2] - 10, self.dealer_y - 10))
        self.screen.blit(self.table_images["table_player"],
                         (self.person_x[2] - 10, self.player_y - 10))

        self.screen.blit(self.table_images["single"],
                         (self.person_x[0] - 10, self.player_y - 10))
        self.screen.blit(self.table_images["single"],
                         (self.person_x[1] - 10, self.player_y - 10))

        self.screen.blit(self.table_images["single"],
                         (self.person_x[0] - 10, self.dealer_y - 10))
        self.screen.blit(self.table_images["single"],
                         (self.person_x[1] - 10, self.dealer_y - 10))

        for index, card in enumerate(self.dealer_cards):
            self.screen.blit(self.card_images[self._card_name(card)],
                             self.dealer_cards_coordinates[index])

        for index, card in enumerate(self.player_cards):
            self.screen.blit(self.card_images[self._card_name(card)],
                             self.player_cards_coordinates[index])

        # Create the pygame text for displaying the percentage win
        if self.percent_active is True:
            bust = self._format(Decimal(100 - self.player_percentage))
            percentage_win = "(Bust on hit " + str(bust) + "%)"

            # Variant Warning red
            if bust <= 50:
                color = self.color_green
            elif bust <= 85:
                color = self.color_orange
            else:
                color = self.color_red

            percentage_win_text = self.font.render(percentage_win, 0, color)
            percentage_win_text_w = percentage_win_text.get_rect().width
            percentage_win_text_h = percentage_win_text.get_rect().height
            self.screen.blit(percentage_win_text,
                             (606 - percentage_win_text_w/2,
                              397.5 - percentage_win_text_h / 2))

            results_text = self.font.render(str(self.player_stats[2]), 0, self.color_white)
            results_text_text_w = results_text.get_rect().width
            results_text_text_h = results_text.get_rect().height
            self.screen.blit(results_text,
                             (875 - results_text_text_w/2,
                              397.5 - results_text_text_h / 2))
        # Who won
        if self.result_active is True:
            result = self.player_result
            player = self.player_stats[3]
            dealer = self.dealer_stats[3]

            result_text = "result: "
            color = self.color_black
            outcome = "DRAW"

            # Variant Warning red
            if result == -1:
                color = self.color_red
                outcome = "LOSS"
            elif result == 1:
                color = self.color_green
                outcome = "WIN"

            result_text = self.font.render(outcome + " with " + str(player) +
                                           " to " + str(dealer), 0, color)
            result_text_w = result_text.get_rect().width
            result_text_h = result_text.get_rect().height
            self.screen.blit(result_text,
                             (606 - result_text_w/2,
                              397.5 - result_text_h / 2))
        # Generate the window
        pygame.display.flip()
        pygame.time.wait(delay)

    def run(self):
        """ run

        """
        def print_player(ret):
            """l"""
            number = ret[0]
            hand = str(ret[1])
            values = ret[2]
            closest = ret[3]
            percent = ret[4]

            print(number, hand, values, closest, percent)

        # Build window
        pygame.display.set_caption(self.screen_title)

        # Draw splash
        self.screen.fill(self.color_background_table)
        self.screen.blit(self.table_images["splash"], (235, 400 - 170))
        pygame.display.flip()
        pygame.time.wait(2000)

        self.screen.fill(self.color_background_table)
        pygame.display.flip()
        pygame.time.wait(1000)

        while True:

            # Load Blackjack game
            bj_game = Blackjack(1)

            self.button_active[0] = False
            self.button_active[1] = False
            self.button_active[2] = False
            self.button_active[3] = False
            self.percent_active = False
            self.result_active = False

            self.update_frame(1000)

            # Start game
            ret = bj_game.round_start()

            deal_player_2 = list(ret[0])
            deal_player_2[1] = deal_player_2[1][0:2]

            deal_player_1 = list(ret[0])
            deal_player_1[1] = deal_player_1[1][0:1]

            deal_dealer_2 = list(ret[1])
            deal_dealer_2[1] = deal_dealer_2[1][0:2]

            deal_dealer_1 = list(ret[1])
            deal_dealer_1[1] = deal_dealer_1[1][0:1]

            # Deal initial hands
            self.update(deal_player_1)
            self.update_frame(500)

            self.update(deal_dealer_1)
            self.update_frame(500)

            self.update(deal_player_2)
            self.update_frame(500)

            self.update(deal_dealer_2)
            self.update_frame(500)

            self.update_frame(500)

            # Full start
            self.update(ret[0])
            self.update_frame(500)

            self.update(ret[1])
            self.update_frame()

            play = True
            while play is True:
                cont = True
                ret = bj_game.player_start()

                self.button_active[0] = True
                self.button_active[1] = True
                self.button_active[3] = False

                self.update(ret)
                self.update_frame(500)

                while cont is True:
                    print_player(ret)

                    self.update(ret)
                    self.update_frame(500)
                    self.percent_active = True
                    self.player_stats = ret

                    action = self.action
                    # hit
                    if action == 1:
                        cont = True

                        self.button_active[0] = True
                        self.button_active[1] = True
                        self.button_active[3] = False
                        self.percent_active = True

                        ret = bj_game.player_hit()
                        self.update(ret)
                        self.update_frame(0)

                    # stand
                    elif action == 2:
                        cont = False

                        self.button_active[0] = False
                        self.button_active[1] = False
                        self.button_active[3] = False
                        self.percent_active = True

                        ret = bj_game.player_stay()
                        self.update(ret)
                        self.update_frame(0)

                    # bust
                    if ret[3] > 21:
                        cont = False

                        self.button_active[0] = False
                        self.button_active[1] = False
                        self.button_active[3] = True
                        self.percent_active = True

                        ret = bj_game.player_stay()
                        self.update(ret)
                        self.update_frame(0)

                    # player end turn
                    if cont is False:
                        self.button_active[0] = False
                        self.button_active[1] = False
                        self.button_active[3] = False
                        self.percent_active = False

                bj_game.player_end()

                if bj_game.player_current == -1:
                    play = False

            round_result = bj_game.round_end()

            ret = bj_game.dealer_stats()
            self.update(ret)
            self.update_frame(500)

            dealer = self.dealer_stats = round_result[1]
            player = self.player_stats = round_result[0]

            state = "DRAW"
            self.player_result = player[5]
            if player[5] == 1:
                state = "WON"
            elif player[5] == -1:
                state = "LOST"
            print("player ", player[0], " ", state, " with ", player[1],
                  " to dealers ", dealer[1])

            self.result_active = True
            self.button_active[3] = True
            replay = True
            while replay is True:
                print('waiting')
                self.update_frame(500)
                if self.action == 5:
                    replay = False

            del bj_game

            self.clear_board()
            self.update_frame()
