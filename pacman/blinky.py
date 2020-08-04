import pygame
from .ghost import Ghost

class Blinky(Ghost):
    def __init__(self, arena):
        Ghost.__init__(self, arena, "blinky")

    def target(self, avatar, ghosts):
        return avatar.position()
