import cairo
import pkg_resources
from .sprite_view import SpriteView

class InternalView(SpriteView):
    def __init__(self, power, image, arena_view):
        SpriteView.__init__(self, power, image, arena_view)

class PowerView:
    def __init__(self, arena_view):
        self._arena_view = arena_view
        path = pkg_resources.resource_filename(__name__, "../data/images/power.png")
        self._image = cairo.ImageSurface.create_from_png(path)

    def view(self, power):
        return InternalView(power, self._image, self._arena_view)
