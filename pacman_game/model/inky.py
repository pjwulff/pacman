from .coordinate import Coordinate
from .ghost import Ghost

class Inky(Ghost):
    """! The cyan 'Inky' ghost."""
    def __init__(self, arena):
        """! Construct a new Inky ghost.

        @param arena The arena object to which this Inky belongs."""
        Ghost.__init__(self, arena, "inky")
    
    def target(self, avatar, ghosts):
        avatar_from = avatar.from_pos
        avatar_to = avatar.to_pos
        dx = avatar_to.x - avatar_from.x
        dy = avatar_to.y - avatar_from.y
        x = avatar_from.x + 2*dx
        y = avatar_from.y + 2*dy
        coord = ghosts["blinky"].coordinate
        x = 2*x - coord.x
        y = 2*y - coord.y
        return Coordinate(x, y)
