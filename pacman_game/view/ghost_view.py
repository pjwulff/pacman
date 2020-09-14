import cairo
import math
from .sprite_view import SpriteView

class GhostView(SpriteView):
    def __init__(self, ghost):
        SpriteView.__init__(self, ghost)

    def draw(self, cr):
        """! Draw this sprite to the screen.

        @param screen The PyGame screen to which this sprite to draw."""
        cr.save()
        cr.set_line_width(3)
        self._set_colour(cr)
        cr.arc(self._sprite.start_pos.x, self._sprite.start_pos.y, 12, 0, 2*math.pi)
        cr.close_path()
        cr.stroke()
        cr.restore()
        coord = self._sprite.coordinate
        if self._sprite.scared and self._sprite.alive:
            self._draw_scared(cr, coord.x, coord.y)
        else:
            if self._sprite.alive:
                self._draw_body(cr, coord.x, coord.y)
            self._draw_eyes(cr, coord.x, coord.y)

    def _set_colour(self, cr):
        if self._sprite.name == "blinky":
            cr.set_source_rgb(1.0, 0.0, 0.0)
        elif self._sprite.name == "pinky":
            cr.set_source_rgb(1.0, 0.0, 1.0)
        elif self._sprite.name == "inky":
            cr.set_source_rgb(0.5, 1.0, 1.0)
        elif self._sprite.name == "clyde":
            cr.set_source_rgb(1.0, 0.5, 0.0)

    def _draw_body(self, cr, x, y):
        self._set_colour(cr)
        cr.move_to(x, y)
        cr.arc(x, y, 9, math.pi, 0)
        cr.close_path()
        cr.fill()
        cr.move_to(x + 9, y)
        cr.line_to(x + 9, y + 9)
        cr.line_to(x - 9, y + 9)
        cr.line_to(x - 9, y)
        cr.close_path()
        cr.fill()

    def _draw_eyes(self, cr, x, y):
        fr = self._sprite.from_pos
        to = self._sprite.to_pos
        dx = to.x - fr.x
        dy = to.y - fr.y
        angle = math.atan2(dy, dx)
        ox = 2.0*math.cos(angle)
        oy = 2.0*math.sin(angle)
        cr.move_to(x+ox, y+oy)
        cr.set_source_rgb(0.0, 0.0, 0.0)
        cr.arc(x+ox-4.5, y+ox-2, 2.5, 0, 2*math.pi)
        cr.close_path()
        cr.fill()
        cr.arc(x+ox+4.5, y+ox-2, 2.5, 0, 2*math.pi)
        cr.close_path()
        cr.fill()
        cr.set_source_rgb(1.0, 1.0, 1.0)
        cr.arc(x+ox-4.5, y+ox-2, 2, 0, 2*math.pi)
        cr.close_path()
        cr.fill()
        cr.arc(x+ox+4.5, y+ox-2, 2, 0, 2*math.pi)
        cr.close_path()
        cr.fill()
        cr.set_source_rgb(0.0, 0.0, 0.0)
        ox = 2.5*math.cos(angle)
        oy = 2.5*math.sin(angle)
        cr.arc(x+ox-4.5, y+ox-2, 1, 0, 2*math.pi)
        cr.close_path()
        cr.fill()
        cr.arc(x+ox+4.5, y+ox-2, 1, 0, 2*math.pi)
        cr.close_path()
        cr.fill()
