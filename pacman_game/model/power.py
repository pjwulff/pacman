from .sprite import Sprite

POWER_RADIUS = 12

## Represents a `power pill' in the maze.
class Power(Sprite):

    ## Create a new Power object.
    #
    # @param coordinate The coordinates where this power pill will be located.
    def __init__(self, coordinate):
        Sprite.__init__(self, coordinate, POWER_RADIUS, "power")
