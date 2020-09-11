import pygame, pkg_resources
from .arena import Arena

class ArenaView:
    def __init__(self, arena):
        self._arena = arena
        path = pkg_resources.resource_filename(__name__, f"data/{arena.image()}")
        self._image = pygame.image.load(path).convert()
        self._screen_rect = self._image.get_rect()

    def draw(self, screen, rect = None):
        """! Draws the entire arena background to the screen, or optionally
        just a section of it. This is used to erase a sprite.

        @param screen The PyGame screen object on which to draw.
        @param rect An optional Rect object to specify which part of the Arena
        to drawn. If not given, this method draws the entire arena."""
        if rect is None:
            screen.fill((0, 0, 0))
            screen.blit(self._image, self._screen_rect)
        else:
            rect = pygame.Rect(rect.x, rect.y, rect.width, rect.height)
            screen.blit(self._image, rect, rect)
