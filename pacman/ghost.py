import pygame, random
from .moving_sprite import MovingSprite

class Ghost(MovingSprite):
    def __init__(self, arena, name):
        MovingSprite.__init__(self, arena, name)
        self._mode = "scatter"
        self._scatter_target = self._arena.scatter_target(name)
        self._target = None
        self._reverse = True
        self._speed_scale = 0.95

    def set_mode(self, mode):
        if self._mode == "chase" and mode != "chase":
            self._reverse = True
        if self._mode == "scatter" and mode != "scatter":
            self._reverse = True
        self._mode = mode

    def target(self, avatar, ghosts):
        return None

    def _pick_initial_direction(self):
        self._direction = "right"
        self._start = False
        self._calculate_speed()

    def _turn_around(self):
        return False

    def update(self, avatar, ghosts):
        self._target = self.target(avatar, ghosts)
        MovingSprite.update(self)

    def _update_arrived(self):
        pass

    def _distance(self, direction, target):
        next_tile = self._from_pos.neighbour(direction)
        dx = (next_tile.x() - target[0]) ** 2.0
        dy = (next_tile.y() - target[1]) ** 2.0
        return dx + dy

    def _new_direction(self):
        if self._mode == "chase":
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
            if flipped in valid_directions:
                valid_directions.remove(self._flip_direction())

        if self._mode == "frightened":
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
