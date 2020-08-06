import pygame
from .ghost import Ghost

class Inky(Ghost):
    def __init__(self, arena):
        Ghost.__init__(self, arena, "inky")

    def target(self, avatar, ghosts):
        avatar_from = avatar.from_pos()
        avatar_to = avatar.to_pos()
        dx = avatar_to.x() - avatar_from.x()
        dy = avatar_to.y() - avatar_from.y()
        x = avatar_from.x() + 2*dx
        y = avatar_from.y() + 2*dy
        (blinky_x, blinky_y) = ghosts["blinky"].position()
        x = 2*x - blinky_x
        y = 2*y - blinky_y
        return (x, y)
