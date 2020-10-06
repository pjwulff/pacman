from .ghost import Ghost

## The red "Blinky" ghost.
class Blinky(Ghost):

    ## Create a new Blinky Ghost.
    #
    # @param arena The Arena object where this Blinky ghost will live.
    def __init__(self, arena):
        Ghost.__init__(self, arena, "blinky")
    
    ## Returns Blinky's target when in chase mode, which is just the Avatar's
    ## current location.
    #
    # @param avatar The avatar object.
    # @param ghosts A dictionary of the ghosts.
    #
    # @return The target coordinates.
    def target(self, avatar, ghosts):
        return avatar.coordinate
