# Txanton Bejos
# tbejos
# 15-112 Term Project
# https://en.wikipedia.org/wiki/Namco_Pac-Man
# http://www.arcade-museum.com/game_detail.php?game_id=10816
# http://www.nerdparadise.com/programming/pygame/part1
import ghosts, ghosts2
import pacman
import pellets

from pygame import *
import time
init()
screen = display.set_mode((672, 864))

blinky = ghosts2.Blinky(screen)
pinky = ghosts2.Pinky(screen)
inky = ghosts2.Inky(screen)
clyde = ghosts2.Clyde(screen)
pac = pacman.PacMan(screen)

def testDraw():
    done = False

    while not done:
        for events in event.get():
            if events.type == QUIT:
                done = True
        screen.fill((0,0,0)) # Clears Screen
        drawAll()
        updateAll()
        time.sleep(0.2) # Animation Timing
        display.flip()

def drawAll():
    blinky.drawGhost1()
    inky.drawGhost2()
    pinky.drawGhost3()
    clyde.drawGhost4()
    pac.drawPacMan()

def updateAll():
    blinky.update()
    inky.update()
    pinky.update()
    clyde.update()
    pac.update()

if __name__ == "__main__":
    testDraw()