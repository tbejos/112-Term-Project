# Txanton Bejos
# tbejos
# 15-112 Term Project

from pygame import *

class Wall(sprite.Sprite):

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.image = image.load('images/Walls/%s.png' %
                                self.name)
        self.rect = self.image.get_rect()
        self.rect.x = 252
        self.rect.y = 372

class GhostBox(Wall):

    def __init__(self):
        super().__init__("GhostBox")