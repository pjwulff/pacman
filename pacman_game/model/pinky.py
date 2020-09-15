from .ghost import Ghost

class Pinky(Ghost):
    """! The pink 'Pinky' ghost."""
    def __init__(self, arena):
        """! Create a new Pinky ghost.

        @param arena The arena to which this Pinky belongs."""
        Ghost.__init__(self, arena, "pinky")
    
    def target(self, avatar, ghosts):
        return avatar.coordinate
