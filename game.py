# Txanton Bejos
# tbejos
# 15-112 Term Project

import ghosts, pacman, items
from pygame import *

def main():

    init()
    # 224x288 was original resolution so I scaled up by 3 (672x864)
    width = 224 * 3
    height = 288 * 3
    screen = display.set_mode((224 * 3, 288 * 3))
    # Create Ghosts
    blinky = ghosts.Blinky()
    pinky = ghosts.Pinky()
    inky = ghosts.Inky()
    clyde = ghosts.Clyde()
    # Create PacMan
    pac = pacman.PacMan()
    # Create items
    pellet = items.Pellet()
    powerPellet = items.PowerPellet()
    cherry = items.Cherry()
    # Create Groups
    ghostGroup = sprite.Group(blinky, pinky, inky, clyde)
    pacmanGroup = sprite.Group(pac)
    itemGroup = sprite.Group(pellet, powerPellet, cherry)
    # Set's initial positions
    blinky.setPosition(20,20)
    inky.setPosition(82, 20)
    pinky.setPosition(144, 20)
    clyde.setPosition(206, 20)
    pac.setPosition(268, 20)
    pellet.setPosition(20, 82)
    powerPellet.setPosition(82, 82)
    cherry.setPosition(144, 82)
    # Clock set-up
    clock = time.Clock()
    frames_per_second = 60
    time_elapsed = 0

    def reset():
        blinky.setPosition(20, 20)
        inky.setPosition(82, 20)
        pinky.setPosition(144, 20)
        clyde.setPosition(206, 20)
        pac.setPosition(width // 2, height // 2)

    running = True
    # Set up for start
    reset()
    while running:

        time_elapsed += clock.tick(frames_per_second)

        events = event.poll()
        if events.type == QUIT or \
            events.type == KEYDOWN and events.key == K_ESCAPE: running = False

        # Movement for PacMan
        if events.type == KEYDOWN:
            if events.key == K_UP:
                pac.direction = "Up"
            elif events.key == K_DOWN:
                pac.direction = "Down"
            elif events.key == K_LEFT:
                pac.direction = "Left"
            elif events.key == K_RIGHT:
                pac.direction = "Right"

        # Makes for more fluid movement
        pac.movement()
        # If hitting wall then reset before drawing movement
        pac.wallCheck(ghostGroup.sprites())
        # Clear screen and draw all groups
        screen.fill((0, 0, 0))
        itemGroup.draw(screen)
        ghostGroup.draw(screen)
        pacmanGroup.draw(screen)

        # Only animates every ~100 ms to make it normal speed
        if time_elapsed >= 100:
            itemGroup.update()
            ghostGroup.update()
            pacmanGroup.update()
            time_elapsed = 0

        # TODO: gameOver() and reset()
        if pac.ghostCheck(ghostGroup.sprites()):
            pac.lives -= 1
            if pac.lives < 1:
                pass
                # gameOver()
            else:
                pass
                # reset()

        display.flip()

if __name__ == "__main__":
    main()