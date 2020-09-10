import pygame
from .sprite import Sprite

POWER_WIDTH = 24
POWER_HEIGHT = 24

class Power(Sprite):
    """! A power pill."""
    def __init__(self, arena, x, y):
        """! Construct a new Power Pill.

        @param arena The arena to which this power pill belongs.
        @param x,y The coordinates of this power pill."""
        Sprite.__init__(self, arena, x, y, POWER_WIDTH, POWER_HEIGHT, "power")
