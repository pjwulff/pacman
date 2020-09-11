import pygame, pkg_resources
from .arena_view import ArenaView
from .avatar_view import AvatarView
from .banner_view import BannerView
from .dot_view import DotView
from .ghost_view import GhostView
from .power_view import PowerView

class GameView:
    def __init__(self):
        self._screen_size = (672, 864)
        pygame.init()
        self._screen = pygame.display.set_mode(self._screen_size)

    def banner(self, mode, next, exit, score = None):
        BannerView(self._screen, mode, next, exit, score)

    def game_view(self, state):
        return InternalView(self._screen, state)

    @property
    def time(self):
        return pygame.time.get_ticks()/1000.0

class InternalView:
    def __init__(self, screen, state):
        self._screen = screen
        self._state = state
        self._arena_view = ArenaView(state.arena)
        self._arena_view.draw(self._screen)
        self._avatar_view = AvatarView(state.avatar, self._arena_view)
        self._ghost_views = {}
        for ghost in state.ghosts:
            self._ghost_views[ghost] = GhostView(state.ghosts[ghost], self._arena_view)
        self._dot_view = DotView(self._arena_view)
        self._power_view = PowerView(self._arena_view)

    def tick(self, step, exit):
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                    return
            direction = {}
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]: direction["left"] = "left"
            if keys[pygame.K_RIGHT]: direction["right"] = "right"
            if keys[pygame.K_UP]: direction["up"] = "up"
            if keys[pygame.K_DOWN]: direction["down"] = "down"
            self._erase()
            if not step(self._state, pygame.time.get_ticks()/1000.0, direction):
                return
            self._draw()
            clock.tick(60)

    def _erase(self):
        self._avatar_view.erase(self._screen)
        for ghost in self._ghost_views:
            self._ghost_views[ghost].erase(self._screen)
        for dot in self._state.dots:
            self._dot_view.view(dot).erase(self._screen)
        for power in self._state.powers:
            self._power_view.view(power).erase(self._screen)

    def _draw(self):
        for dot in self._state.dots:
            self._dot_view.view(dot).draw(self._screen)
        for power in self._state.powers:
            self._power_view.view(power).draw(self._screen)
        for ghost in self._ghost_views:
            self._ghost_views[ghost].draw(self._screen)
        self._avatar_view.draw(self._screen)
        pygame.display.flip()
