import sys, time
from .square_arena import SquareArena
from .graph_arena import GraphArena
from .hexagonal_arena import HexagonalArena
from .avatar import Avatar
from .blinky import Blinky
from .pinky import Pinky
from .inky import Inky
from .clyde import Clyde
from .rect import Rect

class GameState:
    def __init__(self, difficulty, shape):
        """! Construct a new GameState object."""
        self.difficulty = difficulty
        self.shape = shape
        self.lives = 3
        self.score = 0
        self.level = 1
        if shape == "square":
            self._arena = SquareArena(13, 8)
        elif shape == "hexagonal":
            self._arena = HexagonalArena(13, 8)
        elif shape == "graph":
            self._arena = GraphArena(13, 8)
        self._avatar = Avatar(self._arena)
        self._ghosts = {
            "blinky": Blinky(self._arena),
            "pinky": Pinky(self._arena),
            "inky": Inky(self._arena),
            "clyde": Clyde(self._arena),
        }
        self.power_state = False
        self.over = False
    
    @property
    def start_time(self):
        return self._start_time
    
    @start_time.setter
    def start_time(self, start_time):
        self._start_time = start_time
    
    @property
    def level(self):
        return self._level
    
    @level.setter
    def level(self, level):
        self._level = level
    
    @property
    def chase_duration(self):
        return self._chase_duration
    
    @chase_duration.setter
    def chase_duration(self, duration):
        self._chase_duration = duration
    
    @property
    def scatter_duration(self):
        return self._scatter_duration
    
    @scatter_duration.setter
    def scatter_duration(self, duration):
        self._scatter_duration = duration
    
    @property
    def frighten_duration(self):
        return self._frighten_duration
    
    @frighten_duration.setter
    def frighten_duration(self, duration):
        self._frighten_duration = duration
    
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        self._start_time = start_time

    @property
    def lives(self):
        return self._lives
    
    @lives.setter
    def lives(self, lives):
        self._lives = lives
    
    @property
    def condition(self):
        return self._condition
    
    @condition.setter
    def condition(self, condition):
        self._condition = condition
    
    @property
    def over(self):
        return self._over
    
    @over.setter
    def over(self, over):
        self._over = over
    
    @property
    def current_ghost_behaviour(self):
        return self._current_ghost_behaviour
    
    @current_ghost_behaviour.setter
    def current_ghost_behaviour(self, behaviour):
        self._current_ghost_behaviour = behaviour
    
    @property
    def ghost_behaviour_start_time(self):
        return self._ghost_behaviour_start_time
    
    @ghost_behaviour_start_time.setter
    def ghost_behaviour_start_time(self, time):
        self._ghost_behaviour_start_time = time
    
    @property
    def ghost_behaviour_duration(self):
        return self._ghost_behaviour_duration
    
    @ghost_behaviour_duration.setter
    def ghost_behaviour_duration(self, duration):
        self._ghost_behaviour_duration = duration

    @property
    def power_state(self):
        return self._power_state
    
    @power_state.setter
    def power_state(self, power_state):
        self._power_state = power_state

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
    def score(self):
        """! Get the current score.

        @returns The score."""
        return self._score
    
    @score.setter
    def score(self, score):
        self._score = score
