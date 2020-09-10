import pygame
from .sprite import Sprite

class MovingSprite(Sprite):
    """! Base class for all sprites which move during gameplay."""
    def __init__(self, arena, width, height, name):
        """! Construct a new moving sprite object.

        @param arena The arena to which this moving sprite belongs.
        @param name The name of this moving sprite."""
        self._arena = arena
        self._name = name
        self.return_to_spawn()
        self._calculate_position()
        Sprite.__init__(self, arena, self._x, self._y, width, height, name)

    def return_to_spawn(self):
        """! Instructs this moving sprite to return to its spawn location.
        Used when the avatar is hit by a ghost and loses a life."""
        (self._from_pos, self._to_pos) = self._arena.start_pos(self._name)
        self._trans_pos = 0.5
        self._arrived = False
        self._start = True
        self._direction = None
        self._speed = 0.0
        self._speed_scale = 1.0

    @property
    def from_pos(self):
        """! Moving sprites move between vertices in the graph. This method
        returns the vertex this sprite was moving from.

        @returns The node in the graph this sprite is moving from."""
        return self._from_pos

    @property
    def to_pos(self):
        """! Moving sprites move between vertices in the graph. This method
        returns the vertex this sprite is moving towards.

        @returns The node in the graph this sprite is moving to."""
        return self._to_pos

    @property
    def _in_portal(self):
        if self._from_pos.portal(self._direction) is not None:
            return True
        return False

    @property
    def direction(self):
        return self._direction

    def _calculate_position(self):
        from_x = self._from_pos.x
        from_y = self._from_pos.y

        to_x = self._to_pos.x
        to_y = self._to_pos.y
        if self._in_portal:
            if self._direction == "left":
                to_x -= self._arena.rect.width
            elif self._direction == "right":
                to_x += self._arena.rect.width
            elif self._direction == "up":
                to_y -= self._arena.rect.height
            elif self._direction == "down":
                to_y += self._arena.rect.height
        self._x = from_x + (to_x - from_x) * self._trans_pos
        self._y = from_y + (to_y - from_y) * self._trans_pos

    def _calculate_speed(self):
        distance = self._to_pos.distance(self._from_pos)
        self._speed = self._speed_scale * (150.0/60.0) / distance

    def _flip_direction(self):
        if self._direction == "left":
            return "right"
        if self._direction == "right":
            return "left"
        if self._direction == "up":
            return "down"
        if self._direction == "down":
            return "up"

    def update(self):
        """! Update this sprite over the span of time of one frame. This moves
        the sprite between two vertices in the graph. When it reaches a vertex
        it calls the protected _new_direction method to pick a new direction.
        This method must be overridden by subclasses."""
        if self._start:
            self._pick_initial_direction()
        if self._arrived:
            self._direction = self._new_direction()
            if self._direction is not None:
                self._to_pos = self._from_pos.neighbour(self._direction)
                self._calculate_speed()
                self._arrived = False
            else:
                self._speed = 0.0
        else:
            if self._turn_around():
                temp = self._from_pos
                self._from_pos = self._to_pos
                self._to_pos = temp
                self._direction = self._flip_direction()
                self._trans_pos = 1.0 - self._trans_pos
            self._trans_pos += self._speed
            self._calculate_position()
            if self._trans_pos < 0.0:
                self._trans_pos = 0.0
                self._arrived = True
            if self._trans_pos >= 1.0:
                self._trans_pos = 0.0
                self._from_pos = self._to_pos
                self._arrived = True
