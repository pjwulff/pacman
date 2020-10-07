import unittest
from pacman_game.controller import config

class ConfigTestCase(unittest.TestCase):
    def setUp(self):
        self.c = config.Config("easy", "square", "small")

    def test_difficulty(self):
        c = config.Config("easy", "square", "small")
        assert(c.difficulty == "easy")
        c = config.Config("medium", "square", "small")
        assert(c.difficulty == "medium")
        c = config.Config("hard", "square", "small")
        assert(c.difficulty == "hard")

    def test_shape(self):
        c = config.Config("easy", "square", "small")
        assert(c.shape == "square")
        c = config.Config("easy", "hexagonal", "small")
        assert(c.shape == "hexagonal")
        c = config.Config("easy", "graph", "small")
        assert(c.shape == "graph")

    def test_size(self):
        c = config.Config("easy", "square", "small")
        assert(c.size == "small")
        c = config.Config("easy", "square", "medium")
        assert(c.size == "medium")
        c = config.Config("easy", "square", "large")
        assert(c.size == "large")

    def test_chase_duration_set(self):
        self.c.chase_duration = 1000.
        assert(self.c.chase_duration == 1000.)

    def test_scatter_duration_set(self):
        self.c.scatter_duration = 1000.
        assert(self.c.scatter_duration == 1000.)

    def test_frighten_duration_set(self):
        self.c.frighten_duration = 1000.
        assert(self.c.frighten_duration == 1000.)

    def test_start_time_set(self):
        self.c.start_time = 1.
        assert(self.c.start_time == 1.)

    def test_over(self):
        assert(self.c.over == False)

    def test_over_set(self):
        self.c.over = True
        assert(self.c.over == True)

    def test_current_ghost_behaviour_set(self):
        self.c.current_ghost_behaviour = "frighten"
        assert(self.c.current_ghost_behaviour == "frighten")

    def test_ghost_behaviour_start_time_set(self):
        self.c.ghost_behaviour_start_time = 1.
        assert(self.c.ghost_behaviour_start_time == 1.)

    def test_ghost_behaviour_duration_set(self):
        self.c.ghost_behaviour_duration = 1.
        assert(self.c.ghost_behaviour_duration == 1.)

    def test_power_state(self):
        assert(self.c.power_state == False)

    def test_power_state_set(self):
        self.c.power_state = True
        assert(self.c.power_state == True)

config_tests = unittest.makeSuite(ConfigTestCase, "test")
