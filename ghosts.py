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

class Ghost(object):

    def __init__(self, color, screen, name=None):
        self.color = color
        self.screen = screen
        self.index = 0
        if name:
            self.name = name
            self.LEFT  = [image.load('images/%sLeftA.png' % self.name),
                          image.load('images/%sLeftB.png' % self.name)]
            self.RIGHT = [image.load('images/%sRightA.png' % self.name),
                          image.load('images/%sRightB.png' % self.name)]
            self.UP    = [image.load('images/%sUpA.png' % self.name),
                          image.load('images/%sUpB.png' % self.name)]
            self.DOWN = [image.load('images/%sDownA.png' % self.name),
                         image.load('images/%sDownB.png' % self.name)]
        self.EYES = [image.load('images/EyesRight.png'),
                     image.load('images/EyesLeft.png'),
                     image.load('images/EyesUp.png'),
                     image.load('images/EyesDown.png')]
        self.PELLET = [image.load('images/PelletGhostA.png'),
                       image.load('images/PelletGhostB.png')]

    def drawGhost1(self):
        x = 20
        x2 = 268
        self.screen.blit(self.RIGHT[self.index], (x, 20))
        self.screen.blit(self.EYES[0], (x2, 20))
        self.screen.blit(self.LEFT[self.index], (x, 82))
        self.screen.blit(self.EYES[1], (x2, 82))
        self.screen.blit(self.UP[self.index], (x, 144))
        self.screen.blit(self.EYES[2], (x2, 144))
        self.screen.blit(self.DOWN[self.index], (x, 206))
        self.screen.blit(self.EYES[3], (x2, 206))
        self.screen.blit(self.PELLET[self.index], (x, 268))

    def drawGhost2(self):
        x = 82
        self.screen.blit(self.RIGHT[self.index], (x, 20))
        self.screen.blit(self.LEFT[self.index], (x, 82))
        self.screen.blit(self.UP[self.index], (x, 144))
        self.screen.blit(self.DOWN[self.index], (x, 206))
        self.screen.blit(self.PELLET[self.index], (x, 268))

    def drawGhost3(self):
        x = 144
        self.screen.blit(self.RIGHT[self.index], (x, 20))
        self.screen.blit(self.LEFT[self.index], (x, 82))
        self.screen.blit(self.UP[self.index], (x, 144))
        self.screen.blit(self.DOWN[self.index], (x, 206))
        self.screen.blit(self.PELLET[self.index], (x, 268))

    def drawGhost4(self):
        x = 206
        self.screen.blit(self.RIGHT[self.index], (x, 20))
        self.screen.blit(self.LEFT[self.index], (x, 82))
        self.screen.blit(self.UP[self.index], (x, 144))
        self.screen.blit(self.DOWN[self.index], (x, 206))
        self.screen.blit(self.PELLET[self.index], (x, 268))

    def update(self):
        if self.index == 1:
            self.index = 0
        else:
            self.index = 1

class Blinky(Ghost):

    def __init__(self, screen):
        super().__init__(Color("RED"), screen, "Blinky")

class Pinky(Ghost):

    def __init__(self, screen):
        super().__init__(Color("PINK"), screen, "Pinky")

class Inky(Ghost):

    def __init__(self, screen):
        super().__init__(Color("CYAN"), screen, "Inky")

class Clyde(Ghost):

    def __init__(self, screen):
        super().__init__(Color("ORANGE"), screen, "Clyde")
