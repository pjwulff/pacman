import sys
from .arena import Arena
from .avatar import Avatar
from .blinky import Blinky
from .pinky import Pinky
from .inky import Inky
from .clyde import Clyde

class GameState:
    """! Represents the state of the running game. This class also handles the
    updating of the state."""
    def __init__(self, time):
        """! Construct a new GameState object."""
        self._lives = 3
        self._score = 0
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
        self._current_ghost_behaviour = "scatter"
        self._ghost_behaviour_duration = self._scatter_duration
        self._power_state = False
        self._over = False
        self._ghost_behaviour_start_time = time
        self._start_time = time

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

    def update(self, time, direction):
        """! Update the game state for a single frame."""
        if len(self._dots) == 0:
            self._win(time)

        self._avatar.set_direction(direction)
        self._update_ghost_behaviour(time)
        self._avatar.update()
        for ghost in self._ghosts:
            self._ghosts[ghost].update(self._avatar, self._ghosts)

        self._eat_dots()
        self._eat_powers(time)
        self._check_ghost_hit()

    def _eat_dots(self):
        for dot in self._dots:
            if dot.collide(self._avatar):
                self._eat_dot(dot)
                self._dots.remove(dot)

    def _eat_dot(self, dot):
        self._score += 10

    def _eat_powers(self, time):
        for power in self._powers:
            if power.collide(self._avatar):
                self._eat_power(time)
                self._powers.remove(power)

    def _eat_power(self, time):
        self._power_state = True
        self._ghost_behaviour_start_time = time
        self._ghost_behaviour_duration = self._frighten_duration
        for ghost in self._ghosts:
            self._ghosts[ghost].set_mode("frighten")
        self._score += 20

    def _check_ghost_hit(self):
        for ghost in self._ghosts:
            ghost_ = self._ghosts[ghost]
            if ghost_.alive and ghost_.collide(self._avatar):
                if self._power_state:
                    self._eat_ghost(ghost)
                else:
                    self._lose_life()

    def _eat_ghost(self, ghost):
        self._ghosts[ghost].kill()
        self._score += 50

    def _lose_life(self):
        if self._lives == 0:
            self._lose()
        else:
            self._score -= 100
            self._lives -= 1
            self._avatar.return_to_spawn()
            for ghost in self._ghosts:
                self._ghosts[ghost].return_to_spawn()

    def _lose(self):
        self._over = True
        self._condition = "lose"

    def _win(self, time):
        self._over = True
        self._condition = "win"
        bonus = 500 - (time - self._start_time)
        if bonus > 0:
            self._score += bonus

    @property
    def score(self):
        """! Get the current score.

        @returns The score."""
        return self._score

    @property
    def over(self):
        """! Get the running state of the game.

        @returns True if the game is over, False otherwise."""
        return self._over

    @property
    def condition(self):
        """! Returns the reason why the game is over.

        @returns the string "win" if the player won, "lose" if the player lost."""
        return self._condition

    def _update_ghost_behaviour(self, time):
        current_time = time
        duration = current_time - self._ghost_behaviour_start_time
        if duration > self._ghost_behaviour_duration:
            if self._current_ghost_behaviour == "scatter":
                next_ghost_behaviour = "chase"
                self._current_ghost_behaviour = "chase"
                self._ghost_behaviour_duration = self._chase_duration
            elif self._current_ghost_behaviour == "chase":
                next_ghost_behaviour = "scatter"
                self._current_ghost_behaviour = "scatter"
                self._ghost_behaviour_duration = self._scatter_duration
            for ghost in self._ghosts:
                self._ghosts[ghost].set_mode(next_ghost_behaviour)
            self._power_state = False
            self._ghost_behaviour_start_time = current_time
