# Txanton Bejos
# tbejos
# 15-112 Term Project
# 13 * 3 pixels

from pygame import *

class PacMan(object):
    RIGHT = [image.load('images/PacManRight.png'),
             image.load('images/PacManClosed.png')]

    LEFT = [image.load('images/PacManLeft.png'),
             image.load('images/PacManClosed.png')]

    def __init__(self, screen):
        self.screen = screen
        self.index = 0

    def drawPacMan1(self):
        self.screen.blit(self.RIGHT[self.index], (268, 20))

    def drawPacMan2(self):
        self.screen.blit(self.LEFT[self.index], (268, 82))

    def update(self):
        if self.index == 1:
            self.index = 0
        else:
            self.index = 1

class MrsPacMan(PacMan):
    RIGHT = [image.load('images/PacManRight.png'),
             image.load('images/PacManClosed.png')]

    LEFT = [image.load('images/PacManLeft.png'),
            image.load('images/PacManClosed.png')]