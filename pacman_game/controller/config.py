## Represent the `configuration' of a game session (maze shape, difficulty, etc).
class Config:

    ## Create a new Config.
    #
    # @param difficulty:String The difficulty of the game.
    # @param shape The shape of the maze.
    # @param size The size of the maze.
    def __init__(self, difficulty, shape, size):
        self.difficulty = difficulty
        self.shape = shape
        self.size = size
        self.over = False
        self.power_state = False
        self.chase_duration = 5.0
        self.scatter_duration = 20.0
        self.frighten_duration = 7.0
        if difficulty == "easy":
            self._chase_duration_multiplier = 1.01
            self._scatter_duration_multiplier = 0.99
            self._frighten_duration_multiplier = 0.99
        elif difficulty == "medium":
            self._chase_duration_multiplier = 1.05
            self._scatter_duration_multiplier = 0.95
            self._frighten_duration_multiplier = 0.95
        elif difficulty == "hard":
            self._chase_duration_multiplier = 1.1
            self._scatter_duration_multiplier = 0.9
            self._frighten_duration_multiplier = 0.9

    ## The difficulty of this configuration.
    #
    # @return The difficulty of this configuration.
    @property
    def difficulty(self):
        return self._difficulty

    ## Set the difficulty of this configuration
    #
    # @param difficulty The difficulty.
    @difficulty.setter
    def difficulty(self, difficulty):
        self._difficulty = difficulty

    ## The shape of this configuration.
    #
    # @return The shape of this configuration.
    @property
    def shape(self):
        return self._shape

    ## Set the shape of this configuration.
    #
    # @param shape The shape.
    @shape.setter
    def shape(self, shape):
        self._shape = shape

    ## The size of this configuration
    #
    # @return The size of this configuration.
    @property
    def size(self):
        return self._size

    ## Set the size of this configuration.
    #
    # @param size The size.
    @size.setter
    def size(self, size):
        self._size = size

    ## The length of time the ghosts should spend chasing the avatar.
    #
    # @return The length of time the ghosts should spend chasing the avatar.
    @property
    def chase_duration(self):
        return self._chase_duration

    ## Set the length of time the ghosts should spend chasing the avatar.
    #
    # @param duration The duration.
    @chase_duration.setter
    def chase_duration(self, duration):
        self._chase_duration = duration

    ## The length of time the ghosts should spend wandering the maze.
    #
    # @return The length of time the ghosts should spend wandering the maze.
    @property
    def scatter_duration(self):
        return self._scatter_duration

    ## Set the length of time the ghosts should spend wandering.
    #
    # @param duration The duration.
    @scatter_duration.setter
    def scatter_duration(self, duration):
        self._scatter_duration = duration

    ## The length of time the ghosts should be frightened when the Avatar
    ## consumes a power pill.
    #
    # @return The length of time the ghosts should be frightened.
    @property
    def frighten_duration(self):
        return self._frighten_duration

    ## Set the length of time the ghosts should be frightened when the Avatar
    ## consumes a power pill.
    #
    # @param duration The duration.
    @frighten_duration.setter
    def frighten_duration(self, duration):
        self._frighten_duration = duration

    ## The time when this level was started. This is used when transitioning to
    ## a new level to see how long this level took.
    #
    # @return The time the current level was started.
    @property
    def start_time(self):
        return self._start_time

    ## Set the time when this level was started. This should be set when
    ## starting a new level.
    #
    # @param start_time The start time.
    @start_time.setter
    def start_time(self, start_time):
        self._start_time = start_time

    ## The state of the game. Is it over, or is it still in play?
    #
    # @return True if the game is over, False otherwise.
    @property
    def over(self):
        return self._over

    ## Set the state of the game; i.e., if the game is over or still in play.
    #
    # @param over True if the game is over.
    @over.setter
    def over(self, over):
        self._over = over

    ## Get the current behaviour of the ghosts.
    #
    # @return The current behaviour of the ghosts. Should be only
    # "scatter", "chase" or "frighten".
    @property
    def current_ghost_behaviour(self):
        return self._current_ghost_behaviour

    ## Set the current behaviour of the ghosts.
    #
    # @param behaviour The behaviour of the ghosts. Should only be "scatter",
    # "chase" or "frighten".
    @current_ghost_behaviour.setter
    def current_ghost_behaviour(self, behaviour):
        self._current_ghost_behaviour = behaviour

    ## Get the time at which the ghosts started their current behaviour.
    #
    # @return The time the ghosts started their current behaviour.
    @property
    def ghost_behaviour_start_time(self):
        return self._ghost_behaviour_start_time

    ## Set the time at which the ghosts started their current behaviour. This
    ## should be used when the ghosts change behaviour.
    #
    # @param time The time at which the behaviour started.
    @ghost_behaviour_start_time.setter
    def ghost_behaviour_start_time(self, time):
        self._ghost_behaviour_start_time = time

    ## Get the duration length of the ghosts' current behaviour.
    #
    # @return The duration length of the ghosts' current behaviour.
    @property
    def ghost_behaviour_duration(self):
        return self._ghost_behaviour_duration

    ## Set the duration length of the ghosts' current behaviour.
    #
    # @param duration The duration.
    @ghost_behaviour_duration.setter
    def ghost_behaviour_duration(self, duration):
        self._ghost_behaviour_duration = duration

    ## Get the power state; i.e., if the Avatar has consumed a power pill and
    ## can consume the ghosts. This effect should wear of after some time,
    ## as dictated by the ghosts' "frighten" duration.
    #
    # @return True if the Avatar is in the power state and can consume ghosts.
    @property
    def power_state(self):
        return self._power_state

    ## Set the power state; i.e., if the Avatar has consumed a power pill and
    ## can consume the ghosts.
    #
    # @param power_state True if the Avatar is in the power state.
    @power_state.setter
    def power_state(self, power_state):
        self._power_state = power_state

    ## Get the multiplier for the chase duration; i.e., by how much the
    ## chase duration should change upon transitioning to a new level.
    #
    # @return The chase duration multiplier.
    @property
    def chase_duration_multiplier(self):
        return self._chase_duration_multiplier

    ## Get the multiplier for the scatter duration; i.e., by how much the
    ## scatter duration should change upon transitioning to a new level.
    #
    # @return The scatter duration mulitiplier.
    @property
    def scatter_duration_multiplier(self):
        return self._scatter_duration_multiplier

    ## Get the multiplier for the frighten duration; i.e., by how much the
    ## frighten duration should change upon transitioning to a new level.
    #
    # @return The frighten duration multiplier.
    @property
    def frighten_duration_multiplier(self):
        return self._frighten_duration_multiplier
