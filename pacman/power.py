import pygame
from .sprite import Sprite

class Power(Sprite):
    def __init__(self, arena, x, y):
        Sprite.__init__(self, arena, x, y, "power")
