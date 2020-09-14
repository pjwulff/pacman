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
        self.speed_scale = (1.0 + 9*self.speed_scale) / 10.0

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
        valid_neighbours = self.from_pos.neighbours[:]

        if self._reverse:
            self._reverse = False
        else:
            op_neighbour = self.from_pos.neighbour(self.direction.flip())
            if op_neighbour in valid_neighbours and len(valid_neighbours) > 1:
                valid_neighbours.remove(op_neighbour)

        if (self.mode == "frighten" or self.mode == "scatter") and self.alive:
            neighbour = random.choice(valid_neighbours)
        else:
            best_neighbour = valid_neighbours[0]
            best_distance = best_neighbour.distance(target)
            for neighbour in valid_neighbours[1:]:
                dist = neighbour.distance(target)
                if dist < best_distance:
                    best_distance = dist
                    best_neighbour = neighbour
            neighbour = best_neighbour
        return self.from_pos.direction(neighbour)
