from .graph_arena_view import GraphArenaView
from .square_arena_view import SquareArenaView

class ArenaViewFactory:
    @classmethod
    def make_arena_view(cls, arena):
        shape = arena.shape
        if shape == "square":
            return SquareArenaView(arena)
        elif shape == "hexagonal":
            return GraphArenaView(arena)
        elif shape == "graph":
            return GraphArenaView(Arena)
        else:
            raise ValueError("shape not recognised")
