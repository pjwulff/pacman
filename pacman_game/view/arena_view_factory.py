from .graph_arena_view import GraphArenaView
from .square_arena_view import SquareArenaView

## A factory class to return a concrete ArenaView.
class ArenaViewFactory:

    ## Create a new ArenaView for the given Arena.
    #
    # @param arena The Arena object to view.
    #
    # @return An ArenaView object.
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
            raise ValueError(f"shape {shape} not recognised")
