from .graph_arena import GraphArena
from .hexagonal_arena import HexagonalArena
from .square_arena import SquareArena

## A factory class to abstract the details of creating an Arena.
class ArenaFactory:

    ## Create an Arena based on a certain shape, width and height.
    #
    # @param shape The shape of the Arena. Should be only "square",
    # "hexagonal" or "graph".
    # @param width The width of the Arena in terms of number of nodes.
    # @param height The height of the Arena in terms of number of nodes.
    #
    # @return An object a subclass of the abstract class `Arena'.
    @classmethod
    def make_arena(cls, shape, width, height):
        if shape == "square":
            return SquareArena(width, height)
        elif shape == "hexagonal":
            return HexagonalArena(width, height)
        elif shape == "graph":
            return GraphArena(width, height)
        else:
            raise ValueError(f"shape \"{shape}\" not recognised")
