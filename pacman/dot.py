import pygame
from .sprite import Sprite

DOT_WIDTH = 6
DOT_HEIGHT = 6

class Dot(Sprite):
    """! Represents a dot in the maze."""
    def __init__(self, arena, x, y):
        """! Construct a new dot object.

        @param arena The arena to which this dot belongs.
        @param x,y The coordinates where this dot should spawn."""
        Sprite.__init__(self, arena, x, y, DOT_WIDTH, DOT_HEIGHT, "dot")
