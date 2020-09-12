import cairo
import pkg_resources
from .sprite_view import SpriteView

class InternalView(SpriteView):
    def __init__(self, dot, image, arena_view):
        SpriteView.__init__(self, dot, image, arena_view)

class DotView:
    def __init__(self, arena_view):
        self._arena_view = arena_view
        path = pkg_resources.resource_filename(__name__, "../data/images/dot.png")
        self._image = cairo.ImageSurface.create_from_png(path)

    def view(self, dot):
        return InternalView(dot, self._image, self._arena_view)
