import pygame
from player import *
from ball import *

pygame.init()
windowWidth = 600
windowHeight = 400
display = (windowWidth, windowHeight)
gameDisplay = pygame.display.set_mode(display)
pygame.display.set_caption("Pong Maybe?")
clock = pygame.time.Clock()

player1 = player(0, 0, 20, 100, 0, 1)
player2 = player(windowWidth - 20, 100, 20, 100, 0, 2)
ball = ball(200, 200, 10, 10)

def main():
    crashed = False
    timer = 0

    ##########  GAME LOOP  #################
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

        pygame.display.update()
        clock.tick(60)
        gameDisplay.fill((255, 255, 255))

        updateGraphics()
        updateGame()



    ###### WHEN THE GAME QUITS#####
    pygame.quit()
    quit()

def updateGame():
    player1.movement()
    player2.movement()
    ball.movement()
    ball.screenDetection(windowWidth, windowHeight)
    ball.paddleDetection(player1)
    ball.paddleDetection(player2)
    ball.makePoints(player1, player2, windowWidth)

def updateGraphics():
    player1.paint(gameDisplay)
    player2.paint(gameDisplay)
    ball.paint(gameDisplay)

main()