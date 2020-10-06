import sys
import time
from .arena_factory import ArenaFactory
from .avatar import Avatar
from .blinky import Blinky
from .pinky import Pinky
from .inky import Inky
from .clyde import Clyde

## A composite object that encapsulates everything about the current state
## of the `world' of a running game.
class World:
    ## Create a new World object.
    #
    # @param size The size of the Arena. Should only be "small", "medium"
    # or "large".
    # @param shape The shape of the Arena.
    def __init__(self, size, shape):
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

    ## Get the number of lives left.
    #
    # @return The number of remaining lives.
    @property
    def lives(self):
        return self._lives

    ## Set the number of lives.
    #
    # @param lives The number of lives.
    @lives.setter
    def lives(self, lives):
        self._lives = lives

    ## Get the current score.
    #
    # @return The current score.
    @property
    def score(self):
        return self._score

    ## Set the current score.
    #
    # @param score The score.
    @score.setter
    def score(self, score):
        self._score = score

    ## Get the current level number.
    #
    # @return The current level number.
    @property
    def level(self):
        return self._level

    ## Set the current level number.
    #
    # @param level The level numer.
    @level.setter
    def level(self, level):
        self._level = level

    ## Get the Avatar in this game world.
    #
    # @return An Avatar object.
    @property
    def avatar(self):
        return self._avatar

    ## Get the Ghosts in this game world.
    #
    # @return A dictionary of ghosts.
    @property
    def ghosts(self):
        return self._ghosts

    ## Get the dots in this game world.
    #
    # @return A list of dots.
    @property
    def dots(self):
        return self._arena.dots

    ## Get the power pills in this game world.
    #
    # @return A list of power pills.
    @property
    def powers(self):
        return self._arena.powers

    ## Get the Arena object of this game world.
    #
    # @return An Arena object.
    @property
    def arena(self):
        return self._arena
