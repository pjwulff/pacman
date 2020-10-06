from .coordinate import Coordinate
from .ghost import Ghost

## The cyan "Inky" ghost.
class Inky(Ghost):

    ## Create a new Inky ghost.
    #
    # @param arena The Arena object where this Inky ghost will live.
    def __init__(self, arena):
        Ghost.__init__(self, arena, "inky")
    
    ## Returns Inky's target when in chase mode, which as in the original game,
    ## is based on the Avatar's current location, direction, and Blinky's
    ## direction.
    #
    # @param avatar The Avatar object.
    # @param ghosts A dictionary of the ghosts.
    #
    # @return The target coordinates.
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
