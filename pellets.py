# Txanton Bejos
# tbejos
# 15-112 Term Project

# Should be 21 pixels away from each other

from pygame import *

class Pellet(object):

    def __init__(self, screen, name="Pellet"):
        self.screen = screen
        self.name = name
        self.IMAGE = image.load('images/Pellets/%s.png'% self.name)

    def draw(self, x, y):
        self.screen.blit(self.IMAGE, (x, y))

class PowerPellet(Pellet):

    def __init__(self, screen):
        super().__init__( screen, "PowerPellet")