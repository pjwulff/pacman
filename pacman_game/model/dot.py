from .sprite import Sprite

DOT_RADIUS = 3

## Represents a `dot' in the maze.
class Dot(Sprite):

    ## Create a new dot object.
    #
    # @param coordinate The coordinates where this dot will be located.
    def __init__(self, coordinate):
        Sprite.__init__(self, coordinate, DOT_RADIUS, "dot")
