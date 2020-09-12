import cairo
import pkg_resources
from .sprite_view import SpriteView

class AvatarView(SpriteView):
    def __init__(self, avatar, arena_view):
        path = pkg_resources.resource_filename(__name__, "../data/images/avatar.png")
        image = cairo.ImageSurface.create_from_png(path)
        SpriteView.__init__(self, avatar, image, arena_view)
