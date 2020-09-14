import cairo
import math
from .arena_view import ArenaView

class HexagonalArenaView(ArenaView):
    def __init__(self, arena):
        super().__init__(arena)

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
                        
