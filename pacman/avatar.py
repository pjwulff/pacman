import pygame
from .sprite import Sprite

class Avatar(Sprite):
    def __init__(self, arena):
        self.from_pos = arena.start_pos()
        self.to_pos = arena.start_pos()
        self.trans_pos = 0.0
        self.speed = 0.0/60.0
        self.direction = None
        self.arrived = True
        self._calculate_position()
        Sprite.__init__(self, arena, self.x_, self.y_, "data/avatar.png")

    def _calculate_position(self):
        from_x = self.from_pos.x()
        from_y = self.from_pos.y()

        to_x = self.to_pos.x()
        to_y = self.to_pos.y()
        self.x_ = from_x + (to_x - from_x) * self.trans_pos
        self.y_ = from_y + (to_y - from_y) * self.trans_pos

    def _new_direction(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT] and self.from_pos.neighbour("left") is not None:
            return "left"
        elif keys_pressed[pygame.K_RIGHT] and self.from_pos.neighbour("right") is not None:
            return "right"
        elif keys_pressed[pygame.K_UP] and self.from_pos.neighbour("up") is not None:
            return "up"
        elif keys_pressed[pygame.K_DOWN] and self.from_pos.neighbour("down") is not None:
            return "down"
        if self.from_pos.neighbour(self.direction) is not None:
            return self.direction
        else:
            return None

    def _turn_around(self):
        keys_pressed = pygame.key.get_pressed()
        if self.direction == "left" and keys_pressed[pygame.K_RIGHT]:
            return True
        if self.direction == "right" and keys_pressed[pygame.K_LEFT]:
            return True
        if self.direction == "up" and keys_pressed[pygame.K_DOWN]:
            return True
        if self.direction == "down" and keys_pressed[pygame.K_UP]:
            return True

    def _flip_direction(self):
        if self.direction == "left":
            return "right"
        if self.direction == "right":
            return "left"
        if self.direction == "up":
            return "down"
        if self.direction == "down":
            return "up"

    def update(self):
        if self.arrived:
            self.direction = self._new_direction()
            if self.direction is not None:
                self.to_pos = self.from_pos.neighbour(self.direction)
                distance = self.to_pos.distance(self.from_pos)
                self.speed = (60.0/60.0) / distance
                self.arrived = False
            else:
                self.speed = 0.0
        else:
            if self._turn_around():
                temp = self.from_pos
                self.from_pos = self.to_pos
                self.to_pos = temp
                self.direction = self._flip_direction()
                self.trans_pos = 1.0 - self.trans_pos
            self.trans_pos += self.speed
            self._calculate_position()
            if self.trans_pos >= 1.0:
                self.trans_pos = 0.0
                self.from_pos = self.to_pos
                self.arrived = True
