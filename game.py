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

    blinky.setPosition(20,20)
    inky.setPosition(82, 20)
    pinky.setPosition(144, 20)
    clyde.setPosition(206, 20)
    pac.setPosition(268, 20)

    p = items.Pellet()
    pp = items.PowerPellet()
    fruit = items.Cherry()

    p.setPosition(20, 82)
    pp.setPosition(82, 82)
    fruit.setPosition(144, 82)

    itemGroup = sprite.Group(p, pp, fruit)

    def testDraw():
        done = False

        while not done:
            for events in event.get():
                if events.type == QUIT:
                    done = True
            screen.fill((0,0,0)) # Clears Screen
            itemGroup.draw(screen)
            ghostGroup.draw(screen)
            pacmanGroup.draw(screen)
            itemGroup.update()
            ghostGroup.update()
            pacmanGroup.update()
            time.sleep(0.2) # Animation Timing
            display.flip()

    testDraw()

if __name__ == "__main__":
    main()