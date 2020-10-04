import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio

from .controller.game_controller import GameControllerFactory
from .controller.high_scores_controller import HighScoresController
from .view.enter_high_score_dialogue import EnterHighScoreDialogue
from .view.game_view import GameView
from .view.window import PacmanWindow

class Game(Gtk.Application):
    def __init__(self):
        super().__init__(application_id='org.peterleddiman.Pacman',
                         flags=Gio.ApplicationFlags.FLAGS_NONE)
        self._controller = None

    def do_activate(self):
        self._window = self.props.active_window
        if not self._window:
            self._window = PacmanWindow(self.start_game)
        self._window.present()
        Gtk.main()

    def start_game(self, difficulty, shape, size):
        self._disable()
        self._controller = GameControllerFactory.make_controller(
            difficulty = difficulty,
            shape = shape,
            size = size)
        world = self._controller.world
        l = lambda: self.game_over(world.score, difficulty, shape, size)
        view = GameView(self._controller, self._controller.world, l)
        self._window.display_game_view(view)

    def game_over(self, score, difficulty, shape, size):
        self._controller = None
        dialogue = EnterHighScoreDialogue(score)
        dialogue.run()
        initials = dialogue.get_result()
        if initials is not None and initials != "":
            HighScoresController.insert_high_score(initials, score, difficulty, shape, size)
        self.display_start_screen()

    def display_start_screen(self):
        self._enable()
        self._window.display_start_screen()

    def _enable(self):
        self._window.enable()

    def _disable(self):
        self._window.disable()

    def do_shutdown(self):
        Gtk.Application.do_shutdown(self)
        if self._controller is not None:
            self._controller.quit()
