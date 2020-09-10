import pygame
from .sprite_view import SpriteView

class AvatarView(SpriteView):
    def __init__(self, avatar, arena_view):
        image = pygame.image.load("data/avatar.png").convert()
        SpriteView.__init__(self, avatar, image, arena_view)
