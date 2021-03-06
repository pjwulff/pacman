from ..model.angle import *
from .arena_view import ArenaView

## Concrete class of type ArenaView for drawing SquareArenas.
class SquareArenaView(ArenaView):

    ## Create a new SquareArenaView.
    #
    # @param arena The arena to be viewed.
    def __init__(self, arena):
        rect = arena.rect
        super().__init__(arena, rect.width + 24, rect.height + 24)

    ## Draw the arena.
    #
    # @param cr The cairo context to be used for drawing.
    def draw(self, cr):
        super().draw(cr)
        cr.translate(12, 12)
        width = self._arena.logical_width
        height = self._arena.logical_height
        for node in self._arena.nodes:
            for neighbour in node.geoneighbours:
                if neighbour not in node.neighbours:
                    angle = node.direction(neighbour)
                    perp = normalise(angle + math.pi/2.0)
                    ox = 12 * math.cos(angle)
                    oy = 12 * math.sin(angle)
                    px = 12 * math.cos(perp)
                    py = 12 * math.sin(perp)
                    cr.move_to(node.x+ox+px, node.y-oy-py)
                    cr.line_to(node.x+ox-px, node.y-oy+py)
                    cr.stroke()
