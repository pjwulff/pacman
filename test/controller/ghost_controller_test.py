import unittest
from pacman_game.controller import ghost_controller

class MockGhost:
    def return_to_spawn(self):
        pass

class GhostControllerTestCase(unittest.TestCase):
    def setUp(self):
        self.g = MockGhost()
        self.gc = ghost_controller.GhostController(self.g, "easy")

    def test_reset(self):
        self.gc.reset()
        assert(self.g.alive == True)
        assert(self.g.mode == "scatter")

    def test_kill(self):
        self.gc.kill()
        assert(self.g.alive == False)

ghost_controller_tests = unittest.makeSuite(GhostControllerTestCase, "test")
