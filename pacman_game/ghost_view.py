import pygame, pkg_resources
from .sprite_view import SpriteView

class GhostView(SpriteView):
    def __init__(self, ghost, arena_view):
        path = pkg_resources.resource_filename(__name__, f"data/{ghost.name}.png")
        image = pygame.image.load(path).convert()
        SpriteView.__init__(self, ghost, image, arena_view)
        path = pkg_resources.resource_filename(__name__, "data/scared-ghost.png")
        self._scared_image = pygame.image.load(path).convert()
        eyes_path = {
            "up": "data/eyes-up.png",
            "down": "data/eyes-down.png",
            "left": "data/eyes-left.png",
            "right": "data/eyes-right.png",
        }
        self._eyes = {}
        for path in eyes_path:
            p = pkg_resources.resource_filename(__name__, eyes_path[path])
            self._eyes[path] = pygame.image.load(p).convert()

    def draw(self, screen):
        """! Draw this sprite to the screen.

        @param screen The PyGame screen to which this sprite to draw."""
        if self._sprite.scared and self._sprite.alive:
                screen.blit(self._scared_image, self.rect)
        else:
            if self._sprite.alive:
                screen.blit(self._image, self.rect)
            screen.blit(self._eyes[self._sprite.direction], self.rect)
