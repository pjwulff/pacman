import pygame
from .ghost import Ghost

class Pinky(Ghost):
    def __init__(self, arena):
        Ghost.__init__(self, arena, "pinky")
