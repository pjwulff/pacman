import threading
import time
from .avatar_controller import AvatarController
from .config import Config
from .ghost_controller import GhostController
from ..model.world import World

class GameController:
    def __init__(self, config, world):
        self._config = config
        self._world = world
        self._avatar_controller = AvatarController(world.avatar)
        ghosts = world.ghosts
        self._ghost_controllers = {
            "blinky": GhostController(ghosts["blinky"], config.difficulty),
            "clyde": GhostController(ghosts["clyde"], config.difficulty),
            "inky": GhostController(ghosts["inky"], config.difficulty),
            "pinky": GhostController(ghosts["pinky"], config.difficulty),
        }
        self._reset(time.monotonic())
        self._quit = False
        self._thread = threading.Thread(target = self.step)
        self._thread.start()
    
    @property
    def over(self):
        return self._config.over

    @property
    def world(self):
        return self._world

    @property
    def config(self):
        return self._config

    def step(self):
        while True:
            current_time = time.monotonic()
            delta = current_time - self._current_time
            self._current_time = current_time

            if len(self.world.dots) == 0:
                self._win(current_time)
                time.sleep(2.0)
                continue
            self._update_ghosts(delta)
            self._avatar_controller.step(delta)

            self._eat_dots()
            self._eat_powers()
            self._check_ghost_hit()
            if self.config.over or self._quit:
                break
            time.sleep(1.0/300.)

    def _update_ghosts(self, delta):
        avatar = self.world.avatar
        ghosts = self.world.ghosts
        for ghost in self._ghost_controllers:
            self._ghost_controllers[ghost].update_target(avatar, ghosts)
            self._ghost_controllers[ghost].step(delta)
        self._update_ghost_behaviour()

    def _update_ghost_behaviour(self):
        current_time = time.monotonic()
        duration = current_time - self.config.ghost_behaviour_start_time
        if duration > self.config.ghost_behaviour_duration:
            if self.config.current_ghost_behaviour == "scatter":
                next_ghost_behaviour = "chase"
                self.config.current_ghost_behaviour = "chase"
                self.config.ghost_behaviour_duration = self.config.chase_duration
            else:
                next_ghost_behaviour = "scatter"
                self.config.current_ghost_behaviour = "scatter"
                self.config.ghost_behaviour_duration = self.config.scatter_duration
            for ghost in self.world.ghosts:
                self.world.ghosts[ghost].mode = next_ghost_behaviour
            self.config.power_state = False
            self.config.ghost_behaviour_start_time = current_time

    def _eat_dots(self):
        for dot in self.world.dots:
            if dot.collide(self.world.avatar):
                self._eat_dot(dot)
                self.world.dots.remove(dot)

    def _eat_dot(self, dot):
        self.world.score += 10

    def _eat_powers(self):
        for power in self.world.powers:
            if power.collide(self.world.avatar):
                self._eat_power()
                self.world.powers.remove(power)

    def _eat_power(self):
        self.config.power_state = True
        self.config.ghost_behaviour_start_time = time.monotonic()
        self.config.ghost_behaviour_duration = self.config.frighten_duration
        for ghost in self.world.ghosts:
            self.world.ghosts[ghost].mode = "frighten"
        self.world.score += 20

    def _check_ghost_hit(self):
        for ghost in self.world.ghosts:
            ghost_ = self.world.ghosts[ghost]
            if ghost_.alive and ghost_.collide(self.world.avatar):
                if self.config.power_state:
                    self._eat_ghost(ghost)
                else:
                    self._lose_life()

    def _eat_ghost(self, ghost):
        self._ghost_controllers[ghost].kill()
        self.world.score += 50

    def _lose_life(self):
        if self.world.lives == 0:
            self._lose()
        else:
            self.world.lives -= 1
            self.world.avatar.return_to_spawn()
            for ghost in self.world.ghosts:
                self.world.ghosts[ghost].return_to_spawn()

    def stop(self):
        self.config.over = True
        self._thread.join()

    def quit(self):
        self.config.over = True
        self._thread.join()

    def _lose(self):
        self.config.over = True

    def _win(self, time):
        self._increase_difficulty()
        self.world.level += 1
        bonus = 500 - (time - self.config.start_time)
        bonus *= self.world.level
        if bonus > 0:
            self.world.score += 10 * int(bonus/10.)
        self._reset(time)
    
    def _reset(self, time):
        self._current_time = time
        self.config.start_time = time
        self.config.ghost_behaviour_start_time = time
        self.config.current_ghost_behaviour = "scatter"
        self.config.ghost_behaviour_duration = self.config.scatter_duration
        self.world.arena.generate()
        self._avatar_controller.return_to_spawn()
        for ghost in self._ghost_controllers:
            self._ghost_controllers[ghost].reset()
        self.config.power_state = False
    
    def _increase_difficulty(self):
        for ghost in self._ghost_controllers:
            self._ghost_controllers[ghost].increase_difficulty()
        self.config.chase_duration *= self.config.chase_duration_multiplier
        self.config.scatter_duration *= self.config.scatter_duration_multiplier
        self.config.frighten_duration *= self.config.frighten_duration_multiplier
    
    def set_direction(self, direction):
        self._avatar_controller.set_direction(direction)

class GameControllerFactory:
    @classmethod
    def make_controller(cls,
                        difficulty = "easy",
                        shape = "square",
                        size="small"):
        config = Config(difficulty, shape, size)
        world = World(size, shape)
        return GameController(config, world)
