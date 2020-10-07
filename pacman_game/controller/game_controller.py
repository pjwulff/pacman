import threading
import time
from .avatar_controller import AvatarController
from .config import Config
from .ghost_controller import GhostController
from ..model.world import World

## The overall controller for the game. This class implements much of the
## game logic, but also delegates tasks to sub-controllers which this
## class creates.
class GameController:

    ## Create a new GameController
    #
    # @param config The game configuration.
    # @param world The game world.
    def __init__(self, config, world, next):
        self._config = config
        self._world = world
        self._next = next
        self._avatar_controller = AvatarController(world.avatar)
        ghosts = world.ghosts
        self._ghost_controllers = {
            "blinky": GhostController(ghosts["blinky"], config.difficulty),
            "clyde": GhostController(ghosts["clyde"], config.difficulty),
            "inky": GhostController(ghosts["inky"], config.difficulty),
            "pinky": GhostController(ghosts["pinky"], config.difficulty),
        }
        self._reset(time.monotonic())
        self._thread = threading.Thread(target = self._run)
        self._thread.start()

    ## Get the `world' that this controller controls.
    #
    # @return The world associated with this controller.
    @property
    def world(self):
        return self._world

    ## Get the `config' for this controller.
    #
    # @return The config associated with this controller.
    @property
    def config(self):
        return self._config

    ## Run the game. This is run in a separate thread and runs in a loop
    ## until the game is `over'.
    def _run(self):
        while True:
            current_time = time.monotonic()
            delta = current_time - self._current_time
            self._current_time = current_time

            if self._level_over():
                self._win(current_time)
                time.sleep(2.0)
                continue
            self._update_ghosts(delta)
            self._avatar_controller.step(delta)

            self._eat_dots()
            self._eat_powers()
            self._check_ghost_hit()
            if self.config.over:
                break
            time.sleep(1.0/300.)

    ## Returns whether or not this level is over; i.e., if all the dots
    ## and powers have been consumed.
    #
    # @return True if the level is over.
    def _level_over(self):
        return len(self.world.dots) == 0 and \
               len(self.world.powers) == 0

    ## Update the ghosts over a particular duration of time.
    #
    # @param delta The length of time this `frame' lasts.
    def _update_ghosts(self, delta):
        avatar = self.world.avatar
        ghosts = self.world.ghosts
        for ghost in self._ghost_controllers:
            self._ghost_controllers[ghost].update_target(avatar, ghosts)
            self._ghost_controllers[ghost].step(delta)
        self._update_ghost_behaviour()

    ## Update the ghosts behaviour. This function checks if the ghosts should
    ## change their behaviour if they have been in their current behaviour
    ## long enough, as dictated by the configs "duration" properties.
    def _update_ghost_behaviour(self):
        current_time = time.monotonic()
        duration = current_time - self.config.ghost_behaviour_start_time
        if duration > self.config.ghost_behaviour_duration:
            if self.config.current_ghost_behaviour == "scatter":
                next_ghost_behaviour = "chase"
                self.config.current_ghost_behaviour = "chase"
                self.config.ghost_behaviour_duration = \
                    self.config.chase_duration
            else:
                next_ghost_behaviour = "scatter"
                self.config.current_ghost_behaviour = "scatter"
                self.config.ghost_behaviour_duration = \
                    self.config.scatter_duration
            for ghost in self.world.ghosts:
                self.world.ghosts[ghost].mode = next_ghost_behaviour
            self.config.power_state = False
            self.config.ghost_behaviour_start_time = current_time

    ## Checks if the Avatar is colliding with any dots, and `eats' them.
    def _eat_dots(self):
        for dot in self.world.dots:
            if dot.collide(self.world.avatar):
                self._eat_dot(dot)

    ## Eat a single dot. This should increase the score and remove it from
    ## the game world.
    #
    # @param dot The dot to be eaten.
    def _eat_dot(self, dot):
        self.world.score += 10
        self.world.dots.remove(dot)

    ## Checks if the Avatar is colliding with and power pills, and `eats' them.
    def _eat_powers(self):
        for power in self.world.powers:
            if power.collide(self.world.avatar):
                self._eat_power(power)

    ## Eat a single power pill. This should increase the score, remove it from
    ## the game world, change the ghosts' behaviour to "frighten" and put the
    ## game in the `power' state (i.e., make it so the Avatar can temporarily
    ## consume the ghosts).
    #
    # @param power The power pill to be eaten.
    def _eat_power(self, power):
        self.config.power_state = True
        self.config.ghost_behaviour_start_time = time.monotonic()
        self.config.ghost_behaviour_duration = self.config.frighten_duration
        for ghost in self.world.ghosts:
            self.world.ghosts[ghost].mode = "frighten"
        self.world.score += 20
        self.world.powers.remove(power)

    ## Check if the Avatar is colliding with any ghosts. If so, and the game is
    ## not in the `power' state, this should result in the loss of a life and
    ## possibly a game over. If the game is in the `power' state, the ghost
    ## should be eaten.
    def _check_ghost_hit(self):
        for ghost in self.world.ghosts:
            ghost_ = self.world.ghosts[ghost]
            if ghost_.alive and ghost_.collide(self.world.avatar):
                if self.config.power_state:
                    self._eat_ghost(ghost)
                else:
                    self._lose_life()

    ## Eat a ghost. This should `kill' the ghost (even though they're already
    ## dead) and increase the score.
    def _eat_ghost(self, ghost):
        self._ghost_controllers[ghost].kill()
        self.world.score += 50

    ## Decrement the life counter. If there are no lives remaining, this should
    ## result in a game over.
    def _lose_life(self):
        if self.world.lives == 0:
            self._lose()
        else:
            self.world.lives -= 1
            self.world.avatar.return_to_spawn()
            for ghost in self.world.ghosts:
                self.world.ghosts[ghost].return_to_spawn()

    ## Stop the game. This will set the game to `over' and calls `join' on the
    ## main game thread.
    def _stop(self):
        self.config.over = True
        self._next(self.world.score, self.config.difficulty,
                   self.config.shape, self.config.size)

    ## Quit the game early.
    def quit(self):
        self.config.over = True
        self._thread.join()
        self._next(None, self.config.difficulty,
                   self.config.shape, self.config.size)

    ## Stops the game because the player lost (i.e., all lives were lost).
    def _lose(self):
        self._stop()

    ## Indicate that the player has `won' (in other words, beaten this level).
    ## This moves to a new level, resets the game, and increases the difficulty.
    def _win(self, time):
        self._increase_difficulty()
        self.world.level += 1
        bonus = 500 - (time - self.config.start_time)
        bonus *= self.world.level
        if bonus > 0:
            self.world.score += 10 * int(bonus/10.)
        self._reset(time)
    
    ## Reset the game world. This is called if the player loses a life, or
    ## beats the game and progresses to a new level. This function will generate
    ## a new maze, reset the ghosts' positions and behaviours, and return the
    ## Avatar to its spawn location.
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
    
    ## Increase the difficulty of the game. This function is called when the
    ## game progresses to a new level. When this happens, the length of time
    ## the ghosts spend in different behaviours is changed according to the
    ## `multipliers' in the config (which in turn are dictated by the
    ## difficulty). Additionally, the ghosts will become faster.
    def _increase_difficulty(self):
        for ghost in self._ghost_controllers:
            self._ghost_controllers[ghost].increase_difficulty()
        self.config.chase_duration *= \
            self.config.chase_duration_multiplier
        self.config.scatter_duration *= \
            self.config.scatter_duration_multiplier
        self.config.frighten_duration *= \
            self.config.frighten_duration_multiplier
    
    ## Set the desired direction for the Avatar. This public function is
    ## provided so that the `View' can specify in which direction the user
    ## would like the Avatar to move.
    #
    # @param direction The desired direction, as an angle between [-pi, pi).
    # The GameController knows nothing of input/output, and thus does not know
    # how the user is controlling the Avatar (keyboard, mouse, joystick, etc).
    # An angle is used in order to remain agnostic.
    def set_direction(self, direction):
        self._avatar_controller.target_direction = direction

## A factory class to create a GameController, and also a Config and World
## to go with it.
class GameControllerFactory:

    ## Create a new controller. This takes as input the basic configuration
    ## details of the desired game and sets everything up to be able to
    ## construct a GameController.
    #
    # @param difficulty The desired difficulty. If none is provided, "easy"
    # will be used as a default.
    # @param shape The desired shape of the maze. If none is provided, "square"
    # will be used as a default.
    # @param size The desired size of the maze. If none is provided, "small"
    # will be used as a default.
    @classmethod
    def make_controller(cls,
                        next,
                        difficulty = "easy",
                        shape = "square",
                        size = "small"):
        config = Config(difficulty, shape, size)
        world = World(size, shape)
        return GameController(config, world, next)
