from pygame import *

class Ghost(object):

    def __init__(self, color, screen, name=None):
        self.color = color
        self.screen = screen
        self.index = 0
        if name:
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
        self.screen.blit(self.GHOST[self.index], (x, 20))
        self.screen.blit(self.RIGHT, (x, 20))
        self.screen.blit(self.GHOST[self.index], (x, 82))
        self.screen.blit(self.LEFT, (x, 82))
        self.screen.blit(self.GHOST[self.index], (x, 144))
        self.screen.blit(self.UP, (x, 144))
        self.screen.blit(self.GHOST[self.index], (x, 206))
        self.screen.blit(self.DOWN, (x, 206))
        self.screen.blit(self.PELLET[self.index], (x, 268))

    def drawGhost2(self):
        x = 82
        self.screen.blit(self.GHOST[self.index], (x, 20))
        self.screen.blit(self.RIGHT, (x, 20))
        self.screen.blit(self.GHOST[self.index], (x, 82))
        self.screen.blit(self.LEFT, (x, 82))
        self.screen.blit(self.GHOST[self.index], (x, 144))
        self.screen.blit(self.UP, (x, 144))
        self.screen.blit(self.GHOST[self.index], (x, 206))
        self.screen.blit(self.DOWN, (x, 206))
        self.screen.blit(self.PELLET[self.index], (x, 268))

    def drawGhost3(self):
        x = 144
        self.screen.blit(self.GHOST[self.index], (x, 20))
        self.screen.blit(self.RIGHT, (x, 20))
        self.screen.blit(self.GHOST[self.index], (x, 82))
        self.screen.blit(self.LEFT, (x, 82))
        self.screen.blit(self.GHOST[self.index], (x, 144))
        self.screen.blit(self.UP, (x, 144))
        self.screen.blit(self.GHOST[self.index], (x, 206))
        self.screen.blit(self.DOWN, (x, 206))
        self.screen.blit(self.PELLET[self.index], (x, 268))

    def drawGhost4(self):
        x = 206
        self.screen.blit(self.GHOST[self.index], (x, 20))
        self.screen.blit(self.RIGHT, (x, 20))
        self.screen.blit(self.GHOST[self.index], (x, 82))
        self.screen.blit(self.LEFT, (x, 82))
        self.screen.blit(self.GHOST[self.index], (x, 144))
        self.screen.blit(self.UP, (x, 144))
        self.screen.blit(self.GHOST[self.index], (x, 206))
        self.screen.blit(self.DOWN, (x, 206))
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