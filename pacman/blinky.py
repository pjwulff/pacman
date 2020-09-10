import pygame
from .ghost import Ghost

class Blinky(Ghost):
    """! The red 'Blinky' ghost."""
    def __init__(self, arena):
        """! Create a new Blinky ghost.

        @param arena The arena object to which this Blinky ghost belongs."""
        Ghost.__init__(self, arena, "blinky")

    def target(self, avatar, ghosts):
        """! Get the target for the Blinky ghost. Blinky's target is the
        position of the avatar.

        @param avatar The avatar in the arena.
        @param ghosts A dictionary for all ghosts in the arena.

        @returns The coordinate for the Blinky ghost in chase mode."""
        return avatar.position
