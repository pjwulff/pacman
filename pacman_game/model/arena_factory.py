from .graph_arena import GraphArena
from .hexagonal_arena import HexagonalArena
from .square_arena import SquareArena

class ArenaFactory:
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
