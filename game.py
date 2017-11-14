# Txanton Bejos
# tbejos
# 15-112 Term Project
# https://en.wikipedia.org/wiki/Namco_Pac-Man
# http://www.arcade-museum.com/game_detail.php?game_id=10816
# http://www.nerdparadise.com/programming/pygame/part1
import ghosts
import pacman
import pellets

from pygame import *
init()
screen = display.set_mode((672, 864))

blinky = ghosts.Blinky(screen)
pinky = ghosts.Pinky(screen)
inky = ghosts.Inky(screen)
clyde = ghosts.Clyde(screen)

def runGame():
    done = False

    while not done:
        for events in event.get():
            if events.type == QUIT:
                done = True

        blinky.drawGhost()
        display.flip()

if __name__ == "__main__":
    runGame()