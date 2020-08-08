import pygame
from .arena import Arena
from .avatar import Avatar
from .blinky import Blinky
from .pinky import Pinky
from .inky import Inky
from .clyde import Clyde

class GameState:
    def __init__(self):
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
        return self._arena

    def start(self):
        self._ghost_behaviour_start_time = pygame.time.get_ticks()

    def erase(self, screen):
        self._avatar.erase(screen)
        for ghost in self._ghosts:
            self._ghosts[ghost].erase(screen)
        for dot in self._dots:
            dot.erase(screen)
        for power in self._powers:
            power.erase(screen)

    def update(self):
        if len(self._dots) == 0:
            self.win()
            sys.exit()

        self._update_ghost_behaviour()
        self._avatar.update()
        for ghost in self._ghosts:
            self._ghosts[ghost].update(self._avatar, self._ghosts)

        self._eat_dots()
        self._eat_powers()

    def draw(self, screen):
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
                # self._eat_dot(dot)
                self._dots.remove(dot)

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
            self._ghost_behaviour_start_time = current_time
