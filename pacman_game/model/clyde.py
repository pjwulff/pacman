from .ghost import Ghost

## The orange "Clyde" ghost.
class Clyde(Ghost):

    ## Create a new Clyde ghost
    #
    # @param arena The Arena object where this Clyde ghost will live.
    def __init__(self, arena):
        Ghost.__init__(self, arena, "clyde")
    
    ## Returns Cylde's target when in chase mode, which is the Avatar's location
    ## when close enough, or Clyde's spawn location when close to the Avatar.
    #
    # @param avatar The Avatar object.
    # @param ghosts A dictionary of the ghosts.
    #
    # @return The target coordinates.
    def target(self, avatar, ghosts):
        if avatar.coordinate.distance(self.coordinate) > 8*24:
            return avatar.coordinate
        return self.start_pos
