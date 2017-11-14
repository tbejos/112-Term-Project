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

    def __init__(self, screen, name="Template"):
        self.screen = screen
        self.eaten = False
        self.index = 0

        self.name = name
        self.GHOST = [image.load('images/%sA.png' % self.name),
                      image.load('images/%sB.png' % self.name)]
        self.LEFT = image.load('images/EyesLeft.png')
        self.RIGHT = image.load('images/EyesRight.png')
        self.UP = image.load('images/EyesUp.png')
        self.DOWN = image.load('images/EyesDown.png')
        self.PELLET = [image.load('images/PelletGhostA.png'),
                       image.load('images/PelletGhostB.png')]

    def drawGhost1(self):
        x = 20
        self.drawRight(x, 20)
        self.drawLeft(x, 82)
        self.drawUp(x, 144)
        self.drawDown(x, 206)
        self.drawVulnerable(x, 268)

    def drawGhost2(self):
        x = 82
        self.drawRight(x, 20)
        self.drawLeft(x, 82)
        self.drawUp(x, 144)
        self.drawDown(x, 206)
        self.drawVulnerable(x, 268)

    def drawGhost3(self):
        x = 144
        self.drawRight(x, 20)
        self.drawLeft(x, 82)
        self.drawUp(x, 144)
        self.drawDown(x, 206)
        self.drawVulnerable(x, 268)

    def drawGhost4(self):
        x = 206
        self.drawRight(x, 20)
        self.drawLeft(x, 82)
        self.drawUp(x, 144)
        self.drawDown(x, 206)
        self.drawVulnerable(x, 268)

    def drawGhost(self, x, y):
        if not self.eaten:
            self.screen.blit(self.GHOST[self.index], (x, y))

    def drawLeft(self, x, y):
        self.drawGhost(x, y)
        self.screen.blit(self.LEFT, (x, y))

    def drawRight(self, x, y):
        self.drawGhost(x, y)
        self.screen.blit(self.RIGHT, (x, y))

    def drawUp(self, x, y):
        self.drawGhost(x, y)
        self.screen.blit(self.UP, (x, y))

    def drawDown(self, x, y):
        self.drawGhost(x, y)
        self.screen.blit(self.DOWN, (x, y))

    def drawVulnerable(self, x, y):
        self.screen.blit(self.PELLET[self.index], (x, y))

    def update(self):
        if self.index == 1:
            self.index = 0
        else:
            self.index = 1

class Blinky(Ghost):

    def __init__(self, screen):
        super().__init__(screen, "Blinky")

class Pinky(Ghost):

    def __init__(self, screen):
        super().__init__(screen, "Pinky")

class Inky(Ghost):

    def __init__(self, screen):
        super().__init__(screen, "Inky")

class Clyde(Ghost):

    def __init__(self, screen):
        super().__init__(screen, "Clyde")