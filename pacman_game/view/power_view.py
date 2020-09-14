import cairo
from .sprite_view import SpriteView

POWER_RADIUS = 4

class PowerView(SpriteView):
    def __init__(self, power,):
        SpriteView.__init__(self, power)

    def draw(self, cr):
        coord = self._sprite.coordinate
        x = coord.x
        y = coord.y
        cr.move_to(x, y)
        cr.arc(x, y, POWER_RADIUS, 0, 2*math.pi)
        cr.close_path()
        cr.set_source_rgb(1.0, 0.5, 0.0)
        cr.fill()
