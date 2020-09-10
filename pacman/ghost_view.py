import pygame
from .sprite_view import SpriteView

class GhostView(SpriteView):
    def __init__(self, ghost, arena_view):
        image = pygame.image.load(f"data/{ghost.name}.png").convert()
        SpriteView.__init__(self, ghost, image, arena_view)
        self._scared_image = pygame.image.load("data/scared-ghost.png").convert()
        self._eyes = {
            "up": pygame.image.load("data/eyes-up.png").convert(),
            "down": pygame.image.load("data/eyes-down.png").convert(),
            "left": pygame.image.load("data/eyes-left.png").convert(),
            "right": pygame.image.load("data/eyes-right.png").convert()
        }

    def draw(self, screen):
        """! Draw this sprite to the screen.

        @param screen The PyGame screen to which this sprite to draw."""
        if self._sprite.scared and self._sprite.alive:
                screen.blit(self._scared_image, self.rect)
        else:
            if self._sprite.alive:
                screen.blit(self._image, self.rect)
            screen.blit(self._eyes[self._sprite.direction], self.rect)
