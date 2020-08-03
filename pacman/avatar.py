import pygame
from .sprite import Sprite

class Avatar(Sprite):
    def __init__(self, arena):
        self.from_pos = arena.start_pos()
        self.to_pos = arena.start_pos()
        self.trans_pos = 0.0
        self.direction = "left"
        (x, y) = self._calculate_position()
        Sprite.__init__(self, arena, x, y, "data/avatar.png")

    def _calculate_position(self):
        from_x = self.from_pos.x()
        from_y = self.from_pos.y()

        to_x = self.to_pos.x()
        to_y = self.to_pos.y()
        x = from_x + (to_x - from_x) * self.trans_pos
        y = from_y + (to_y - from_y) * self.trans_pos
        return (x, y)
