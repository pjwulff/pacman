from .coordinate import Coordinate
from .ghost import Ghost

class Pinky(Ghost):
    """! The pink 'Pinky' ghost."""
    def __init__(self, arena):
        """! Create a new Pinky ghost.

        @param arena The arena to which this Pinky belongs."""
        Ghost.__init__(self, arena, "pinky")
    
    def target(self, avatar, ghosts):
        avatar_from = avatar.from_pos
        avatar_to = avatar.to_pos
        dx = avatar_to.x - avatar_from.x
        dy = avatar_to.y - avatar_from.y
        x = avatar_from.x + 4*dx
        y = avatar_from.y + 4*dy
        return Coordinate(x, y)
