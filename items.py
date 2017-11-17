# Txanton Bejos
# tbejos
# 15-112 Term Project

# Should be 21 pixels away from each other

from pygame import *

class Item(sprite.Sprite):

    def __init__(self, name, points):
        super().__init__()
        self.name = name
        self.points = points

        self.image = image.load('images/items/%s.png'% self.name)

        self.rect = self.image.get_rect()

    def setPosition(self, x, y):
        self.rect.x = x
        self.rect.y = y



class Pellet(Item):

    def __init__(self):
        super().__init__("Pellet", 10)

class PowerPellet(Item):

    def __init__(self):
        super().__init__("PowerPellet", 50)
        self.other = Surface((42, 42))

    def update(self):   # Only Power Pellet blinks
        temp = self.image
        self.image = self.other
        self.other = temp
        x, y = self.rect.x, self.rect.y
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

class Cherry(Item):

    def __init__(self):
        super().__init__("Cherry", 100)