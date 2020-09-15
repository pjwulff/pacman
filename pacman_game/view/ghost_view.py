import cairo
import math
from .sprite_view import SpriteView

class GhostView(SpriteView):
    def __init__(self, ghost):
        SpriteView.__init__(self, ghost)
        self._last_angle = 0

    def draw(self, cr):
        """! Draw this sprite to the screen.

        @param screen The PyGame screen to which this sprite to draw."""
        cr.save()
        # self._draw_path(cr)
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

    def _draw_path(self, cr):
        cr.save()
        self._set_colour(cr)
        cr.set_line_width(1)
        path = self._sprite._path
        if path is not None:
            for i in range(1, len(path)-1):
                cr.move_to(path[i].x, path[i].y)
                cr.line_to(path[i+1].x, path[i+1].y)
                cr.stroke()
        cr.restore()

    def _set_colour(self, cr):
        if self._sprite.name == "blinky":
            cr.set_source_rgb(1.0, 0.0, 0.0)
        elif self._sprite.name == "pinky":
            cr.set_source_rgb(1.0, 0.0, 1.0)
        elif self._sprite.name == "inky":
            cr.set_source_rgb(0.5, 1.0, 1.0)
        elif self._sprite.name == "clyde":
            cr.set_source_rgb(1.0, 0.5, 0.0)

    def _draw_scared(self, cr, x, y):
        cr.set_source_rgb(0, 0.25, 0.75)
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
        cr.set_source_rgb(1, 1, 1)
        cr.arc(x-4.5, y-3, 2, 0, 2*math.pi)
        cr.close_path()
        cr.fill()
        cr.arc(x+4.5, y-3, 2, 0, 2*math.pi)
        cr.close_path()
        cr.fill()
        cr.set_line_width(1)
        cr.arc(x-6, y+4, 1, math.pi, 0)
        cr.stroke()
        cr.arc(x-4, y+4, 1, 0, math.pi)
        cr.stroke()
        cr.arc(x-2, y+4, 1, math.pi, 0)
        cr.stroke()
        cr.arc(x, y+4, 1, 0, math.pi)
        cr.stroke()
        cr.arc(x+2, y+4, 1, math.pi, 0)
        cr.stroke()
        cr.arc(x+4, y+4, 1, 0, math.pi)
        cr.stroke()
        cr.arc(x+6, y+4, 1, math.pi, 0)
        cr.stroke()

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
        angle = self._sprite.direction
        if angle is None:
            angle = self._last_angle
        else:
            self._last_angle = angle
        ox = 2.0*math.cos(angle)
        oy = 2.0*math.sin(angle)
        cr.save()
        cr.translate(x+ox, y-oy)
        cr.set_source_rgb(0.0, 0.0, 0.0)
        cr.arc(-4.5, 0, 2.5, 0, 2*math.pi)
        cr.close_path()
        cr.fill()
        cr.arc(+4.5, 0, 2.5, 0, 2*math.pi)
        cr.close_path()
        cr.fill()
        cr.set_source_rgb(1.0, 1.0, 1.0)
        cr.arc(-4.5, 0, 2, 0, 2*math.pi)
        cr.close_path()
        cr.fill()
        cr.arc(+4.5, 0, 2, 0, 2*math.pi)
        cr.close_path()
        cr.fill()
        cr.translate(ox*0.5, -oy*0.5)
        cr.set_source_rgb(0.0, 0.0, 0.0)
        cr.arc(-4.5, 0, 1, 0, 2*math.pi)
        cr.close_path()
        cr.fill()
        cr.arc(+4.5, 0, 1, 0, 2*math.pi)
        cr.close_path()
        cr.fill()
        cr.restore()
