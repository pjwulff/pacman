import sys, pygame
from .game_state import GameState

class Game:
    """! A class to control the running of the game."""
    def __init__(self):
        """! Construct a new Game object."""
        self._screen_size = (672, 864)
        pygame.init()
        self._screen = pygame.display.set_mode(self._screen_size)
        self._mode = "start"
        self._banner("start", self._start)

    def _start(self):
        if self._game_loop() == "win":
            self._banner("win", self._win)
        else:
            self._banner("lose", self._lose)
        return True

    def _banner(self, path, next):
        image = pygame.image.load(f"data/{path}.png").convert()
        image_rect = image.get_rect().move(228, 258)
        self._screen.fill((0, 0, 0))
        self._screen.blit(image, image_rect)
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    if image_rect.collidepoint(event.pos):
                        if not next():
                            return
                        self._screen.fill((0, 0, 0))
                        self._screen.blit(image, image_rect)
                        pygame.display.flip()

    def _win(self):
        return False

    def _lose(self):
        return False

    def _game_loop(self):
        self._game_state = GameState()
        self._game_state.arena().draw(self._screen)
        clock = pygame.time.Clock()
        self._game_state.start()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self._game_state.erase(self._screen)
            self._game_state.update()
            if self._game_state.over():
                return self._game_state.condition()
            self._game_state.draw(self._screen)
            clock.tick(60)
