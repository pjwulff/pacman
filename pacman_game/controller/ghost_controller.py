import random
from ..model.angle import *
from ..model.coordinate import Coordinate
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
        self._target = Coordinate()
        self._reverse = False
        self._last_pos = None
    
    def reset(self):
        self.return_to_spawn()
        self._sprite.alive = True
        self._reverse = False
        self._sprite.mode = "scatter"
        
    def increase_difficulty(self):
        self.speed_scale = (1.0 + 9*self.speed_scale) / 10.0
    
    def update_target(self, avatar, ghosts):
        if self._arrived:
            self._target = self.sprite.target(avatar, ghosts)

    def kill(self):
        """! Called when this ghost is touched by the avatar while a power pill
        is active. This 'kills' the ghost and causes it to return to the ghost
        prison in the centre of the maze."""
        self.alive = False
        self._reverse = True

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
    
    def _scatter_direction(self):
        neighbours = self.from_pos.neighbours[:]
        if self._last_pos in neighbours:
            neighbours.remove(self._last_pos)
        self.sprite._path = None
        self._last_pos = self.from_pos
        return self.from_pos.direction(random.choice(neighbours))
    
    def _respawn_direction(self):
        if self.from_pos == self.sprite.start_pos:
            self.alive = True
        pos = self.sprite.start_pos
        target = Coordinate(pos.x, pos.y)
        return self._generic_direction(target)
    
    def _generic_direction(self, target):
        if self._reverse:
            self._reverse = False
            self.sprite._path = self.sprite.path(self.from_pos, target)
        else:
            self.sprite._path = self.sprite.path(self.from_pos, target, self._last_pos)
        if self.sprite._path is None:
            return self._scatter_direction()
        neighbour = self.sprite._path[2]
        if neighbour is not None:
            self._last_pos = self.from_pos
        else:
            self.sprite._path = None
        return self.from_pos.direction(neighbour)
        
    def _chase_direction(self):
        return self._generic_direction(self._target)

    def _new_direction(self):
        if not self.alive:
            return self._respawn_direction()
        elif self.mode == "scatter":
            return self._scatter_direction()
        elif self.mode == "chase":
            return self._chase_direction()
        elif self.mode == "frighten":
            return self._respawn_direction()
