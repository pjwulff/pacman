from .ghost import Ghost

class Blinky(Ghost):
    """! The red 'Blinky' ghost."""
    def __init__(self, arena):
        """! Create a new Blinky ghost.

        @param arena The arena object to which this Blinky ghost belongs."""
        Ghost.__init__(self, arena, "blinky")
    
    def target(self, avatar, ghosts):
        return avatar.coordinate
