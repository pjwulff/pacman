import cairo
import math
from .arena_view import ArenaView

## Concrete class of type ArenaView. This one class can be used for both
## viewing HexagonalArenas and GraphArenas.
class GraphArenaView(ArenaView):

    ## Create a new GraphArenaView.
    #
    # @param arena The Arena object we are viewing.
    def __init__(self, arena):
        rect = arena.rect
        super().__init__(arena, rect.width, rect.height)

    ## Draw the arena.
    #
    # @param cr The cairo context to be used for drawing.
    def draw(self, cr):
        width = self._arena.logical_width
        height = self._arena.logical_height
        cr.set_line_cap(cairo.LINE_CAP_ROUND)
        cr.set_source_rgb(0, 0, 0)
        cr.paint()
        base_angle = 2*math.pi/6
        angles = [n*base_angle for n in range(6)]
        ox = [12*math.cos(t) for t in angles]
        oy = [12*math.sin(t) for t in angles]
        for node in self._arena.nodes:
            cr.set_line_width(1.0)
            cr.set_source_rgb(0.5, 0.5, 0.5)
            for neighbour in node.neighbours:
                cr.move_to(node.x, node.y)
                cr.line_to(neighbour.x, neighbour.y)
                cr.stroke()
            cr.set_line_width(3)
            cr.set_source_rgb(0., 0., 1.0)
                        
