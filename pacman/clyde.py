import pygame
from .ghost import Ghost

class Clyde(Ghost):
    """! The orange 'Clyde' ghost."""
    def __init__(self, arena):
        """! Create a new Clyde ghost.

        @param arena The arena to which this Clyde belongs."""
        Ghost.__init__(self, arena, "clyde")

    def target(self, avatar, ghosts):
        """ Get the target for the Clyde ghost. When Clyde is more than
        8 tiles from the avatar, Clyde will head towards the avatar just as
        Blinky does. When within an 8 tiles range, Clyde will head towards
        its standard scatter target.

        @param avatar The avatar object in the same arena.
        @param ghosts A dictionary of the ghosts in the same arena.
        @returns The coordinates of Clyde's target in chase mode."""
        (avatar_x, avatar_y) = avatar.position
        (clyde_x, clyde_y) = self.position
        dx = (avatar_x - clyde_x) ** 2.0
        dy = (avatar_y - clyde_y) ** 2.0
        if (dx + dy) > 36864:
            return (avatar_x, avatar_y)
        else:
            return self._scatter_target
