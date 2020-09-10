import pygame
from .sprite_view import SpriteView

class InternalView(SpriteView):
    def __init__(self, dot, image, arena_view):
        SpriteView.__init__(self, dot, image, arena_view)

class DotView:
    def __init__(self, arena_view):
        self._arena_view = arena_view
        self._image = pygame.image.load("data/dot.png").convert()

    def view(self, dot):
        return InternalView(dot, self._image, self._arena_view)
