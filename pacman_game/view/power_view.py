import cairo
import math
from .sprite_view import SpriteView

POWER_RADIUS = 4

## A view to draw power pills.
class PowerView(SpriteView):

    ## Create a new PowerViwe object.
    #
    # @param power The power pill we are viewing.
    def __init__(self, power):
        SpriteView.__init__(self, power)

    ## Draw the power pill.
    #
    # @param cr The cairo context to be used for drawing.
    def draw(self, cr):
        coord = self._sprite.coordinate
        x = coord.x
        y = coord.y
        cr.move_to(x, y)
        cr.arc(x, y, POWER_RADIUS, 0, 2*math.pi)
        cr.close_path()
        cr.set_source_rgb(1.0, 0.5, 0.0)
        cr.fill()
