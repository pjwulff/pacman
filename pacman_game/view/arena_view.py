import cairo
from ..model.rect import Rect

class ArenaView:
    def __init__(self, arena, width, height):
        self._arena = arena
        self._rect = Rect(width, height)
    
    @property
    def rect(self):
        return self._rect
    
    def draw(self, cr):
        width = self.rect.width
        height = self.rect.height
        cr.set_line_cap(cairo.LINE_CAP_ROUND)
        cr.set_source_rgb(0, 0, 0)
        cr.paint()
        cr.set_line_width(3)
        cr.set_source_rgb(0.0, 0.0, 1.0)
        cr.move_to(0, 0)
        cr.line_to(width, 0)
        cr.line_to(width, height)
        cr.line_to(0, height)
        cr.line_to(0, 0)
        cr.stroke()
