import pygame

class Sprite:
    """! Base class for all displayable sprites.

    """
    def __init__(self, arena, x, y, name):
        """! Base constructor for sprites.

        @param arena The arena to which this sprite belongs.
        @param x,y   The coordinates where this sprite should spawn.
        @param name  The name of this sprite."""
        self._name = name
        self._arena = arena
        self._x = x
        self._y = y
        self._image = pygame.image.load(f"data/{name}.png").convert()
        self._rect = self._image.get_rect()

    def erase(self, screen):
        """! Erase this sprite from the screen,
        so that it can be redrawn somewhere else.

        @param screen The PyGame screen object to modify."""
        self._arena.draw(screen, self.rect())

    def draw(self, screen):
        """! Draw this sprite to the screen.

        @param screen The PyGame screen to which this sprite to draw."""
        screen.blit(self._image, self.rect())

    def position(self):
        """! Get the coordinates of this sprite.

        @returns The coordinates of this sprite."""
        return (self._x, self._y)

    def rect(self):
        """! Get the rect object describing this sprite.

        @returns The rect object describing this sprite."""
        (x, y) = self.position()
        x -= self._rect.width/2
        y -= self._rect.height/2
        return self._rect.move(x, y)

    def collide(self, other):
        """! Detects if this sprite overlaps another.
        Uses only simple rectangles to perform hit detection.

        @returns True if the two sprites overlap, False otherwise."""
        return self.rect().colliderect(other.rect())

    def name(self):
        """! Gets the name of this sprite.

        @returns The name of this sprite."""
        return self._name
