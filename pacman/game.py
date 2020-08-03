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

    def game_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            dots = self.arena.dots()
            self.avatar.erase(self.screen)
            for dot in dots:
                dot.erase(self.screen)
            self.avatar.draw(self.screen)
            for dot in dots:
                dot.draw(self.screen)
            pygame.display.flip()
