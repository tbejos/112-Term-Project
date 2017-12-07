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
from implementation import *
import random

mazeGraph = GraphWithWeights()
mazeGraph.edges = {
    1 : [2, 7],
    2 : [1, 3, 8],
    3 : [2, 10],
    4 : [5, 11],
    5 : [4, 6, 13],
    6 : [5, 14],
    7 : [8, 1, 15],
    8 : [7, 9, 2, 16],
    9 : [8, 10, 17],
    10: [9, 11, 3],
    11: [10, 12, 4],
    12: [11, 13, 20],
    13: [12, 14, 5, 21],
    14: [13, 6, 22],
    15: [16, 7],
    16: [15, 8, 27],
    17: [18, 9],
    18: [17, 24],
    19: [20, 25],
    20: [19, 12],
    21: [22, 13, 30],
    22: [21, 14],
    23: [24, 28],
    24: [23, 25, 18],
    25: [24, 26, 19],
    26: [25, 29],
    27: [30, 28, 16, 34],
    28: [27, 23, 31],
    29: [30, 26, 32],
    30: [29, 27, 21, 39],
    31: [32, 28, 35],
    32: [31, 29, 38],
    33: [34, 41],
    34: [33, 35, 27, 43],
    35: [34, 36, 31],
    36: [35, 45],
    37: [38, 46],
    38: [37, 39, 32],
    39: [38, 40, 30, 48],
    40: [39, 50],
    41: [42, 33],
    42: [41, 52],
    43: [44, 34, 53],
    44: [43, 45, 54],
    45: [44, 46, 36],
    46: [45, 47, 37],
    47: [46, 48, 57],
    48: [47, 39, 58],
    49: [50, 59],
    50: [49, 40],
    51: [52, 61],
    52: [51, 53, 42],
    53: [54, 55],
    54: [55, 44],
    55: [54, 62],
    56: [57, 63],
    57: [56, 47],
    58: [59, 48],
    59: [58, 60, 49],
    60: [59, 64],
    61: [62, 51],
    62: [61, 63, 55],
    63: [62, 64, 56],
    64: [63, 60]}

class GhostSprite(sprite.Sprite):
    # Amount ghosts move per tick
    MOVES = {"Left": (-1, 0),
              "Right": (1, 0),
              "Up": (0, -1),
              "Down": (0, 1)}
    DIRECTIONS = ["Left", "Right", "Up", "Down"]

    def __init__(self, name, home):
        super().__init__()
        self.name = name
        self.home = home
        self.direction = "Left"
        self.index = 24
        self.count = 0
        self.turn = "Left"
        self.next = None
        self.start = False
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
        self.pelleted = \
            {"Normal":
                [image.load('images/Ghost Sprites/PelletGhostA.png'),
                 image.load('images/Ghost Sprites/PelletGhostB.png')],
             "Flashing":
                [image.load('images/Ghost Sprites/PelletGhostA.png'),
                 image.load('images/Ghost Sprites/PelletGhostFlash.png')]}
        self.eyes = \
            {"Left":
                image.load('images/Eyes/EyesLeft.png'),
            "Right":
                image.load('images/Eyes/EyesRight.png'),
            "Up":
                image.load('images/Eyes/EyesLeft.png'),
            "Down":
                image.load('images/Eyes/EyesLeft.png')}


        self.rect = self.image.get_rect()

    def update(self):
        if self.count == 0:
            self.count = 1
        else:
            self.count = 0
        if self.start:
            self.image = self.eyes[self.direction]
        else:
            self.image = self.other[self.direction][self.count]
        x, y = self.rect.x, self.rect.y
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def setPosition(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def movement(self):
        self.rect.x += self.MOVES[self.direction][0]
        self.rect.y += self.MOVES[self.direction][1]

    def switchDirection(self):
        if self.direction == "Up":
            self.direction = "Down"
        elif self.direction == "Down":
            self.direction = "Up"
        elif self.direction =="Left":
            self.direction = "Right"
        elif self.direction == "Right":
            self.direction = "Left"

    def randomTurn(self):
        self.turn = self.DIRECTIONS[random.randint(0, 3)]

    def returnToStart(self):
        a = a_star_search(mazeGraph, self.index, self.home)
        try:
            self.next = mazeGraph.edges[self.index].index(self.parse(a, 25))
        except:
            self.start = False

    def parse(self, map, goal):
        route, garbage = map
        ans = 0
        i = goal
        while route[i] != None:
            ans = i
            i = route[i]
        return ans

class Blinky(GhostSprite):

    def __init__(self):
        super().__init__("Blinky", 24)

    def updateTurn(self, pac):
        a = a_star_search(mazeGraph, self.index, pac)
        # Makes sure we don't go out of bounds when he is eaten
        try:
            self.next = mazeGraph.edges[self.index].index(self.parse(a, pac))
        except:
            self.next = 0

class Inky(GhostSprite):

    def __init__(self):
        super().__init__("Inky", 8)

    def updateTurn(self, goal):
        if self.index in [8, 9, 10, 11, 12]:
            self.turn = "Right"
        if self.index in [13, 21, 30, 39]:
            self.turn = "Down"
        if self.index in [48, 47, 46, 45, 44]:
            self.turn = "Left"
        if self.index in [43, 34, 27, 16]:
            self.turn = "Up"


class Pinky(GhostSprite):

    def __init__(self):
        super().__init__("Pinky", 25)
        self.home = 25

    def updateTurn(self, goal):
        if self.index in [23, 24, 25]:
            self.turn = "Right"
        if self.index in [26, 29]:
            self.turn = "Down"
        if self.index == 32:
            self.turn = "Left"
        if self.index in [31, 28]:
            self.turn = "Up"

class Clyde(GhostSprite):

    def __init__(self):
        super().__init__("Clyde", 25)

    def updateTurn(self, goal):
        self.turn = self.DIRECTIONS[random.randint(0, 3)]