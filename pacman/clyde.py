import pygame
from .ghost import Ghost

class Clyde(Ghost):
    def __init__(self, arena):
        Ghost.__init__(self, arena, "clyde")
