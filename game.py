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
        self.cherry = items.Cherry()
        self.berry = items.Strawberry()
        self.orange = items.Orange()
        # Create Groups
        self.ghostGroup = sprite.Group(self.blinky, self.pinky, self.inky,
                                       self.clyde)
        self.pacmanGroup = sprite.Group(self.pac)
        self.fruitGroup = sprite.Group(self.cherry, self.berry, self.orange)
        self.wallGroup = sprite.Group()
        self.pelletGroup = sprite.Group()
        self.tpGroup = sprite.Group()
        self.turnGroup = sprite.Group()
        # Clock set-up
        self.clock = time.Clock()
        self.frames_per_second = 60
        self.time_elapsed = 0
        # Additional set-up
        self.inMenu = True
        self.running = False
        # Font
        self.myFont = font.SysFont('Consolas', 30)
        # -29 and 698 make it so PacMan is completely off screen
        self.left = walls.TeleportBlock(-29, 396)
        self.right = walls.TeleportBlock(698, 396)
        self.tpGroup.add(self.left, self.right)
        self.makeMaze()

    def makeMaze(self):
        maze = open("Maze.txt", "r")
        ycounter = 0
        for line in maze.readlines():
            for char in range(len(line)):
                if line[char] == "+":
                    self.wallGroup.add(walls.HitBox(12 * char,
                                                      72 + ycounter))
            ycounter += 12
        pellets = open("Pellets.txt", "r")
        ycounter = 0
        for line in pellets.readlines():
            for char in range(len(line)):
                if line[char] == "+":
                    self.pelletGroup.add(items.Pellet(24 * char,
                                                      72 + ycounter))
                elif line[char] == "*":
                    self.pelletGroup.add(items.PowerPellet(24 * char,
                                                           72 + ycounter))
            ycounter += 24
        turns = open("turn.txt", "r")
        for line in turns.readlines():
            list = []
            line = line[:-1]
            for param in line.split(","):
                list.append(param)
            self.turnGroup.add(walls.Turn( list[2:],int(list[0]), int(list[1])))

    def reset(self):
        self.blinky.setPosition(315, 327)
        self.blinky.direction = "Left"
        self.inky.setPosition(267, 399)
        self.inky.direction = "Up"
        self.pinky.setPosition(315, 399)
        self.pinky.direction = "Down"
        self.clyde.setPosition(363, 399)
        self.clyde.direction = "Up"
        self.pac.setPosition(312, 612)
        self.pac.direction = "Left"

    # TODO: Make actual gameOver function
    def gameOver(self):
        self.running = False

    def keyPressed(self):
        events = key.get_pressed()
        # Checks if it should Quit
        if event.poll().type == QUIT:
            self.running = False
        # Movement for PacMan
        if events[K_ESCAPE]:
            self.running = False
        if events[K_UP]:
            self.pac.turn = "Up"
        elif events[K_DOWN]:
            self.pac.turn = "Down"
        elif events[K_LEFT]:
            self.pac.turn = "Left"
        elif events[K_RIGHT]:
            self.pac.turn = "Right"

    def drawGame(self):
        # Clear screen and draw all groups
        # self.screen.fill((0, 0, 0))
        self.screen.blit(self.background, (0, 0))
        score = self.myFont.render("Score: %4d" % self.pac.score, False, (255,
                                                                    255, 255))
        lives = self.myFont.render("Lives: %d" % self.pac.lives, False, (255,
                                                                    255, 255))
        self.screen.blit(score, (460, 20))
        self.screen.blit(lives, (20, 20))
        if self.inMenu:  # TODO: Menu Design
            self.screen.blit(self.ready, (264, 477))
        # self.fruitGroup.draw(self.screen)
        self.pelletGroup.draw(self.screen)
        self.ghostGroup.draw(self.screen)
        self.pacmanGroup.draw(self.screen)
        # self.wallGroup.draw(self.screen)
        # self.turnGroup.draw(self.screen)
        display.flip()

    def animate(self):
        self.fruitGroup.update()
        self.ghostGroup.update()
        self.pacmanGroup.update()

    def checkCollision(self):
        if self.pac.ghostCheck(self.ghostGroup):
            self.pac.lives -= 1
            if self.pac.lives < 1:
                self.gameOver()
            else:
                self.reset()
            return False
        # If hitting wall then reset before drawing movement
        self.pac.itemCheck(self.pelletGroup)
        if self.pac.turn:
            self.turn(self.pac)
        return self.wallCheck(self.pac)

    def wallCheck(self, character):
        dirs = []
        teleport = sprite.spritecollide(character, self.tpGroup, False)

        for tp in teleport:
            if tp == self.left:
                character.rect.right = self.right.rect.left
            elif tp == self.right:
                character.rect.left = self.left.rect.right

        collisionList = sprite.spritecollide(character, self.wallGroup.sprites(),
                                             False)
        # If horizontal collision
        for hitObject in collisionList:
            if character.DIRECTIONS[character.direction][0] > 0:
                character.rect.right = hitObject.rect.left
                dirs.append("Right")
            elif character.DIRECTIONS[character.direction][0] < 0:
                character.rect.left = hitObject.rect.right
                dirs.append("Left")

        # Have to redefine list since sprite may have moved in last loop
        collisionList = sprite.spritecollide(character, self.wallGroup.sprites(),
                                             False)
        # If vertical collision
        for hitObject in collisionList:
            if character.DIRECTIONS[character.direction][1] > 0:
                character.rect.bottom = hitObject.rect.top
                dirs.append("Down")
            elif character.DIRECTIONS[character.direction][1] < 0:
                character.rect.top = hitObject.rect.bottom
                dirs.append("Up")

        return dirs

    def turn(self, character):
        if character.turn == oppositeDirection(character.direction) and not \
            self.wallCheck(character):
            character.direction = character.turn
            character.turn = None
        collisionList = sprite.spritecollide(character,
                                             self.turnGroup.sprites(), False)
        for turnBlock in collisionList:
            if character.rect.x == turnBlock.rect.x and \
               character.rect.y == turnBlock.rect.y:
                if character.turn in turnBlock.directions:
                    character.direction = character.turn
                    character.turn = None

    def run(self):
        time_elapsed = 0
        counter = 0
        while self.running:
            # Keeps track of the number of ticks
            time_elapsed += self.clock.tick(self.frames_per_second)
            # Checks for input
            for i in range(5):
                self.keyPressed()
                self.pac.movement()
                self.checkCollision()

            for ghost in self.ghostGroup.sprites():
                ghost.movement()
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
                counter += 1
            if counter == 3:
                self.pelletGroup.update()
                counter = 0


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

def oppositeDirection(direction):
    if direction == "Up":
        return "Down"
    elif direction == "Down":
        return "Up"
    elif direction == "Left":
        return "Right"
    elif direction == "Right":
        return "Left"

def main():
    game = Game()
    # game.cherry.setPosition(144, 82)
    # game.berry.setPosition(206, 82)
    # game.orange.setPosition(268, 82)
    game.menu()

if __name__ == "__main__":
    main()