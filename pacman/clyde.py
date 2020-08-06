import pygame
from .ghost import Ghost

class Clyde(Ghost):
    def __init__(self, arena):
        Ghost.__init__(self, arena, "clyde")

    def target(self, avatar, ghosts):
        (avatar_x, avatar_y) = avatar.position()
        (clyde_x, clyde_y) = self.position()
        dx = (avatar_x - clyde_x) ** 2.0
        dy = (avatar_y - clyde_y) ** 2.0
        if (dx + dy) > 36864:
            return (avatar_x, avatar_y)
        else:
            return self._scatter_target
