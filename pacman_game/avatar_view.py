import pygame, pkg_resources
from .sprite_view import SpriteView

class AvatarView(SpriteView):
    def __init__(self, avatar, arena_view):
        path = pkg_resources.resource_filename(__name__, "data/avatar.png")
        image = pygame.image.load(path).convert()
        SpriteView.__init__(self, avatar, image, arena_view)
