from .ghost import Ghost

class Inky(Ghost):
    """! The cyan 'Inky' ghost."""
    def __init__(self, arena):
        """! Construct a new Inky ghost.

        @param arena The arena object to which this Inky belongs."""
        Ghost.__init__(self, arena, "inky")
    
    def target(self, avatar, ghosts):
        return avatar.coordinate
