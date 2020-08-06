import pygame
from .sprite import Sprite

class MovingSprite(Sprite):
    def __init__(self, arena, name):
        (self._from_pos, self._to_pos) = arena.start_pos(name)
        self._trans_pos = 0.5
        self._arrived = False
        self._start = True
        self._direction = None
        self._calculate_position()
        self._speed = 0.0
        self._speed_scale = 1.0
        Sprite.__init__(self, arena, self._x, self._y, name)

    def from_pos(self):
        return self._from_pos

    def to_pos(self):
        return self._to_pos

    def _in_portal(self):
        if self._from_pos.portal(self._direction) is not None:
            return True
        return False

    def _calculate_position(self):
        from_x = self._from_pos.x()
        from_y = self._from_pos.y()

        to_x = self._to_pos.x()
        to_y = self._to_pos.y()
        if self._in_portal():
            if self.direction == "left":
                to_x -= self._arena.rect().width
            elif self.direction == "right":
                to_x += self._arena.rect().width
            elif self.direction == "up":
                to_y -= self._arena.rect().height
            elif self.direction == "down":
                to_y += self._arena.rect().height
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
        if self._start:
            self._pick_initial_direction()
        if self._arrived:
            self._update_arrived()
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
