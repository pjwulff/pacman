import time
from .arena_controller import ArenaController
from .avatar_controller import AvatarController
from .blinky_controller import BlinkyController
from ..model.game import GameState

class InternalController:
    def __init__(self, state):
        self._state = state
        self._arena_controller = ArenaController(state.arena)
        self._avatar_controller = AvatarController(state.avatar)
        ghosts = state.ghosts
        self._ghost_controllers = {
            "blinky": BlinkyController(ghosts["blinky"], state.difficulty),
            "clyde": BlinkyController(ghosts["clyde"], state.difficulty),
            "inky": BlinkyController(ghosts["inky"], state.difficulty),
            "pinky": BlinkyController(ghosts["pinky"], state.difficulty),
        }
        self._current_time = time.monotonic()
        self.state.start_time = self._current_time
        self.state.chase_duration = 5.0
        self.state.scatter_duration = 20.0
        self.state.frighten_duration = 7.0
        self.state.current_ghost_behaviour = "scatter"
        self.state.ghost_behaviour_duration = self.state.scatter_duration
        self.state.ghost_behaviour_start_time = self._current_time
    
    @property
    def state(self):
        return self._state

    def step(self):
        current_time = time.monotonic()
        delta = current_time - self._current_time
        self._current_time = current_time
        
        if len(self.state.dots) == 0:
            self._win(current_time)
            return True
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
        self._increase_difficulty()
        self.state.level += 1
        bonus = 500 - (time - self.state.start_time)
        bonus *= self.state.level
        if bonus > 0:
            self.state.score += int(bonus)
        self.state.start_time = time
        self._arena_controller.reset()
        self._avatar_controller.return_to_spawn()
        for ghost in self._ghost_controllers:
            self._ghost_controllers[ghost].return_to_spawn()
        self.state.current_ghost_behaviour = "scatter"
        self.state.ghost_behaviour_duration = self.state.scatter_duration
    
    def _increase_difficulty(self):
        for ghost in self._ghost_controllers:
            self._ghost_controllers[ghost].increase_difficulty()
        if self.state.difficulty == "easy":
            self.state.chase_duration *= 1.01
            self.state.scatter_duration *= 0.99
            self.state.frighten_duration *= 0.99
        elif self.state.difficulty == "medium":
            self.state.chase_duration *= 1.05
            self.state.scatter_duration *= 0.95
            self.state.frighten_duration *= 0.95
        elif self.state.difficulty == "hard":
            self.state.chase_duration *= 1.1
            self.state.scatter_duration *= 0.9
            self.state.frighten_duration *= 0.9
    
    def add_direction(self, direction):
        self._avatar_controller.add_direction(direction)
    
    def remove_direction(self, direction):
        self._avatar_controller.remove_direction(direction)


class GameController:
    def __init__(self):
        pass
    
    def start_game(self, difficulty, shape):
        state = GameState(difficulty, shape)
        return InternalController(state)
