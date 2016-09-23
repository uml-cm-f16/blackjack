import sys
import pygame

pygame.init()
# max cards allowed in hand = 11
# Four Aces, Four 2s Three 3s

coords = [(41, 950), (291, 950), (541, 950), (791, 950)]  #coordinates for the buttons
boxSize = (100, 30)
rectList = [None]*5      #list of buttons to draw

#coordinates for all the cards
cardcoords = [(32, 595), (242, 595), (472, 595), (512, 595), (552, 595),
(592, 595), (632, 595), (672, 595), (712, 595), (752, 595), (792, 595)]

images = [None]*11
for x in range(0, 11):
    temp = pygame.image.load("ace_of_spades.png")
    temp = pygame.transform.scale(temp, (185, 310))
    images[x] = temp

for x in range(0, 4):  #from 0 to 4, make buttons to put in array
    button = pygame.Rect(coords[x], boxSize)
    rectList[x] = button
size = width_, height_ = 1000, 1000
black = 0, 0, 0
white = 255, 255, 255
tablegreen = 46, 139, 87
showCard = False
showCard2 = False
dealerBust = "Dealer Bust"
dealerWin = "Dealer Win"
playerBust = "Player Bust"
playerWin = "Player Win"

'''
button1 = pygame.Rect(coords[1], boxSize)
button2 = pygame.Rect(100, 500, 90, 30)
button3 = pygame.Rect(500, 100, 90, 30)
button4 = pygame.Rect(500, 500, 90, 30)
button5 = pygame.Rect(700, 50, 90, 30)
'''

screen = pygame.display.set_mode(size)

hitMe = "Hit Me"
stand = "Stand"
doubleDown = "Double Down"
replay = "Replay"
font = pygame.font.Font(None, 40)
text1 = font.render(string, 0, black)

while 1:
    x, y = -1, -1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
    screen.fill(tablegreen)

    #Drawing the five buttons on the screen
    for i in range(0, 4):
        pygame.draw.rect(screen, white, rectList[i], 0)
    #pygame.draw.rect(screen, white, button1, 0)
    #pygame.draw.rect(screen, white, button2, 0)
    #pygame.draw.rect(screen, white, button3, 0)
    #pygame.draw.rect(screen, white, button4, 0)
    #pygame.draw.rect(screen, white, button5, 0)

    #Checking to see if the user clicked any of the buttons
    for i in range(0, 4):
        tempRect = rectList[i]
        if tempRect.collidepoint(x, y):
            print("Button {0} clicked".format(i+1))
            if i == 0:
                showCard = True
            if i == 1:
                showCard = False
            if i == 2:
                showCard2 = True
            if i == 3:
                showCard2 = False

    for x in range(0, 11):
        if x == 0 or x == 1:
            if x == 0:
                if showCard:
                    screen.blit(images[x], cardcoords[x])
            if x == 1:
                if showCard2:
                    screen.blit(images[x], cardcoords[x])
        else:
            screen.blit(images[x], cardcoords[x])

    screen.blit(text1, coords[1])
    pygame.display.flip()
