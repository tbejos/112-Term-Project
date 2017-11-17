# Txanton Bejos
# tbejos
# 15-112 Term Project

# They cycle through different "modes" of behavior, colloquially known as
# "scatter"–where they retreat to the four corners of the maze
# "chase"–where their A.I. kicks in. Each ghost has unique A.I.
# There are certain one-way areas on the maze–namely, the two "T" formations
# located directly above and below the Ghost Home (the box in the center of the
# stage)–that the ghosts can travel down through, but can't go up through.
# There are also two entrances to a tunnel on either side of the maze that Pac-Man
# can travel through and come out the opposite side of the screen on, which will
# slow the ghosts down if they enter it. Yet another advantage Pac-Man has over
# the quartet is that he can turn slightly faster.
#
#     the red ghost, Blinky, doggedly pursues Pac-Man;
#     the pink ghost, Pinky, tries to ambush Pac-Man by moving parallel to him;
#     the cyan ghost, Inky, tends not to chase Pac-Man directly unless Blinky is near;
#     the orange ghost, Clyde, pursues Pac-Man when far from him, but usually
#       wanders away when he gets close.



from pygame import *

class Ghost(object):

    def __init__(self, screen, name="Template"):
        self.screen = screen
        self.eaten = False
        self.index = 0

        self.name = name
        # Loads all the images needed
        self.GHOST = [image.load('images/%s/%sA.png' % (self.name, self.name)),
                      image.load('images/%s/%sB.png' % (self.name, self.name))]
        self.LEFT = image.load('images/Eyes/EyesLeft.png')
        self.RIGHT = image.load('images/Eyes/EyesRight.png')
        self.UP = image.load('images/Eyes/EyesUp.png')
        self.DOWN = image.load('images/Eyes/EyesDown.png')
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
        if not self.eaten:  # If it is eaten it will only draw the eyes
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