# Txanton Bejos
# tbejos
# 15-112 Term Project

# He stated that the red enemy chases Pac-Man,
# and the pink enemy aims for a position in front of Pac-Man's mouth.
# The blue enemy is "fickle" and sometimes heads towards Pac-Man, and
# other times away. Although he claimed that the
# orange enemy's behavior is random, in actuality it alternates from behaving
# like the red enemy when at some distance from Pac-Man and aiming towards the
# lower-left corner of the maze whenever it gets too close to him.

from pygame import *

class GhostSprite(sprite.Sprite):
    # Amount ghosts move per tick
    DIRECTIONS = {"Left": (-3, 0),
                  "Right": (3, 0),
                  "Up": (0, -3),
                  "Down": (0, 3)}

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.direction = "Left"
        self.index = 0

        self.image = image.load('images/Ghost Sprites/%s%sA.png' % (self.name,
                                                           self.direction))
        self.other = \
            {"Left":
              [image.load('images/Ghost Sprites/%sLeftA.png' % self.name),
               image.load('images/Ghost Sprites/%sLeftB.png' % self.name)],
              "Right":
                  [image.load('images/Ghost Sprites/%sRightA.png' % self.name),
                   image.load('images/Ghost Sprites/%sRightB.png' % self.name)],
              "Up":
                  [image.load('images/Ghost Sprites/%sUpA.png' % self.name),
                   image.load('images/Ghost Sprites/%sUpB.png' % self.name)],
              "Down":
                  [image.load('images/Ghost Sprites/%sDownA.png' % self.name),
                   image.load('images/Ghost Sprites/%sDownB.png' % self.name)]}

        self.rect = self.image.get_rect()

    def update(self):
        if self.index == 0:
            self.index = 1
        else:
            self.index = 0
        self.image = self.other[self.direction][self.index]
        x, y = self.rect.x, self.rect.y
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def setPosition(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def movement(self):
        self.rect.x += self.DIRECTIONS[self.direction][0]
        self.rect.y += self.DIRECTIONS[self.direction][1]

    def switchDirection(self):
        if self.direction == "Up":
            self.direction = "Down"
        elif self.direction == "Down":
            self.direction = "Up"
        elif self.direction =="Left":
            self.direction = "Right"
        elif self.direction == "Right":
            self.direction = "Left"

    # TODO: Ghost AI

class Blinky(GhostSprite):

    def __init__(self):
        super().__init__("Blinky")

    def movement(self):
        pass

class Inky(GhostSprite):

    def __init__(self):
        super().__init__("Inky")

class Pinky(GhostSprite):

    def __init__(self):
        super().__init__("Pinky")

class Clyde(GhostSprite):

    def __init__(self):
        super().__init__("Clyde")
