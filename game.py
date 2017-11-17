# Txanton Bejos
# tbejos
# 15-112 Term Project

import ghosts, pacman, items
from pygame import *
import time

def main():

    init()
    # 224x288 was original resolution so I scaled up by 3 (672x864)
    screen = display.set_mode((224 * 3, 288 * 3))
    # Create Ghosts
    blinky = ghosts.Blinky(screen)
    pinky = ghosts.Pinky(screen)
    inky = ghosts.Inky(screen)
    clyde = ghosts.Clyde(screen)

    pac = pacman.PacMan()

    ghostGroup = sprite.Group(blinky, pinky, inky, clyde)
    pacmanGroup = sprite.Group(pac)

    blinky.set_position(20,20)
    inky.set_position(82, 20)
    pinky.set_position(144, 20)
    clyde.set_position(206, 20)
    pac.set_position(268, 20)

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
            drawItems()
            ghostGroup.draw(screen)
            pacmanGroup.draw(screen)
            ghostGroup.update()
            pacmanGroup.update()
            time.sleep(0.2) # Animation Timing
            display.flip()

    def drawItems():
        p.drawItem(20, 330)
        pp.drawItem(82, 330)
        fruit.drawItem(268, 268)

    testDraw()

if __name__ == "__main__":
    main()