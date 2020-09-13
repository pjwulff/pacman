import random
from ..model.coordinate import Coordinate
from ..model.direction import Direction
from .moving_sprite_controller import MovingSpriteController

class GhostController(MovingSpriteController):
    def __init__(self, sprite, difficulty):
        super().__init__(sprite)
        if difficulty == "easy":
            self.speed_scale = 0.25
        elif difficulty == "medium":
            self.speed_scale = 0.5
        elif difficulty == "hard":
            self.speed_scale = 0.75
        self._scatter_target = sprite.scatter_target
        self._target = Coordinate()
        self._reverse = False
        
    def increase_difficulty(self):
        self.speed_scale = (1.0 + self.speed_scale) / 2.0

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
        self.alive = False
        self._reverse = True
    
    def plan(self, avatar, ghosts):
        self._target = self.target(avatar, ghost)

    def _distance(self, direction, target):
        next_tile = self.from_pos.neighbour(direction)
        if next_tile is None or target is None:
            return 1000.0
        dx = (next_tile.x - target.x) ** 2.0
        dy = (next_tile.y - target.y) ** 2.0
        return dx + dy

    @property
    def alive(self):
        return self.sprite.alive

    @alive.setter
    def alive(self, alive):
        self.sprite.alive = alive

    @property
    def mode(self):
        return self.sprite.mode

    @mode.setter
    def mode(self, mode):
        """! Set the movement mode for this ghost. In the game ghosts will normally
        alternate between 'scatter' and 'chase' mode. In scatter mode the ghosts
        will head towards to their own corner of the maze. In chase mode they
        will chase the avatar in their own particular way. When the avatar
        consumes a power pill the ghosts enter 'frighten' mode and move randomly.

        @param mode The movement mode this ghost should take on. Can be either
        'scatter', 'chase' or 'frighten'."""
        if self.sprite.mode == "chase" and mode != "chase":
            self.sprite.reverse = True
        if self.sprite.mode == "scatter" and mode != "scatter":
            self.sprite.reverse = True
        self.sprite.mode = mode

    def _new_direction(self):
        target = None
        if self.alive == False:
            if self.from_pos == self.sprite.return_position:
                self.alive = True
            else:
                pos = self.sprite.return_position
                target = Coordinate(pos.x, pos.y)
        elif self.mode == "chase":
            target = self._target
        elif self.mode == "scatter":
            target = self._scatter_target
        valid_directions = []
        if self.from_pos.neighbour("left") is not None:
            valid_directions += ["left"]
        if self.from_pos.neighbour("right") is not None:
            valid_directions += ["right"]
        if self.from_pos.neighbour("up") is not None:
            valid_directions += ["up"]
        if self.from_pos.neighbour("down") is not None:
            valid_directions += ["down"]

        if self._reverse:
            self._reverse = False
        else:
            flipped = str(self.direction.flip())
            if flipped in valid_directions and len(valid_directions) > 1:
                valid_directions.remove(flipped)

        if self.mode == "frighten" and self.alive:
            return Direction(random.choice(valid_directions))
        else:
            valid_directions = [Direction(d) for d in valid_directions]
            best_direction = valid_directions[0]
            best_distance = self._distance(best_direction, target)
            for direction in valid_directions[1:]:
                dist = self._distance(direction, target)
                if dist < best_distance:
                    best_distance = dist
                    best_direction = direction
            return best_direction
