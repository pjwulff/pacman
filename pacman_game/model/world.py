import sys
import time
from .arena_factory import ArenaFactory
from .avatar import Avatar
from .blinky import Blinky
from .pinky import Pinky
from .inky import Inky
from .clyde import Clyde

class World:
    def __init__(self, size, shape):
        """! Construct a new World object."""
        self.lives = 3
        self.score = 0
        self.level = 1
        width = 0
        height = 0
        if size == "small":
            width = 8
            height = 5
        elif size == "medium":
            width = 13
            height = 8
        elif size == "large":
            width = 21
            height = 13
        else:
            raise ValueError(f"size \"{size}\" not recognised")
        self._arena = ArenaFactory.make_arena(shape, width, height)
        self._avatar = Avatar(self._arena)
        self._ghosts = {
            "blinky": Blinky(self._arena),
            "pinky": Pinky(self._arena),
            "inky": Inky(self._arena),
            "clyde": Clyde(self._arena),
        }

    @property
    def lives(self):
        return self._lives

    @lives.setter
    def lives(self, lives):
        self._lives = lives

    @property
    def score(self):
        """! Get the current score.

        @returns The score."""
        return self._score

    @score.setter
    def score(self, score):
        self._score = score

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, level):
        self._level = level

    @property
    def avatar(self):
        return self._avatar

    @property
    def ghosts(self):
        return self._ghosts

    @property
    def dots(self):
        return self._arena.dots

    @property
    def powers(self):
        return self._arena.powers

    @property
    def arena(self):
        """! Get the arena associated with this game state.

        @returns The arena object associated with this game state."""
        return self._arena

    @arena.setter
    def arena(self, arena):
        self._arena = arena

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size
