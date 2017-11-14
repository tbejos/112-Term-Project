# Txanton Bejos
# tbejos
# 15-112 Term Project

# http://www.pngmart.com/image/14620

# He stated that the red enemy chases Pac-Man,
# and the pink enemy aims for a position in front of Pac-Man's mouth.
# The blue enemy is "fickle" and sometimes heads towards Pac-Man, and
# other times away. Although he claimed that the
# orange enemy's behavior is random, in actuality it alternates from behaving
# like the red enemy when at some distance from Pac-Man and aiming towards the
# lower-left corner of the maze whenever it gets too close to him.

from pygame import *

class Ghost(object):

    def __init__(self, color, screen):
        self.color = color
        self.screen = screen
        self.index = 0

    def drawGhost1(self):
        self.screen.blit(self.RIGHT[self.index], (20, 20))
        self.screen.blit(self.LEFT[self.index], (20, 82))

    def drawGhost2(self):
        self.screen.blit(self.RIGHT[self.index], (82, 20))
        self.screen.blit(self.LEFT[self.index], (82, 82))

    def drawGhost3(self):
        self.screen.blit(self.RIGHT[self.index], (144, 20))
        self.screen.blit(self.LEFT[self.index], (144, 82))

    def drawGhost4(self):
        self.screen.blit(self.RIGHT[self.index], (206, 20))
        self.screen.blit(self.LEFT[self.index], (206, 82))

    def update(self):
        if self.index == 1:
            self.index = 0
        else:
            self.index = 1

class Blinky(Ghost):
    LEFT = [image.load('images/BlinkyLeftA.png'),
            image.load('images/BlinkyLeftB.png')]
    RIGHT = [image.load('images/BlinkyRightA.png'),
             image.load('images/BlinkyRightB.png')]

    def __init__(self, screen):
        super().__init__(Color("RED"), screen)
        self.direction = 'Left'

class Pinky(Ghost):
    LEFT = [image.load('images/PinkyLeftA.png'),
            image.load('images/PinkyLeftB.png')]
    RIGHT = [image.load('images/PinkyRightA.png'),
            image.load('images/PinkyRightB.png')]

    def __init__(self, screen):
        super().__init__(Color("PINK"), screen)

class Inky(Ghost):
    LEFT = [image.load('images/InkyLeftA.png'),
            image.load('images/InkyLeftB.png')]
    RIGHT = [image.load('images/InkyRightA.png'),
             image.load('images/InkyRightB.png')]

    def __init__(self, screen):
        super().__init__(Color("CYAN"), screen)

class Clyde(Ghost):
    LEFT = [image.load('images/ClydeLeftA.png'),
            image.load('images/ClydeLeftB.png')]
    RIGHT = [image.load('images/ClydeRightA.png'),
             image.load('images/ClydeRightB.png')]

    def __init__(self, screen):
        super().__init__(Color("ORANGE"), screen)
