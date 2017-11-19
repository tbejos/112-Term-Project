# Txanton Bejos
# tbejos
# 15-112 Term Project

import ghosts, pacman, items
from pygame import *

class Game(object):

    def __init__(self):
        # 224x288 was original resolution so I scaled up by 3 (672x864)
        self.width = 224 * 3
        self.height = 288 * 3
        self.screen = display.set_mode((self.width, self.height))
        # Create Ghosts
        self.blinky = ghosts.Blinky()
        self.pinky = ghosts.Pinky()
        self.inky = ghosts.Inky()
        self.clyde = ghosts.Clyde()
        # Create PacMan
        self.pac = pacman.PacMan()
        # Create items
        self.pellet = items.Pellet()
        self.powerPellet = items.PowerPellet()
        self.cherry = items.Cherry()
        # Create Groups
        self.ghostGroup = sprite.Group(self.blinky, self.pinky, self.inky,
                                       self.clyde)
        self.pacmanGroup = sprite.Group(self.pac)
        self.itemGroup = sprite.Group(self.pellet, self.powerPellet,
                                      self.cherry)
        # Clock set-up
        self.clock = time.Clock()
        self.frames_per_second = 60
        self.time_elapsed = 0
        # Additional set-up
        self.running = True
        self.events = None

    # TODO: Make actual reset function (and location)
    def reset(self):
        self.blinky.setPosition(20, 20)
        self.inky.setPosition(82, 20)
        self.pinky.setPosition(144, 20)
        self.clyde.setPosition(206, 20)
        self.pac.setPosition(self.width // 2, self.height * (2 / 3))

    # TODO: Make actual gameOver function
    def gameOver(self):
        self.running = False

    def keyPressed(self):
        self.events = event.poll()
        # Checks if it should Quit
        if self.events.type == QUIT:
            self.running = False
        # Movement for PacMan
        if self.events.type == KEYDOWN:
            if self.events.key == K_ESCAPE:
                self.running = False
            if self.events.key == K_UP:
                self.pac.direction = "Up"
            elif self.events.key == K_DOWN:
                self.pac.direction = "Down"
            elif self.events.key == K_LEFT:
                self.pac.direction = "Left"
            elif self.events.key == K_RIGHT:
                self.pac.direction = "Right"

    def drawAll(self):
        # Clear screen and draw all groups
        self.screen.fill((0, 0, 0))
        self.itemGroup.draw(self.screen)
        self.ghostGroup.draw(self.screen)
        self.pacmanGroup.draw(self.screen)
        display.flip()

    def animate(self):
        self.itemGroup.update()
        self.ghostGroup.update()
        self.pacmanGroup.update()

    # TODO: Move collision checks from PacMan to here as functions
    def checkCollision(self):
        if self.pac.ghostCheck(self.ghostGroup):
            self.pac.lives -= 1
            if self.pac.lives < 1:
                self.gameOver()
            else:
                self.reset()
        # If hitting wall then reset before drawing movement
        # self.pac.wallCheck(self.ghostGroup)
        self.pac.itemCheck(self.itemGroup)

    def run(self):
        time_elapsed = 0
        while self.running:
            # Keeps track of the number of ticks
            time_elapsed += self.clock.tick(self.frames_per_second)
            # Checks for input
            self.keyPressed()
            # Makes for more fluid movement
            self.pac.movement()
            # Draw
            self.drawAll()
            # Only animates every ~100 ms to make it normal speed
            if time_elapsed >= 100:
                self.animate()
                time_elapsed = 0
            self.checkCollision()

def main():
    init()
    game = Game()
    game.pellet.setPosition(20, 82)
    game.powerPellet.setPosition(82, 82)
    game.cherry.setPosition(144, 82)
    game.reset()
    game.run()


if __name__ == "__main__":
    main()