import random
from ..model.angle import *
from ..model.coordinate import Coordinate
from .moving_sprite_controller import MovingSpriteController

## A generic controller for all ghosts.
class GhostController(MovingSpriteController):

    ## Create a GhostController.
    #
    # @param sprite The ghost this controller should control.
    # @param difficulty The difficulty level of the game, used to decide the
    # speed of the ghost.
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
    
    ## Reset this ghost. This moves the ghost back to its spawn location,
    ## make the ghost `alive' and changes its current behaviour to `scatter'
    def reset(self):
        self.return_to_spawn()
        self._sprite.alive = True
        self._reverse = False
        self._sprite.mode = "scatter"
        
    ## Increase the difficulty for this ghost, which currently only means
    ## increasing the ghost's speed.
    def increase_difficulty(self):
        self.speed_scale = (1.0 + 9*self.speed_scale) / 10.0
    
    ## Recalculate the target for this ghost; i.e., where this ghost should go
    ## when in `chase' mode. Each ghost has its own targeting method, and as
    ## controller works generically for all ghosts, this uses the Sprite's
    ## `target' function.
    #
    # @param avatar The avatar sprite.
    # @param ghosts A list of ghosts in the game.
    def update_target(self, avatar, ghosts):
        if self._arrived:
            self._target = self.sprite.target(avatar, ghosts)

    ## Kill the ghost. Callec when the Avatar eats the ghost. This makes the
    ## ghost intangible and head back to its spawn location.
    def kill(self):
        self.alive = False
        self._reverse = True

    ## Get whether or not this ghost is `alive'.
    #
    # @return True if this ghost is alive.
    @property
    def alive(self):
        return self.sprite.alive

    ## Set whether or not this ghost is alive.
    #
    # @param alive If the ghost is alive or not.
    @alive.setter
    def alive(self, alive):
        self.sprite.alive = alive

    ## Get the current mode or behaviour for this ghost.
    #
    # @return The current mode or behaviour for this ghost. Should only be
    # "scatter", "chase" or "frighten".
    @property
    def mode(self):
        return self.sprite.mode

    ## Set the current mode or behaviour for this ghost.
    #
    # @param mode The current mode of behaviour for this ghost. Should only be
    # "scatter", "chase" or "frighten". Normally ghosts cannot reverse their
    # directions, but they can when they change mode.
    @mode.setter
    def mode(self, mode):
        if self.sprite.mode == "chase" and mode != "chase":
            self.sprite.reverse = True
        if self.sprite.mode == "scatter" and mode != "scatter":
            self.sprite.reverse = True
        self.sprite.mode = mode
    
    ## Get a direction for this ghost to use when in scatter mode.
    #
    # @return A direction.
    def _scatter_direction(self):
        neighbours = self.from_pos.neighbours[:]
        if self._last_pos in neighbours:
            neighbours.remove(self._last_pos)
        self.sprite._path = None
        self._last_pos = self.from_pos
        return self.from_pos.direction(random.choice(neighbours))
    
    ## Get a direction for this ghost to move in when it is returning to its
    ## spawn location.
    #
    # @return A direction.
    def _respawn_direction(self):
        if self.from_pos == self.sprite.start_pos:
            self.alive = True
        pos = self.sprite.start_pos
        target = Coordinate(pos.x, pos.y)
        return self._generic_direction(target)
    
    ## Get a direction this ghost should use when heading towards a generic
    ## `target'. This function ultimately uses an A*-search to find the best
    ## path towards a target, and chooses that direction.
    #
    # @param target A target to head towards.
    # @return A direction.
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
        
    ## Get a direction for this ghost when it is in chase mode. Every ghost has
    ## its own target when in chase mode, and this function returns the best
    ## direction to use to head towards that target.
    #
    # @return A direction.
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
