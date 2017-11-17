# Txanton Bejos
# tbejos
# 15-112 Term Project

import ghosts2
import pacman
import items

from pygame import *
import time
init()
# 224x288 was original resolution so I scaled up by 3 (672x864)
screen = display.set_mode((224 * 3, 288 * 3))

blinky = ghosts2.Blinky(screen)
pinky = ghosts2.Pinky(screen)
inky = ghosts2.Inky(screen)
clyde = ghosts2.Clyde(screen)
pac = pacman.PacMan(screen)
p = items.Pellet(screen)
pp = items.PowerPellet(screen)
fruit = items.Cherry(screen)

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
    p.drawItem(20, 330)
    pp.drawItem(82, 330)
    fruit.drawItem(268, 268)

def updateAll():
    blinky.update()
    inky.update()
    pinky.update()
    clyde.update()
    pac.update()

if __name__ == "__main__":
    testDraw()