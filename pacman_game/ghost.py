import random
from .moving_sprite import MovingSprite

GHOST_WIDTH = 42
GHOST_HEIGHT = 42

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
        MovingSprite.__init__(self, arena, GHOST_WIDTH, GHOST_HEIGHT, name)
        self._mode = "scatter"
        self._scatter_target = self._arena.scatter_target(name)
        self._target = None
        self._reverse = True
        self._speed_scale = 1.0
        self._alive = True

    @property
    def scared(self):
        return self._mode == "frighten"

    @property
    def alive(self):
        """! Gets the status of whether or not the ghost is alive; ie., can be
        interacted with by the avatar.

        @returns True if the ghost is alive, False otherwise."""
        return self._alive

    def set_mode(self, mode):
        """! Set the movement mode for this ghost. In the game ghosts will normally
        alternate between 'scatter' and 'chase' mode. In scatter mode the ghosts
        will head towards to their own corner of the maze. In chase mode they
        will chase the avatar in their own particular way. When the avatar
        consumes a power pill the ghosts enter 'frighten' mode and move randomly.

        @param mode The movement mode this ghost should take on. Can be either
        'scatter', 'chase' or 'frighten'."""
        if self._mode == "chase" and mode != "chase":
            self._reverse = True
        if self._mode == "scatter" and mode != "scatter":
            self._reverse = True
        self._mode = mode

    def target(self, avatar, ghosts):
        """! Get the target for this ghost. Must be overridden by subclasses.

        @param avatar The avatar object in the same arena.
        @param ghosts A dictionary of the ghosts in the same arena.
        @returns The coordinates to where this ghost should head in chase mode."""
        return None

    def kill(self):
        """! Called when this ghost is touched by the avatar while a power pill
        is active. This 'kills' the ghost and causes it to return to the ghost
        prison in the centre of the maze."""
        self._alive = False
        self._reverse = True

    def _pick_initial_direction(self):
        self._direction = "right"
        self._start = False
        self._calculate_speed()

    def _turn_around(self):
        return False

    def update(self, avatar, ghosts):
        """! Move this ghost over the span of time of one frame.

        @param avatar The avatar object in the same arena.
        @param ghosts A dictionary of the ghosts in the same arena."""
        self._target = self.target(avatar, ghosts)
        MovingSprite.update(self)

    def _distance(self, direction, target):
        next_tile = self._from_pos.neighbour(direction)
        dx = (next_tile.x - target[0]) ** 2.0
        dy = (next_tile.y - target[1]) ** 2.0
        return dx + dy

    def _new_direction(self):
        if self._alive == False and self._from_pos == self._arena.ghost_return_position():
            self._alive = True
            self._mode = "scatter"
        if self._alive == False:
            pos = self._arena.ghost_return_position()
            target = (pos.x, pos.y)
        elif self._mode == "chase":
            target = self._target
        elif self._mode == "scatter":
            target = self._scatter_target
        valid_directions = []
        if self._from_pos.neighbour("left") is not None:
            valid_directions += ["left"]
        if self._from_pos.neighbour("right") is not None:
            valid_directions += ["right"]
        if self._from_pos.neighbour("up") is not None:
            valid_directions += ["up"]
        if self._from_pos.neighbour("down") is not None:
            valid_directions += ["down"]

        if self._reverse:
            self._reverse = False
        else:
            flipped = self._flip_direction()
            if flipped in valid_directions and len(valid_directions) > 1:
                valid_directions.remove(self._flip_direction())

        if self._mode == "frighten" and self._alive:
            return random.choice(valid_directions)
        else:
            best_direction = valid_directions[0]
            best_distance = self._distance(best_direction, target)
            for direction in valid_directions[1:]:
                dist = self._distance(direction, target)
                if dist < best_distance:
                    best_distance = dist
                    best_direction = direction
            return best_direction
