# Txanton Bejos
# tbejos
# 15-112 Term Project
# 14 * 3 pixels

from pygame import *

class PacMan(sprite.Sprite):
    # Amount PacMan moves per tick
    DIRECTIONS = {"Left":(-5, 0),
                  "Right":(5, 0),
                  "Up":(0, -5),
                  "Down":(0, 5)}

    def __init__(self, name="PacMan"):
        super().__init__()
        self.name = name
        self.direction = "Left"
        self.index = 1
        self.powerpellet = False
        self.lives = 3
        self.score = 0

        self.image = image.load('images/%s/%sClosed.png' % (self.name,
                                                           self.name))
        self.backup = self.image # Backup of closed so that we can update()
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
        if self.index == 1:
            self.image = self.open[self.direction]
            self.index = 0
        else:
            self.image = self.backup
            self.index = 1
        x, y = self.rect.x, self.rect.y
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def movement(self):
        self.rect.x += self.DIRECTIONS[self.direction][0]
        self.rect.y += self.DIRECTIONS[self.direction][1]

    # TODO: Move collision checks to game.py
    def wallCheck(self, wallGroup):
        collisionList = sprite.spritecollide(self, wallGroup.sprites(), False)
        # If horizontal collision
        for hitObject in collisionList:
            if self.DIRECTIONS[self.direction][0] > 0:
                self.rect.right = hitObject.rect.left
            elif self.DIRECTIONS[self.direction][0] < 0:
                self.rect.left = hitObject.rect.right
        # Have to redefine list since sprite may have moved in last loop
        collisionList = sprite.spritecollide(self, wallGroup.sprites(), False)
        # If vertical collision
        for hitObject in collisionList:
            if self.DIRECTIONS[self.direction][1] > 0:
                self.rect.bottom = hitObject.rect.top
            elif self.DIRECTIONS[self.direction][1] < 0:
                self.rect.top = hitObject.rect.bottom

    # TODO: Move collision checks to game.py
    def ghostCheck(self, ghostGroup): # True or False
        collisionList = sprite.spritecollide(self, ghostGroup.sprites(), False)
        # If touching >= 1 ghost
        return len(collisionList) > 0

    # TODO: Move collision checks to game.py
    def itemCheck(self, itemGroup):
        collisionList = sprite.spritecollide(self, itemGroup.sprites(), False)
        for item in collisionList:
            self.score += item.points
            item.kill()

    def setPosition(self, x, y):
        self.rect.x = x
        self.rect.y = y
