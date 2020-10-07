from ..model.angle import *

## A generic controller for all moving sprites. Intended to be used via
## inheritance by AvatarController and GhostController, as much of the logic
## of how these sprites move is identical.
class MovingSpriteController:
    ## Create a generic MovingSpriteController.
    #
    # @param sprite The sprite to control.
    def __init__(self, sprite):
        self._sprite = sprite
        self.speed_scale = 1.0
        self.return_to_spawn()
    
    ## Return this sprite to its spawn location in the map. This function also
    ## resets the sprite's speed and direction.
    def return_to_spawn(self):
        self._sprite.return_to_spawn()
        self._arrived = False
        self._start = True
        self.target_direction = None
        self.speed = 0.0

    ## Get the target direction this sprite would like to move in.
    #
    # @return The target direction.
    @property
    def target_direction(self):
        return self._target_direction
    
    ## Set the target direction this sprite would like to move in. If possible,
    ## this will allow the sprite to turn around.
    #
    # @param target_direction The target direction.
    @target_direction.setter
    def target_direction(self, target_direction):
        self._target_direction = target_direction
        if target_direction is not None and self.direction is not None and \
            opposite(target_direction, self.direction) and not self._arrived:
            self._turn_around()
    
    ## Causes the sprite to turn around and reverse its direction.
    def _turn_around(self):
        temp = self.sprite.from_pos
        self.sprite.from_pos = self.sprite.to_pos
        self.sprite.to_pos = temp
        self.sprite.trans_pos = 1.0 - self.sprite.trans_pos
        self.sprite.calculate_position()
    
    ## Gets the node in the maze from which this sprite is currently moving.
    #
    # @return A node in the maze.
    @property
    def from_pos(self):
        return self.sprite.from_pos
    
    ## Gets the sprite this controller is controlling.
    #
    # @return A sprite.
    @property
    def sprite(self):
        return self._sprite

    ## Gets the direction in which this sprite is currently actually moving
    ## (which may or may not be its target direction).
    #
    # @return A direction.
    @property
    def direction(self):
        return self.sprite.direction
        
    ## Gets the current movement speed of this sprite.
    #
    # @return A speed as a floating point number.
    @property
    def speed(self):
        return self._speed
    
    ## Set the movement speed for this sprite.
    #
    # @param speed The speed of this sprite as a floating point number.
    @speed.setter
    def speed(self, speed):
        self._speed = speed

    ## Get the speed scale for this sprite. Every sprite has its own speed
    ## scale, which dictates how quickly it can move between vertices in the
    ## maze.
    #
    # @return The speed scale for this sprite.
    @property
    def speed_scale(self):
        return self._speed_scale
    
    ## Set the speed scale for this sprite.
    #
    # @param speed_scale The speed scale.
    @speed_scale.setter
    def speed_scale(self, speed_scale):
        self._speed_scale = speed_scale

    ## Calculate how fast this sprite should be moving, based on the sprite's
    ## speed scale and how far apart the two nodes are between which it is
    ## moving
    #
    # @return The sprite's current movement speed.
    def _calculate_speed(self):
        distance = self.sprite.to_pos.distance(self.sprite.from_pos)
        if distance == 0.0:
            return 0.0000
        self._speed = self.speed_scale * 100.0 / distance

    ## Update this sprite over `delta' time. This involves moving it through
    ## the maze. When it reaches a vertex in the maze it has the opportunity
    ## to choose a new direction.
    #
    # @param delta The length of time passed since this sprite last moved.
    def step(self, delta):
        if self._start:
            direction = self._new_direction()
            if direction is not None:
                self._calculate_speed()
                self._start = False
        if self._arrived:
            direction = self._new_direction()
            new_to = self.sprite.from_pos.neighbour(direction, math.pi/4.)
            if new_to is not None:
                self.sprite.to_pos = new_to
                self._calculate_speed()
                self.sprite.calculate_position()
                self._arrived = False
            else:
                self.speed = 0
        else:
            self.sprite.trans_pos += self._speed * delta
            self.sprite.calculate_position()
            if self.sprite.trans_pos <= 0.0:
                self.sprite.trans_pos = 0.0
                self._arrived = True
            if self.sprite.trans_pos >= 1.0:
                self.sprite.trans_pos = 0.0
                self.sprite.from_pos = self.sprite.to_pos
                self._arrived = True

    ## Gets a new direction for this sprite when it reaches a vertex in the
    ## maze.
    #
    # @return A direction.
    def _new_direction(self):
        direction = self.target_direction
        if direction is not None:
            neighbour = self.sprite.from_pos.neighbour(direction, math.pi/4.)
            if neighbour is not None:
                return direction
        return self.direction
