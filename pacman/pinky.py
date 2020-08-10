import pygame
from .ghost import Ghost

class Pinky(Ghost):
    """! The pink 'Pinky' ghost."""
    def __init__(self, arena):
        """! Create a new Pinky ghost.

        @param arena The arena to which this Pinky belongs."""
        Ghost.__init__(self, arena, "pinky")

    def target(self, avatar, ghosts):
        """! Get the target for this Pinky ghost.
        Pinky will directly target the avatar as Blinky does, but will instead
        take into account the direction in which the avatar is moving and target
        four tiles ahead of the avatar's position.

        @param avatar The avatar object in the same arena.
        @param ghosts A dictionary of the ghosts in the same arena.
        @returns The coordinates of the Pinky ghost in chase mode."""
        avatar_from = avatar.from_pos()
        avatar_to = avatar.to_pos()
        dx = avatar_to.x() - avatar_from.x()
        dy = avatar_to.y() - avatar_from.y()
        x = avatar_from.x() + 4*dx
        y = avatar_from.y() + 4*dy
        return (x, y)
