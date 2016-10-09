import sys
import pygame

class Display_Engine(object):
    '''
    Class that drives the displayed window and
    interactions with the window.
    '''

    '''
    buttonCoordinates = [(41, 950), (291, 950), (541, 950), (791, 950)]
    displayPlayerCards = [False]*11
    buttonSizes = [(90, 35), (83, 35), (185, 35), (97, 35)]
    buttonList = [None]*4
    playerCardCoordinates = [(32, 595), (242, 595), (472, 595), (512, 595), (552, 595),
    (592, 595), (632, 595), (672, 595), (712, 595), (752, 595), (792, 595)]
    screenCard = [None]*11
    screenSize = (1000, 1000)
    screen = None
    black = 0, 0, 0
    white = 255, 255, 255
    tableGreen = 46, 139, 87
    buttonText = ["Hit Me", "Stand", "Double Down", "Replay"]
    text1 = None
    text2 = None
    text3 = None
    text4 = None
    '''

    def __init__(self):
        pygame.init()

        self.buttonCoordinates = [(41, 950), (291, 950), (541, 950), (791, 950)]
        self.displayPlayerCards = [False]*11
        self.displayDealerCards = [False]*11
        self.buttonSizes = [(90, 35), (83, 35), (185, 35), (97, 35)]
        self.buttonList = [None]*4
        self.playerCardCoordinates = [(32, 595), (242, 595), (472, 595), (512, 595), (552, 595),
        (592, 595), (632, 595), (672, 595), (712, 595), (752, 595), (792, 595)]
        self.dealerCardCoordinates = [(32, 80), (242, 80), (472, 80), (512, 80), (552, 80),
        (592, 80), (632, 80), (672, 80), (712, 80), (752, 80), (792, 80)]
        self.screenCard = [None]*11
        self.screenSize = (1000, 1000)
        self.screen = pygame.display.set_mode((1000, 1000))
        self.black = 0, 0, 0
        self.white = 255, 255, 255
        self.tableGreen = 46, 139, 87
        self.buttonText = ["Hit Me", "Stand", "Double Down", "Replay"]
        self.text1 = None
        self.text2 = None
        self.text3 = None
        self.text4 = None

        font = pygame.font.Font(None, 40)
        self.text1 = font.render(self.buttonText[0], 0, self.black)
        self.text2 = font.render(self.buttonText[1], 0, self.black)
        self.text3 = font.render(self.buttonText[2], 0, self.black)
        self.text4 = font.render(self.buttonText[3], 0, self.black)
        
        for x in range(0, 11):
            temp = pygame.image.load("cards/king_of_clubs2.png")
            temp = pygame.transform.scale(temp, (190, 320))
            self.screenCard[x] = temp

        for x in range(0, 4):
            button = pygame.Rect(self.buttonCoordinates[x], self.buttonSizes[x])
            self.buttonList[x] = button

        pygame.display.set_caption("BlackJack")

    def clearBoard(self):
        '''
        Sets the card display values to false
        '''
        #for x in range(0, 11):
        self.displayPlayerCards = [False]*11
        print("Clear Board")
    
    def hitMe(self):
        i = 0
        while self.displayPlayerCards[i] and i < 10:
            i = i + 1
        self.displayPlayerCards[i] = True
        print("Hit")

    def stand(self):
        print("Stand")
    
    def doubleDown(self):
        print("Double Down")

    def run(self):
        font = pygame.font.Font(None, 40)
        while 1:
            x, y = -1, -1

            #Check for button clicks and user exiting the window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos

            self.screen.fill(self.tableGreen)

            #Drawing the four buttons on the screen
            for i in range(0, 4):
                pygame.draw.rect(self.screen, self.white, self.buttonList[i])

            #Check to see if the user clicked any buttons
            for i in range(0, 4):
                if self.buttonList[i].collidepoint(x, y):
                    if i == 0:
                        self.hitMe()
                        #Hit Me
                    if i == 1:
                        self.stand()
                        #Stand
                    if i == 2:
                        self.doubleDown()
                        #Double Down
                    if i == 3:
                        self.clearBoard()
                        #Replay
            
            #Draw the necessary cards on the screen
            for i in range(0, 11):
                if self.displayPlayerCards[i]:
                    self.screen.blit(self.screenCard[i], self.playerCardCoordinates[i])

            #Create the pygame text for displaying the percentage win
            percentageWin = "Chance to win: 12.344%" #replace none with get percentage win from game
            percentageWinText = font.render(percentageWin, 0, self.black)
            a = percentageWinText.get_rect().width
            #Draw the button text
            self.screen.blit(self.text1, self.buttonCoordinates[0])
            self.screen.blit(self.text2, self.buttonCoordinates[1])
            self.screen.blit(self.text3, self.buttonCoordinates[2])
            self.screen.blit(self.text4, self.buttonCoordinates[3])

            
            self.screen.blit(percentageWinText, (500 - a/2, 500))
            #Generate the window
            pygame.display.flip()