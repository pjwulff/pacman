import cairo
from ..model.rect import Rect

## An abstract base class for viewing an Arena.
class ArenaView:

    ## Create a new ArenaView
    #
    # @param arena The Arena object.
    # @param width The width of the view.
    # @param height The height of the view.
    def __init__(self, arena, width, height):
        self._arena = arena
        self._rect = Rect(width, height)
    
    ## Get a rectangle object that represents this view.
    #
    # @return A rectangle object.
    @property
    def rect(self):
        return self._rect
    
    ## Draw this view.
    #
    # @param cr A cairo context to use to draw.
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
