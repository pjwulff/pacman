import pygame
from .ghost import Ghost

class Inky(Ghost):
    def __init__(self, arena):
        Ghost.__init__(self, arena, "inky")
