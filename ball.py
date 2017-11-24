import pygame
from random import *

class ball:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.movementSpeed = [4, 4]

    def movement(self):
        self.x += self.movementSpeed[0]
        self.y += self.movementSpeed[1]

    def screenDetection(self, windowWidth, windowHeight):
        if self.y > windowHeight or self.y < 0:
            self.movementSpeed[1]*=-1

    def makePoints(self, player1, player2, windowWidth):
        if self.x - self.width/2 > windowWidth:
            player1.addPoint()
            self.reset(windowWidth)

        if self.x + self.width/2 < 0:
            player2.addPoint()
            self.reset(windowWidth)

    def reset(self, windowWidth):
        self.y = randint(1, windowWidth/2)
        self.x = windowWidth/2

        yDirection = randint(0, 1)
        xDirection = randint(0, 1)
        if yDirection == 0:
            yDirection*=-1
        if xDirection == 0:
            xDirection*= -1


    def paddleDetection(self, paddle):
        x = self.x
        y = self.y
        width = self.width
        height = self.height

        if x + width/2 >= paddle.x and x - width/2 <= paddle.x + width:
            if y + height/2 >= paddle.y and y <= paddle.y + paddle.height:
                self.movementSpeed[0]*=-1

    def paint(self, display):
        pygame.draw.circle(display, (0,255,0), (self.x ,self.y), self.width, self.height)