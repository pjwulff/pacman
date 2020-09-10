import pygame
from .sprite_view import SpriteView

class InternalView(SpriteView):
    def __init__(self, power, image, arena_view):
        SpriteView.__init__(self, power, image, arena_view)

class PowerView:
    def __init__(self, arena_view):
        self._arena_view = arena_view
        self._image = pygame.image.load("data/power.png").convert()

    def view(self, power):
        return InternalView(power, self._image, self._arena_view)
