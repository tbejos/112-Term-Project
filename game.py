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

    pac = pacman.PacMan()

    ghostGroup = sprite.Group(blinky, pinky, inky, clyde)
    pacmanGroup = sprite.Group(pac)

    blinky.setPosition(20,20)
    inky.setPosition(82, 20)
    pinky.setPosition(144, 20)
    clyde.setPosition(206, 20)
    pac.setPosition(268, 20)

    pellet= items.Pellet()
    powerPellet = items.PowerPellet()
    cherry = items.Cherry()

    pellet.setPosition(20, 82)
    powerPellet.setPosition(82, 82)
    cherry.setPosition(144, 82)

    itemGroup = sprite.Group(pellet, powerPellet, cherry)

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

    draw = 0

    while running:

        events = event.poll()
        if events.type == QUIT or \
            events.type == KEYDOWN and events.key == K_ESCAPE: running = False

        time_elapsed +=  clock.tick(frames_per_second)
        if events.type == KEYDOWN:
            if events.key == K_UP:
                pac.direction = "Up"
            elif events.key == K_DOWN:
                pac.direction = "Down"
            elif events.key == K_LEFT:
                pac.direction = "Left"
            elif events.key == K_RIGHT:
                pac.direction = "Right"

        for ghost in ghostGroup:
            if sprite.collide_rect(pac, ghost):
                reset()


        pac.movement()
        screen.fill((0, 0, 0))  # Clears Screen
        itemGroup.draw(screen)
        ghostGroup.draw(screen)
        pacmanGroup.draw(screen)
        if time_elapsed >= 100:
            itemGroup.update()
            ghostGroup.update()
            pacmanGroup.update()
            time_elapsed = 0
        display.flip()

if __name__ == "__main__":
    main()