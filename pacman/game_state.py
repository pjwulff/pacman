import pygame, sys
from .arena import Arena
from .avatar import Avatar
from .blinky import Blinky
from .pinky import Pinky
from .inky import Inky
from .clyde import Clyde

class GameState:
    """! Represents the state of the running game. This class also handles the
    updating of the state and drawing it to the screen."""
    def __init__(self):
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
        self._chase_duration = 5000
        self._scatter_duration = 20000
        self._frighten_duration = 7000
        self._current_ghost_behaviour = "scatter"
        self._ghost_behaviour_duration = self._scatter_duration
        self._power_state = False

    def arena(self):
        """! Get the arena associated with this game state.

        @returns The arena object associated with this game state."""
        return self._arena

    def start(self):
        """! Performs necessary duties to start a new game."""
        self._ghost_behaviour_start_time = pygame.time.get_ticks()

    def erase(self, screen):
        """! Erase all sprites from the screen.

        @param screen The PyGame screen to draw on."""
        self._avatar.erase(screen)
        for ghost in self._ghosts:
            self._ghosts[ghost].erase(screen)
        for dot in self._dots:
            dot.erase(screen)
        for power in self._powers:
            power.erase(screen)

    def update(self):
        """! Update the game state for a single frame."""
        if len(self._dots) == 0:
            self._win()

        self._update_ghost_behaviour()
        self._avatar.update()
        for ghost in self._ghosts:
            self._ghosts[ghost].update(self._avatar, self._ghosts)

        self._eat_dots()
        self._eat_powers()
        self._check_ghost_hit()

    def draw(self, screen):
        """! Draw all sprites to the screen.

        @param screen The PyGame screen to draw on."""
        for dot in self._dots:
            dot.draw(screen)
        for power in self._powers:
            power.draw(screen)
        for ghost in self._ghosts:
            self._ghosts[ghost].draw(screen)
        self._avatar.draw(screen)
        pygame.display.flip()

    def _eat_dots(self):
        for dot in self._dots:
            if dot.collide(self._avatar):
                self._eat_dot(dot)
                self._dots.remove(dot)

    def _eat_dot(self, dot):
        pass

    def _eat_powers(self):
        for power in self._powers:
            if power.collide(self._avatar):
                self._eat_power()
                self._powers.remove(power)

    def _eat_power(self):
        self._power_state = True
        self._ghost_behaviour_start_time = pygame.time.get_ticks()
        self._ghost_behaviour_duration = self._frighten_duration
        for ghost in self._ghosts:
            self._ghosts[ghost].set_mode("frighten")

    def _check_ghost_hit(self):
        for ghost in self._ghosts:
            ghost_ = self._ghosts[ghost]
            if ghost_.alive() and ghost_.collide(self._avatar):
                if self._power_state:
                    self._eat_ghost(ghost)
                else:
                    self._lose_life()

    def _eat_ghost(self, ghost):
        self._ghosts[ghost].kill()

    def _lose_life(self):
        if self._lives == 0:
            self._lose()
        else:
            self._lives -= 1
            self._avatar.return_to_spawn()
            for ghost in self._ghosts:
                self._ghosts[ghost].return_to_spawn()

    def _lose(self):
        print("You lose!")
        sys.exit()

    def _win(self):
        print("You win!")
        sys.exit()

    def _update_ghost_behaviour(self):
        current_time = pygame.time.get_ticks()
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
