# Txanton Bejos
# tbejos
# 15-112 Term Project
# 14 * 3 pixels

from pygame import *

class PacMan(sprite.Sprite):
    DIRECTIONS = {"Left":(-10, 0),
                  "Right":(10, 0),
                  "Up":(0, -10),
                  "Down":(0, 10)}

    def __init__(self, name="PacMan"):
        super().__init__()
        self.name = name
        self.direction = "Left"
        self.index = 1
        self.powerpellet = False
        self.wall = False

        self.image = image.load('images/%s/%sClosed.png' % (self.name,
                                                           self.name))
        self.backup = self.image # Backup of closed so that we can update
        self.open = {"Left":image.load('images/%s/%sLeft.png' % (self.name,
                                                                 self.name)),
                      "Right": image.load('images/%s/%sRight.png' % (self.name,
                                                                     self.name)),
                      "Up":image.load('images/%s/%sUp.png' % (self.name,
                                                              self.name)),
                      "Down":image.load('images/%s/%sDown.png' % (self.name,
                                                                  self.name))}
        self.rect = self.image.get_rect()

    def update(self):
        if self.index == 1 or self.wall:
            self.image = self.open[self.direction]
            self.index = 0
        else:
            self.image = self.backup
            self.index = 1
            self.movement()
        x, y = self.rect.x, self.rect.y
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def movement(self):
        self.rect.x += self.DIRECTIONS[self.direction][0]
        self.rect.y += self.DIRECTIONS[self.direction][1]

    def setPosition(self, x, y):
        self.rect.x = x
        self.rect.y = y
