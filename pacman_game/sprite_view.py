import pygame

class SpriteView:
    def __init__(self, sprite, image, arena_view):
        self._sprite = sprite
        self._image = image
        self._arena_view = arena_view

    def erase(self, screen):
        """! Erase this sprite from the screen,
        so that it can be redrawn somewhere else.

        @param screen The PyGame screen object to modify."""
        self._arena_view.draw(screen, self.rect)

    def draw(self, screen):
        """! Draw this sprite to the screen.

        @param screen The PyGame screen to which this sprite to draw."""
        screen.blit(self._image, self.rect)

    @property
    def rect(self):
        sr = self._sprite.rect
        return pygame.Rect(sr.x, sr.y, sr.width, sr.height)
