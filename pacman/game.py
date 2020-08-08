import sys, pygame
from .game_state import GameState

class Game:
    def __init__(self):
        self._screen_size = (672, 864)
        pygame.init()
        self._screen = pygame.display.set_mode(self._screen_size)
        self._game_state = GameState()
        self._game_state.arena().draw(self._screen)
        self._game_loop()

    def win(self):
        print("You win!")

    def _game_loop(self):
        clock = pygame.time.Clock()
        self._game_state.start()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self._game_state.erase(self._screen)
            self._game_state.update()
            self._game_state.draw(self._screen)
            clock.tick(60)
