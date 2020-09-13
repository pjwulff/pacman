from .arena_view import ArenaView

class SquareArenaView(ArenaView):
    def __init__(self, arena):
        super().__init__(arena)

    def draw(self, cr):
        super().draw(cr)
        width = self._arena.logical_width
        height = self._arena.logical_height
        for i in range(width):
            for j in range(height):
                node = self._arena.nodes[i][j]
                directions = list(node.geoneighbours.keys())
                for direction in directions:
                    neighbour = node.neighbour(direction)
                    if neighbour is None:
                        if direction == "left":
                            cr.move_to(node.x - 12, node.y - 12)
                            cr.line_to(node.x - 12, node.y + 12)
                            cr.stroke()
                        elif direction == "right":
                            cr.move_to(node.x + 12, node.y - 12)
                            cr.line_to(node.x + 12, node.y + 12)
                            cr.stroke()
                        elif direction == "up":
                            cr.move_to(node.x - 12, node.y - 12)
                            cr.line_to(node.x + 12, node.y - 12)
                            cr.stroke()
                        elif direction == "down":
                            cr.move_to(node.x - 12, node.y + 12)
                            cr.line_to(node.x + 12, node.y + 12)
                            cr.stroke()
