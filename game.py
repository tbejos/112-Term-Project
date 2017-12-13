# Txanton Bejos
# tbejos
# 15-112 Term Project

import ghosts, pacman, items, walls
from pygame import *

class Game(object):
    turns = ["Left", "Right", "Up", "Down"]

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
        self.chomp = mixer.Sound('sounds/pacman_chomp.wav')
        self.die = mixer.Sound('sounds/pacman_death.wav')
        # -29 and 698 make it so PacMan is completely off screen
        self.left = walls.TeleportBlock(-29, 396)
        self.right = walls.TeleportBlock(698, 396)
        self.tpGroup.add(self.left, self.right)
        self.makeMaze()

    def makeMaze(self):
        maze = open("text/Maze.txt", "r")
        ycount = 0
        for line in maze.readlines():
            for char in range(len(line)):
                if line[char] == "+":
                    self.wallGroup.add(walls.HitBox(12 * char,
                                                      72 + ycount))
            ycount += 12
        pellets = open("text/Pellets.txt", "r")
        ycount = 0
        for line in pellets.readlines():
            for char in range(len(line)):
                if line[char] == "+":
                    self.pelletGroup.add(items.Pellet(24 * char,
                                                      72 + ycount))
                elif line[char] == "*":
                    self.pelletGroup.add(items.PowerPellet(24 * char,
                                                           72 + ycount))
            ycount += 24
        turns = open("text/Turn.txt", "r")
        index = 1
        for line in turns.readlines():
            list = []
            line = line[:-1]
            for param in line.split(","):
                list.append(param)
            self.turnGroup.add(walls.Turn( index, list[2:],int(list[0]),
                                           int(list[1])))
            index += 1

    def reset(self):
        self.pac.powerpellet = False
        for ghost in self.ghostGroup.sprites():
            ghost.start = False
        self.blinky.setPosition(312, 324)
        self.clyde.setPosition(348, 324)
        self.inky.setPosition(132,180)
        self.pinky.setPosition(204, 324)
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
        self.wallGroup.draw(self.screen)
        # self.turnGroup.draw(self.screen)
        display.flip()

    def animate(self):
        self.fruitGroup.update()
        self.ghostGroup.update()
        self.pacmanGroup.update()

    def checkCollision(self):
        if self.pac.ghostCheck(self.ghostGroup):
            self.die.play()
            self.pac.lives -= 1
            time.wait(1000)
            if self.pac.lives < 1:
                self.gameOver()
            else:
                self.reset()
            return False
        # If hitting wall then reset before drawing movement
        self.itemCheck()
        if self.pac.turn:
            self.turn(self.pac)
        self.teleportCheck(self.pac)
        return self.horizontalWalls(self.pac) + self.verticalWalls(self.pac)

    def itemCheck(self):
        collisionList = sprite.spritecollide(self.pac,
                                             self.pelletGroup.sprites(),
                                             False)
        for item in collisionList:
            self.pac.score += item.points
            if item.name == "PowerPellet":
                # Resets timer
                if self.pac.powerpellet:
                    self.count = 0
                self.pac.powerpellet = True
            item.kill()

    def teleportCheck(self, character):
        teleport = sprite.spritecollide(character, self.tpGroup, False)

        for tp in teleport:
            if tp == self.left:
                character.rect.right = self.right.rect.left
            elif tp == self.right:
                character.rect.left = self.left.rect.right
    """
    Most of my wall code is heavily based off of this video
    https://www.youtube.com/watch?v=57bkG0HytI8&list=PL1H1sBF1VAKXh0GR1O94UUguIxkCP3dHM&index=12
    however I have made some modifications in order to better reflect my use 
    case.
    """
    def horizontalWalls(self, character):
        dirs = []

        collisionList = sprite.spritecollide(character, self.wallGroup.sprites(),
                                             False)
        # If horizontal collision
        for hitObject in collisionList:
            if character.MOVES[character.direction][0] > 0:
                character.rect.right = hitObject.rect.left
                dirs.append("Right")
            elif character.MOVES[character.direction][0] < 0:
                character.rect.left = hitObject.rect.right
                dirs.append("Left")

        return dirs

    def verticalWalls(self, character):
        dirs = []

        collisionList = sprite.spritecollide(character, self.wallGroup.sprites(),
                                             False)
        # If vertical collision
        for hitObject in collisionList:
            if character.MOVES[character.direction][1] > 0:
                character.rect.bottom = hitObject.rect.top
                dirs.append("Down")
            elif character.MOVES[character.direction][1] < 0:
                character.rect.top = hitObject.rect.bottom
                dirs.append("Up")

        return dirs

    def turn(self, character):
        # Only PacMan can switch direction on a straight away
        if character.name == "PacMan" and \
           character.turn == oppositeDirection(character.direction) and not \
            (self.horizontalWalls(character) + self.verticalWalls(character)):
            character.direction = character.turn
            character.turn = None
        collisionList = sprite.spritecollide(character,
                                             self.turnGroup.sprites(), False)

        for turnBlock in collisionList:
            try:
                if character.next >= 0:
                    character.turn = turnBlock.directions[character.next]
            except:
                pass
            character.index = turnBlock.index
            if character.rect.x == turnBlock.rect.x and \
               character.rect.y == turnBlock.rect.y:
                if character.turn in turnBlock.directions:
                    character.direction = character.turn
                    if character in self.ghostGroup.sprites():
                        character.turn = character.direction
                    else:
                        character.turn = None

    def run(self):
        time_elapsed = 0
        self.count = 0
        mixer.music.load('sounds/pacman_chomp.wav')
        mixer.music.play(-1)
        while self.running:
            if len(self.pelletGroup.sprites()) == 0:
                self.pac.lives += 1
                self.makeMaze()
                self.reset()
            if self.pac.powerpellet:
                if self.count >= 30:
                    self.pac.powerpellet = False
                    self.count = 0
                    for ghost in self.ghostGroup.sprites():
                        ghost.start = False
                else:
                    for ghost in self.ghostGroup.sprites():
                        if not ghost.start:
                            ghost.image = ghost.pelleted["Normal"][ghost.count]
                            if self.count >= 20:
                                ghost.image = ghost.pelleted["Flashing"][ghost.count]
                        else:
                            ghost.image = ghost.eyes[ghost.direction]
                self.blinky.randomTurn()
                self.clyde.randomTurn()
                self.inky.updateTurn(self.pac.index)
                self.pinky.updateTurn(self.pac.index)
                self.moveGhosts(1)
            else:
                for ghost in self.ghostGroup.sprites():
                    ghost.updateTurn(self.pac.index)
                self.moveGhosts(2)
            # Keeps track of the number of ticks
            time_elapsed += self.clock.tick(self.frames_per_second)
            # Movement and collision detections
            self.movePac(3)
            # Draw
            self.drawGame()
            # Only animates every ~100 ms to make it normal speed
            if time_elapsed >= 200:
                self.animate()
                time_elapsed = 0
                if self.pac.powerpellet:
                    self.count += 1
                else:
                    self.count = 0

    def movePac(self, numPixels):
        # Moves numPixels but 1 at a time to make sure we don't miss anything
        for i in range(numPixels):
            self.keyPressed()
            self.pac.movement()
            self.checkCollision()

    def moveGhosts(self, numPixels):
        # Moves numPixels but 1 pixel ata time in order to make sure we don't
        # miss any turns or jump into walls
        for i in range(numPixels):
            for ghost in self.ghostGroup.sprites():
                ghost.movement()
            self.checkCollision()
            for ghost in self.ghostGroup.sprites():
                self.teleportCheck(ghost)
                self.horizontalWalls(ghost)
                self.verticalWalls(ghost)
                if ghost.turn:
                    self.turn(ghost)

    def menu(self):
        self.ready = image.load('images/Walls/Ready.png')
        self.reset()
        mixer.music.load('sounds/pacman_beginning.wav')
        mixer.music.play(-1)
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
                        mixer.music.stop()
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