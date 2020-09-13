import cairo
import pkg_resources
from .sprite_view import SpriteView

POWER_RADIUS = 4

class InternalView(SpriteView):
    def __init__(self, power, image, arena_view):
        SpriteView.__init__(self, power, image, arena_view)

    def draw(self, cr):
        coord = self._sprite.coordinate
        x = coord.x
        y = coord.y
        cr.move_to(x, y)
        cr.arc(x, y, POWER_RADIUS, 0, 2*math.pi)
        cr.close_path()
        cr.set_source_rgb(1.0, 0.5, 0.0)
        cr.fill()

class PowerView:
    def __init__(self, arena_view):
        self._arena_view = arena_view

    def view(self, power):
        return InternalView(power, None, self._arena_view)
