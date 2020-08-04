import sys, pygame, json
from .arena import *
from .avatar import *

class Game:
    def __init__(self):
        self.screen_size = (672, 864)
        pygame.init()
        self.screen = pygame.display.set_mode(self.screen_size)
        self.arena = Arena()
        self.avatar = Avatar(self.arena)
        self.arena.draw(self.screen)
        self.game_loop()

    def win(self):
        print("You win!")

    def game_loop(self):
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            dots = self.arena.dots()
            powers = self.arena.powers()
            ghosts = self.arena.ghosts()

            if len(dots) == 0 and len(powers) == 0:
                self.win()
                sys.exit()

            self.avatar.erase(self.screen)
            for ghost in ghosts:
                ghosts[ghost].erase(self.screen)
            for dot in dots:
                dot.erase(self.screen)
            for power in powers:
                power.erase(self.screen)

            self.avatar.update()
            for ghost in ghosts:
                ghosts[ghost].update(self.avatar, ghosts)

            for dot in dots:
                dot.draw(self.screen)
            for power in powers:
                power.draw(self.screen)
            for ghost in ghosts:
                ghosts[ghost].draw(self.screen)
            self.avatar.draw(self.screen)
            pygame.display.flip()
            clock.tick(60)
