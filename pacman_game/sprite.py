from .rect import Rect

class Sprite:
    """! Base class for all displayable sprites.

    """
    def __init__(self, arena, x, y, width, height, name):
        """! Base constructor for sprites.

        @param arena The arena to which this sprite belongs.
        @param x,y   The coordinates where this sprite should spawn.
        @param name  The name of this sprite."""
        self._arena = arena
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._name = name

    @property
    def visible(self):
        return self._visible

    @visible.setter
    def visible(self, v):
        self.visible = v

    @property
    def position(self):
        """! Get the coordinates of this sprite.

        @returns The coordinates of this sprite."""
        return (self._x, self._y)

    @property
    def rect(self):
        """! Get the rect object describing this sprite.

        @returns The rect object describing this sprite."""
        return Rect(self._width, self._height,
                    int(self._x - self._width/2),
                    int(self._y - self._height/2))

    def collide(self, other):
        """! Detects if this sprite overlaps another.
        Uses only simple rectangles to perform hit detection.

        @returns True if the two sprites overlap, False otherwise."""
        return self.rect.collide(other.rect)

    @property
    def name(self):
        """! Gets the name of this sprite.

        @returns The name of this sprite."""
        return self._name
