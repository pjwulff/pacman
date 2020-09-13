import time
from .avatar_controller import AvatarController
from .blinky_controller import BlinkyController
from ..model.game import GameState

class InternalController:
    def __init__(self, state):
        self._state = state
        self._avatar_controller = AvatarController(state.avatar)
        ghosts = state.ghosts
        self._ghost_controllers = {
            "blinky": BlinkyController(ghosts["blinky"]),
            "clyde": BlinkyController(ghosts["clyde"]),
            "inky": BlinkyController(ghosts["inky"]),
            "pinky": BlinkyController(ghosts["pinky"]),
        }
        self._current_time = time.monotonic()
    
    @property
    def state(self):
        return self._state

    def step(self):
        current_time = time.monotonic()
        delta = current_time - self._current_time
        self._current_time = current_time
        
        if len(self.state.dots) == 0:
            self._win(current_time)
        self._update_ghosts(delta)
        self._avatar_controller.step(delta)

        self._eat_dots()
        self._eat_powers()
        self._check_ghost_hit()
        if self.state.over:
            return False
        return True
    
    def _update_ghosts(self, delta):
        for ghost in self._ghost_controllers:
            self._ghost_controllers[ghost].step(delta)
        self._update_ghost_behaviour()

    def _update_ghost_behaviour(self):
        current_time = time.monotonic()
        duration = current_time - self.state.ghost_behaviour_start_time
        if duration > self.state.ghost_behaviour_duration:
            if self.state.current_ghost_behaviour == "scatter":
                next_ghost_behaviour = "chase"
                self.state.current_ghost_behaviour = "chase"
                self.state.ghost_behaviour_duration = self.state.chase_duration
            elif self.state.current_ghost_behaviour == "chase":
                next_ghost_behaviour = "scatter"
                self.state.current_ghost_behaviour = "scatter"
                self.state.ghost_behaviour_duration = self.state.scatter_duration
            for ghost in self.state.ghosts:
                self.state.ghosts[ghost].mode = next_ghost_behaviour
            self.state.power_state = False
            self.state.ghost_behaviour_start_time = current_time

    def _eat_dots(self):
        for dot in self.state.dots:
            if dot.collide(self.state.avatar):
                self._eat_dot(dot)
                self.state.dots.remove(dot)

    def _eat_dot(self, dot):
        self.state.score += 10

    def _eat_powers(self):
        for power in self.state.powers:
            if power.collide(self.state.avatar):
                self._eat_power()
                self.state.powers.remove(power)

    def _eat_power(self):
        self.state.power_state = True
        self.state.ghost_behaviour_start_time = time.monotonic()
        self.state.ghost_behaviour_duration = self.state.frighten_duration
        for ghost in self.state.ghosts:
            self.state.ghosts[ghost].mode = "frighten"
        self.state.score += 20

    def _check_ghost_hit(self):
        for ghost in self.state.ghosts:
            ghost_ = self.state.ghosts[ghost]
            if ghost_.alive and ghost_.collide(self.state.avatar):
                if self.state.power_state:
                    self._eat_ghost(ghost)
                else:
                    self._lose_life()

    def _eat_ghost(self, ghost):
        self._ghost_controllers[ghost].kill()
        self.state.score += 50

    def _lose_life(self):
        if self.state.lives == 0:
            self._lose()
        else:
            self.state.score -= 100
            self.state.lives -= 1
            self.state.avatar.return_to_spawn()
            for ghost in self.state.ghosts:
                self.state.ghosts[ghost].return_to_spawn()

    def _lose(self):
        self.state.over = True
        self.state.condition = "lose"

    def _win(self, time):
        self.state.over = True
        self.state.condition = "win"
        bonus = 500 - (time - self.state.start_time)
        if bonus > 0:
            self.state.score += bonus
    
    def add_direction(self, direction):
        self._avatar_controller.add_direction(direction)
    
    def remove_direction(self, direction):
        self._avatar_controller.remove_direction(direction)


class GameController:
    def __init__(self):
        pass
    
    def start_game(self):
        state = GameState()
        return InternalController(state)
