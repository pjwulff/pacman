import cairo
import math
from .sprite_view import SpriteView

DOT_RADIUS = 2

class DotView(SpriteView):
    def __init__(self, dot):
        SpriteView.__init__(self, dot)

    def draw(self, cr):
        coord = self._sprite.coordinate
        x = coord.x
        y = coord.y
        cr.move_to(x, y)
        cr.arc(x, y, DOT_RADIUS, 0, 2*math.pi)
        cr.close_path()
        cr.set_source_rgb(1.0, 0.5, 0.0)
        cr.fill()
