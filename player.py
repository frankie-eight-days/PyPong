import pygame
from pygame.locals import *

class player:

    def __init__(self, x, y, width, height, points, playerNumber):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.points = 0
        self.playerNumber = playerNumber

    def movement(self):
        self.y += self.keyboardActivity()

    def addPoint(self):
        self.points+=1

    def paint(self, display):
        pygame.draw.rect(display, (255, 0, 0), (self.x, self.y, self.width, self.height))
        font = pygame.font.Font(None, 18)
        scoreText = font.render("score:"+str(self.points), 1, (0,0,255))
        if self.playerNumber == 1:
            display.blit(scoreText, (self.x + 50, 20))
        if self.playerNumber == 2:
            display.blit(scoreText, (self.x - 50, 20))

    def keyboardActivity(self):
        deltaMove = 0
        keys = pygame.key.get_pressed()
        if keys[K_w]:
            deltaMove = -5
        if keys[K_s]:
            deltaMove = +5
        return deltaMove
