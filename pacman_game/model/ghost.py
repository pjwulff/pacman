import random
from .moving_sprite import MovingSprite

GHOST_RADIUS = 9

class Ghost(MovingSprite):
    """! Base class for all Ghost types. Handles duties common to all ghosts,
    including moving around the maze. This class expects the 'target' method
    to be overridden by subclasses to find where the ghost should head during
    'chase' mode."""
    def __init__(self, arena, name):
        """! Construct a new Ghost.

        @param arena The arena to which this ghost belongs.
        @param name The name of the ghost. This is used to extract relevant information
        from the arena object."""
        MovingSprite.__init__(self, arena, GHOST_RADIUS, name)
        self.alive = True
        self.mode = "scatter"
    
    @property
    def mode(self):
        return self._mode
    
    @mode.setter
    def mode(self, mode):
        self._mode = mode

    @property
    def scared(self):
        return self._mode == "frighten"

    @property
    def alive(self):
        """! Gets the status of whether or not the ghost is alive; ie., can be
        interacted with by the avatar.

        @returns True if the ghost is alive, False otherwise."""
        return self._alive

    @alive.setter
    def alive(self, alive):
        self._alive = alive
    
    @property
    def return_position(self):
        return self._arena.ghost_return_position()
    
    @property
    def scatter_target(self):
        return self._arena.scatter_target(self.name)
