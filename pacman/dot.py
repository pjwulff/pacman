import pygame
from .sprite import Sprite

class Dot(Sprite):
    def __init__(self, arena, x, y):
        Sprite.__init__(self, arena, x, y, "data/dot.png")
