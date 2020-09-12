from .ghost_controller import GhostController

class BlinkyController(GhostController):
    def __init__(self, sprite):
        super().__init__(sprite)

    def target(self, avatar, ghosts):
        """! Get the target for the Blinky ghost. Blinky's target is the
        position of the avatar.

        @param avatar The avatar in the arena.
        @param ghosts A dictionary for all ghosts in the arena.

        @returns The coordinate for the Blinky ghost in chase mode."""
        return avatar.coordinate
