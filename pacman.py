# Txanton Bejos
# tbejos
# 15-112 Term Project
# 13 * 3 pixels

from pygame import *

class PacMan(object):

    def __init__(self, screen, name="PacMan"):
        self.screen = screen
        self.index = 0
        self.name = name
        self.LEFT = [image.load('images/%s/%sClosed.png' % (self.name, self.name)),
                     image.load('images/%s/%sLeft.png' % (self.name, self.name))]
        self.RIGHT = [image.load('images/%s/%sClosed.png' % (self.name, self.name)),
                      image.load('images/%s/%sRight.png' % (self.name, self.name))]
        self.UP = [image.load('images/%s/%sClosed.png' % (self.name, self.name)),
                   image.load('images/%s/%sUp.png' % (self.name, self.name))]
        self.DOWN = [image.load('images/%s/%sClosed.png' % (self.name, self.name)),
                   image.load('images/%s/%sDown.png' % (self.name, self.name))]

    def drawPacMan(self):
        x = 268
        self.screen.blit(self.RIGHT[self.index], (x, 20))
        self.screen.blit(self.LEFT[self.index], (x, 82))
        self.screen.blit(self.UP[self.index], (x, 144))
        self.screen.blit(self.DOWN[self.index], (x, 206))


    def update(self):
        if self.index == 1:
            self.index = 0
        else:
            self.index = 1