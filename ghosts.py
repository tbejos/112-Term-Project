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

    def drawGhost(self):
        self.screen.blit(self.image, (20, 20))

class Blinky(Ghost):
    image = image.load('images/Blinky.png')

    def __init__(self, screen):
        super().__init__(Color("RED"), screen)

class Pinky(Ghost):
    image = image.load('images/Pinky.png')

    def __init__(self, screen):
        super().__init__(Color("PINK"), screen)

class Inky(Ghost):
    image = image.load('images/Inky.png')

    def __init__(self, screen):
        super().__init__(Color("CYAN"), screen)

class Clyde(Ghost):
    image = image.load('images/Clyde.png')

    def __init__(self, screen):
        super().__init__(Color("ORANGE"), screen)
