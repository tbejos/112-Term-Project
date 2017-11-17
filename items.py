# Txanton Bejos
# tbejos
# 15-112 Term Project

# Should be 21 pixels away from each other

from pygame import *

class Item(object):

    def __init__(self, screen, name, points):
        self.screen = screen
        self.name = name
        self.points = points
        self.IMAGE = image.load('images/items/%s.png'% self.name)

    def drawItem(self, x, y):
        self.screen.blit(self.IMAGE, (x, y))

class Pellet(Item):

    def __init__(self, screen):
        super().__init__(screen, "Pellet", 10)

class PowerPellet(Item):

    def __init__(self, screen):
        super().__init__( screen, "PowerPellet", 50)

class Cherry(Item):

    def __init__(self, screen):
        super().__init__(screen, "Cherry", 100)