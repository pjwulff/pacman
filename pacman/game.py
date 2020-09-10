import sys
from .game_state import GameState
from .game_view import GameView

class Game:
    """! A class to control the running of the game."""
    def __init__(self):
        """! Construct a new Game object."""
        self._game_view = GameView()
        self._mode = "start"
        self._banner("start", self._start)

    def _start(self):
        (condition, score) = self._game_loop()
        if condition == "win":
            self._banner("win", self._win, score)
        else:
            self._banner("lose", self._lose, score)
        return True

    def _banner(self, mode, next, score = None):
        self._game_view.banner(mode, next, sys.exit, score)

    def _win(self):
        return False

    def _lose(self):
        return False

    def _game_loop(self):
        print("game loop")
        state = GameState(self._game_view.time)
        view = self._game_view.game_view(state)
        view.tick(self._internal_step, sys.exit)
        return (state.condition, state.score)

    def _internal_step(self, state, time, direction):
        state.update(time, direction)
        if state.over:
            return False
        return True
