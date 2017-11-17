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

    def __init__(self, screen, name):
        super().__init__()
        self.name = name
        self.screen = screen
        self.direction = "Left"

        self.image = image.load('images/%s/%sA.png' % (self.name, self.name))
        self.other = image.load('images/%s/%sB.png' % (self.name, self.name))

        self.eyes = {"Left":image.load('images/Eyes/EyesLeft.png'),
                     "Right":image.load('images/Eyes/EyesRight.png'),
                     "Up":image.load('images/Eyes/EyesUp.png'),
                     "Down":image.load('images/Eyes/EyesDown.png')}

        self.rect = self.image.get_rect()

    def update(self):
        self.screen.blit(self.eyes[self.direction], self.rect)
        temp = self.image
        self.image = self.other
        self.other = temp
        x, y = self.rect.x, self.rect.y
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y

class Blinky(GhostSprite):

    def __init__(self, screen):
        super().__init__(screen, "Blinky")

class Pinky(GhostSprite):

    def __init__(self, screen):
        super().__init__(screen, "Pinky")

class Inky(GhostSprite):

    def __init__(self, screen):
        super().__init__(screen, "Inky")

class Clyde(GhostSprite):

    def __init__(self, screen):
        super().__init__(screen, "Clyde")

