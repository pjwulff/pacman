from .coordinate import Coordinate
from .ghost import Ghost

## The pink "Pinky" ghost.
class Pinky(Ghost):

    ## Create a new Pinky ghost.
    #
    # @param arena The arena object where this Pinky ghost will live.
    def __init__(self, arena):
        Ghost.__init__(self, arena, "pinky")
    
    ## Returns Pinky's target when in chase mode. Pinky will try to target
    ## a few steps ahead of where the Avatar is currently heading.
    #
    # @param avatar The Avatar object.
    # @param ghosts A dictionry of ghosts.
    #
    # @return The target coordinates.
    def target(self, avatar, ghosts):
        avatar_from = avatar.from_pos
        avatar_to = avatar.to_pos
        dx = avatar_to.x - avatar_from.x
        dy = avatar_to.y - avatar_from.y
        x = avatar_from.x + 4*dx
        y = avatar_from.y + 4*dy
        return Coordinate(x, y)
