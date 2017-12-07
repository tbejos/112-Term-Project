# Txanton Bejos
# tbejos
# 15-112 Term Project
# 14 * 3 pixels

from pygame import *

class PacMan(sprite.Sprite):
    # Amount PacMan moves per tick
    MOVES = {"Left":(-1, 0),
                  "Right":(1, 0),
                  "Up":(0, -1),
                  "Down":(0, 1)}

    def __init__(self, name="PacMan"):
        super().__init__()
        self.name = name
        self.direction = "Left"
        self.index = 43
        self.count = 0
        self.powerpellet = False
        self.lives = 3
        self.score = 0
        self.turn = None
        self.ghost = mixer.Sound('sounds/pacman_eatghost.wav')
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
        if self.count == 1:
            self.image = self.open[self.direction]
            self.count = 0
        else:
            self.image = self.backup
            self.count = 1
        x, y = self.rect.x, self.rect.y
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def movement(self):
        self.rect.x += self.MOVES[self.direction][0]
        self.rect.y += self.MOVES[self.direction][1]

    def ghostCheck(self, ghostGroup): # True or False
        collisionList = sprite.spritecollide(self, ghostGroup.sprites(), False)
        # If touching >= 1 ghost
        if self.powerpellet:
            for ghost in collisionList:
                if not ghost.start:
                    self.ghost.play()
                    self.score += 400
                ghost.start = True
        else:
            for ghost in collisionList:
                if ghost.rect.y == self.rect.x and ghost.rect.x in range(
                        self.rect.x - 24, self.rect.x + 25):
                    if not ghost.start:
                        return True
                if ghost.rect.x == self.rect.x and ghost.rect.y in range(
                        self.rect.y - 24, self.rect.y + 25):
                    if not ghost.start:
                        return True
        return False

    def switchDirection(self):
        if self.direction == "Up":
            self.direction = "Down"
        elif self.direction == "Down":
            self.direction = "Up"
        elif self.direction =="Left":
            self.direction = "Right"
        elif self.direction == "Right":
            self.direction = "Left"

    def setPosition(self, x, y):
        self.rect.x = x
        self.rect.y = y

