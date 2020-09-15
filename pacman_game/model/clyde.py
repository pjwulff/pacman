from .ghost import Ghost

class Clyde(Ghost):
    """! The orange 'Clyde' ghost."""
    def __init__(self, arena):
        """! Create a new Clyde ghost.

        @param arena The arena to which this Clyde belongs."""
        Ghost.__init__(self, arena, "clyde")
    
    def target(self, avatar, ghosts):
        if avatar.coordinate.distance(self.coordinate) > 8*24:
            return avatar.coordinate
        return self.start_pos
