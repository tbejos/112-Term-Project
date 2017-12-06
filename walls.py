# Txanton Bejos
# tbejos
# 15-112 Term Project

from pygame import *

class Wall(sprite.Sprite):

    def __init__(self, name, x, y):
        super().__init__()
        self.name = name
        self.image = image.load('images/Walls/%s.png' %
                                self.name)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class WallTile(Wall):

    def __init__(self, x=0, y=0):
        super().__init__("WallTile", x, y)

class HitBox(Wall):

    def __init__(self, x=0, y=0):
        super().__init__("HitBox", x, y)

class TeleportBlock(Wall):

    def __init__(self, x=0, y=0):
        super().__init__("TPBlock", x, y)

class Turn(Wall):

    def __init__(self, index, directions, x=0, y=0):
        super().__init__("Turn", x, y)
        self.index = index
        self.directions = directions