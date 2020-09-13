from .ghost_controller import GhostController

class InkyController(GhostController):
    def __init__(self, sprite, difficulty):
        super().__init__(sprite, difficulty)

    def target(self, avatar, ghosts):
        """! Get the target for the Inky ghost in chase mode. Inky uses a complicated
        targeting method. It uses a combination of where the avatar is heading
        and the current location of the Blinky ghost. It draws a vector between
        the Blinky ghost's location and a point two tiles in front of the avatar.
        It then extends that vector's length by two to find Inky's target.

        @param avatar The avatar object in the same arena.
        @param ghosts A dictionary of the ghosts in the same arena.
        @returns The coordinates for the Inky ghost in chase mode."""
        avatar_from = avatar.from_pos
        avatar_to = avatar.to_pos
        dx = avatar_to.x - avatar_from.x
        dy = avatar_to.y - avatar_from.y
        x = avatar_from.x + 2*dx
        y = avatar_from.y + 2*dy
        coord = ghosts["blinky"].coordinate
        x = 2*x - coord.x
        y = 2*y - coord.y
        return (x, y)
