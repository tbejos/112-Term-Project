# Txanton Bejos
# tbejos
# 15-112 Term Project

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
p = pellets.Pellet(screen)
pp = pellets.PowerPellet(screen)

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
    p.draw(20, 330)
    pp.draw(82, 330)

def updateAll():
    blinky.update()
    inky.update()
    pinky.update()
    clyde.update()
    pac.update()

if __name__ == "__main__":
    testDraw()