from .sprite import Sprite

DOT_RADIUS = 3

class Dot(Sprite):
    """! Represents a dot in the maze."""
    def __init__(self, arena, coordinate):
        """! Construct a new dot object.

        @param arena The arena to which this dot belongs.
        @param x,y The coordinates where this dot should spawn."""
        Sprite.__init__(self, arena, coordinate, DOT_RADIUS, "dot")
