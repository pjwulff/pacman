class Config:
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

    @property
    def difficulty(self):
        return self._difficulty

    @difficulty.setter
    def difficulty(self, difficulty):
        self._difficulty = difficulty

    @property
    def shape(self):
        return self._shape

    @shape.setter
    def shape(self, shape):
        self._shape = shape

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size

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
    def chase_duration_multiplier(self):
        return self._chase_duration_multiplier

    @property
    def scatter_duration_multiplier(self):
        return self._scatter_duration_multiplier

    @property
    def frighten_duration_multiplier(self):
        return self._frighten_duration_multiplier
