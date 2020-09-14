from .sprite import Sprite

POWER_RADIUS = 12

class Power(Sprite):
    """! A power pill."""
    def __init__(self, coordinate):
        """! Construct a new Power Pill.

        @param arena The arena to which this power pill belongs.
        @param x,y The coordinates of this power pill."""
        Sprite.__init__(self, coordinate, POWER_RADIUS, "power")
