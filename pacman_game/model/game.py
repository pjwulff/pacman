import sys, time
from .arena import Arena
from .avatar import Avatar
from .blinky import Blinky
from .pinky import Pinky
from .inky import Inky
from .clyde import Clyde

class GameState:
    def __init__(self):
        """! Construct a new GameState object."""
        self.lives = 3
        self.score = 0
        self._arena = Arena()
        self._avatar = Avatar(self._arena)
        self._ghosts = {
            "blinky": Blinky(self._arena),
            "pinky": Pinky(self._arena),
            "inky": Inky(self._arena),
            "clyde": Clyde(self._arena),
        }
        self._dots = self._arena.dots()
        self._powers = self._arena.powers()
        self._chase_duration = 5.0
        self._scatter_duration = 20.0
        self._frighten_duration = 7.0
        self.current_ghost_behaviour = "scatter"
        self.ghost_behaviour_duration = self._scatter_duration
        self.power_state = False
        self.over = False
        self.ghost_behaviour_start_time = time.monotonic()
        self._start_time = time.monotonic()
    
    @property
    def chase_duration(self):
        return self._chase_duration
    
    @property
    def scatter_duration(self):
        return self._scatter_duration
    
    @property
    def frighten_duration(self):
        return self._frighten_duration
    
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
        return self._dots

    @property
    def powers(self):
        return self._powers

    @property
    def arena(self):
        """! Get the arena associated with this game state.

        @returns The arena object associated with this game state."""
        return self._arena

    @property
    def score(self):
        """! Get the current score.

        @returns The score."""
        return self._score
    
    @score.setter
    def score(self, score):
        self._score = score
