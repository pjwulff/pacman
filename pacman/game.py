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
        (condition, score) = self._game_loop()
        if condition == "win":
            self._banner("win", self._win, score)
        else:
            self._banner("lose", self._lose, score)
        return True

    def _list_numbers(self, num):
        neg = False
        if num < 0:
            neg = True
            num = -num
        lst = [num % 10]
        num = num // 10
        while num > 0:
            lst = [(num % 10)] + lst
            num = num // 10
        if neg:
            lst = ["-"] + lst
        return lst

    def _banner(self, path, next, score = None):
        image = pygame.image.load(f"data/{path}.png").convert()
        image_rect = image.get_rect().move(228, 258)
        self._screen.fill((0, 0, 0))
        self._screen.blit(image, image_rect)
        if score is not None:
            self._display_score(score)
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

    def _display_score(self, score):
        lst = self._list_numbers(score)
        length = len(lst)
        digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-"]
        digits = [pygame.image.load(f"data/{s}.png").convert() for s in digits]
        x = 336 - 24*length//2
        y = 336
        for digit in lst:
            if digit == "-":
                image = digits[10]
            else:
                image = digits[digit]
            rect = image.get_rect().move(x, y)
            self._screen.blit(image, rect)
            x += 24

    def _game_loop(self):
        game_state = GameState()
        game_state.arena().draw(self._screen)
        clock = pygame.time.Clock()
        game_state.start()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            game_state.erase(self._screen)
            game_state.update()
            if game_state.over():
                return (game_state.condition(), game_state.score())
            game_state.draw(self._screen)
            clock.tick(60)
