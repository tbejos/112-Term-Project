# Txanton Bejos
# tbejos
# 15-112 Term Project

import ghosts, pacman, items, walls
from pygame import *

class Game(object):

    def __init__(self):
        init()
        font.init()
        # 224x288 was original resolution so I scaled up by 3 (672x864)
        self.width = 224 * 3
        self.height = 288 * 3
        self.screen = display.set_mode((self.width, self.height))
        self.background = image.load('images/BackGround.png')
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
        self.berry = items.Strawberry()
        self.orange = items.Orange()
        # Create Groups
        self.ghostGroup = sprite.Group(self.blinky, self.pinky, self.inky,
                                       self.clyde)
        self.pacmanGroup = sprite.Group(self.pac)
        self.itemGroup = sprite.Group(self.pellet, self.powerPellet,
                                      self.cherry, self.berry, self.orange)
        self.wallGroup = sprite.Group()
        # Clock set-up
        self.clock = time.Clock()
        self.frames_per_second = 60
        self.time_elapsed = 0
        # Additional set-up
        self.inMenu = True
        self.running = False
        # Font
        self.myFont = font.SysFont('Consolas', 30)
        self.makeMaze()

    def makeMaze(self):
        maze = open("Maze.txt", "r")
        ycounter = 0
        for line in maze.readlines():
            for char in range(len(line)):
                if line[char] == "+":
                    self.wallGroup.add(walls.SmallWallTile(12 * char,
                                                           72 + ycounter))
            ycounter += 12

        for sprite in self.wallGroup.sprites():
            print("%d, %d" % (sprite.rect.x, sprite.rect.y))

    def reset(self):
        self.blinky.setPosition(315, 327)
        self.inky.setPosition(267, 399)
        self.pinky.setPosition(315, 399)
        self.clyde.setPosition(363, 399)
        self.pac.setPosition(315, 615)

    # TODO: Make actual gameOver function
    def gameOver(self):
        self.running = False

    def keyPressed(self):
        events = event.poll()
        # Checks if it should Quit
        if events.type == QUIT:
            self.running = False
        # Movement for PacMan
        if events.type == KEYDOWN:
            if events.key == K_ESCAPE:
                self.running = False
            if events.key == K_UP:
                self.pac.direction = "Up"
            elif events.key == K_DOWN:
                self.pac.direction = "Down"
            elif events.key == K_LEFT:
                self.pac.direction = "Left"
            elif events.key == K_RIGHT:
                self.pac.direction = "Right"

    def drawGame(self):
        # Clear screen and draw all groups
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.background, (0, 0))
        if self.inMenu:  # TODO: Menu Design
            self.screen.blit(self.ready, (264, 477))
        self.itemGroup.draw(self.screen)
        self.ghostGroup.draw(self.screen)
        self.pacmanGroup.draw(self.screen)
        self.wallGroup.draw(self.screen)
        self.wallGroup.draw(self.screen)
        display.flip()

    def animate(self):
        self.itemGroup.update()
        self.ghostGroup.update()
        self.pacmanGroup.update()

    def checkCollision(self):
        if self.pac.ghostCheck(self.ghostGroup):
            self.pac.lives -= 1
            if self.pac.lives < 1:
                self.gameOver()
            else:
                self.reset()
        # If hitting wall then reset before drawing movement
        self.wallCheck(self.pac)
        self.pac.itemCheck(self.itemGroup)

    # TODO: Doesn't work if inside the box
    def wallCheck(self, character):
        collisionList = sprite.spritecollide(character, self.wallGroup.sprites(),
                                             False)
        # If horizontal collision
        for hitObject in collisionList:
            if character.DIRECTIONS[character.direction][0] > 0:
                character.rect.right = hitObject.rect.left
                return True
            elif character.DIRECTIONS[character.direction][0] < 0:
                character.rect.left = hitObject.rect.right
                return True

        # Have to redefine list since sprite may have moved in last loop
        collisionList = sprite.spritecollide(character, self.wallGroup.sprites(),
                                             False)
        # If vertical collision
        for hitObject in collisionList:
            if character.DIRECTIONS[character.direction][1] > 0:
                character.rect.bottom = hitObject.rect.top
                return True
            elif character.DIRECTIONS[character.direction][1] < 0:
                character.rect.top = hitObject.rect.bottom
                return True

    def run(self):
        time_elapsed = 0
        while self.running:
            # Keeps track of the number of ticks
            time_elapsed += self.clock.tick(self.frames_per_second)
            # Checks for input
            self.keyPressed()
            # Move and check for collisions/reset position
            for ghost in self.ghostGroup.sprites():
                ghost.movement()
            self.pac.movement()
            self.checkCollision()
            for ghost in self.ghostGroup.sprites():
                if self.wallCheck(ghost):
                    ghost.switchDirection()
            # Draw
            self.drawGame()
            # Only animates every ~100 ms to make it normal speed
            if time_elapsed >= 100:
                self.animate()
                time_elapsed = 0

    def menu(self):
        self.ready = image.load('images/Walls/Ready.png')
        self.reset()
        while self.inMenu:
            self.drawGame()
            for menuEvent in event.get():
                if menuEvent.type == QUIT:
                    self.inMenu = False
                if menuEvent.type == KEYDOWN:
                    if menuEvent.key == K_ESCAPE:
                        self.inMenu = False
                    if menuEvent.key == K_RETURN:
                        self.inMenu = False
                        self.running = True
                        self.run()

def main():
    game = Game()
    game.pellet.setPosition(20, 82)
    game.powerPellet.setPosition(82, 82)
    game.cherry.setPosition(144, 82)
    game.berry.setPosition(206, 82)
    game.orange.setPosition(268, 82)
    game.menu()

if __name__ == "__main__":
    main()