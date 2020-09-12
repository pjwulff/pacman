from ..model.direction import Direction

class MovingSpriteController:
    def __init__(self, sprite):
        self._sprite = sprite
        self.speed_scale = 1.0
        self.return_to_spawn()
    
    def return_to_spawn(self):
        self._sprite.return_to_spawn()
        self._arrived = False
        self._start = True
        self.target_direction = Direction()
        self.speed = 0.0

    @property
    def target_direction(self):
        return self._target_direction
    
    @target_direction.setter
    def target_direction(self, target_direction):
        self._target_direction = target_direction
        if target_direction == self.direction.flip():
            self._turn_around()
    
    def add_direction(self, direction):
        self.target_direction.add_direction(direction)
    
    def remove_direction(self, direction):
        self.target_direction.remove_direction(direction)
    
    def _turn_around(self):
        temp = self.sprite.from_pos
        self.sprite.from_pos = self.sprite.to_pos
        self.sprite.to_pos = temp
        self.sprite.trans_pos = 1.0 - self.sprite.trans_pos
    
    @property
    def from_pos(self):
        return self.sprite.from_pos
    
    @property
    def sprite(self):
        return self._sprite

    @property
    def direction(self):
        return self.sprite.direction
    
    @direction.setter
    def direction(self, direction):
        self.sprite.direction = direction
        
    @property
    def speed(self):
        return self._speed
    
    @speed.setter
    def speed(self, speed):
        self._speed = speed
        
    @property
    def speed_scale(self):
        return self._speed_scale
    
    @speed_scale.setter
    def speed_scale(self, speed_scale):
        self._speed_scale = speed_scale

    def _calculate_speed(self):
        distance = self.sprite.to_pos.distance(self.sprite.from_pos)
        self._speed = self.speed_scale * 150.0 / distance

    def step(self, delta):
        """! Update this sprite over the span of time of one frame. This moves
        the sprite between two vertices in the graph. When it reaches a vertex
        it calls the protected _new_direction method to pick a new direction.
        This method must be overridden by subclasses."""
        if self._start:
            direction = self._new_direction()
            if direction is not None:
                self.direction = direction
                self._calculate_speed()
                self._start = False
        if self._arrived:
            self.direction = self._new_direction()
            if self.direction is not None:
                self.sprite.to_pos = self.sprite.from_pos.neighbour(self.direction)
                self._calculate_speed()
                self._arrived = False
            else:
                self.speed = 0.0
        else:
            self.sprite.trans_pos += self._speed * delta
            self.sprite.calculate_position()
            if self.sprite.trans_pos < 0.0:
                self.sprite.trans_pos = 0.0
                self._arrived = True
            if self.sprite.trans_pos >= 1.0:
                self.sprite.trans_pos = 0.0
                self.sprite.from_pos = self.sprite.to_pos
                self._arrived = True

    def _new_direction(self):
        direction = self.target_direction
        if "left" in direction and self.sprite.from_pos.neighbour("left") is not None:
            return Direction("left")
        elif "right" in direction and self.sprite.from_pos.neighbour("right") is not None:
            return Direction("right")
        elif "up" in direction and self.sprite.from_pos.neighbour("up") is not None:
            return Direction("up")
        elif "down" in direction and self.sprite.from_pos.neighbour("down") is not None:
            return Direction("down")
        if self.sprite.from_pos.neighbour(self.direction) is not None:
            return self.direction
        else:
            return None

    def _pick_initial_direction(self):
        self.direction = self._new_direction()
        if self.direction.valid():
            self._start = False
            if self.sprite.from_pos.neighbour(self.direction) != self.sprite.to_pos:
                self._turn_around()
            self._calculate_speed()
