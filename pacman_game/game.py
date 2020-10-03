import pkg_resources
import sys

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio

from .controller.game_controller import GameController
from .view.game_view import GameView
from .view.window import PacmanWindow

class Game(Gtk.Application):
    def __init__(self):
        super().__init__(application_id='org.peterleddiman.Pacman',
                         flags=Gio.ApplicationFlags.FLAGS_NONE)
        self._controller = GameController()

    def do_activate(self):
        self._window = self.props.active_window
        if not self._window:
            self._window = PacmanWindow(self.start_game)
        self._window.present()
        Gtk.main()

    def start_game(self, difficulty, shape, size):
        self._disable()
        controller = self._controller.start_game(difficulty, shape)
        view = GameView(controller, controller.state, self.game_over)
        self._window.display_game_view(view)

    def game_over(self, score):
        self.display_start_screen()

    def display_start_screen(self):
        self._enable()
        self._window.display_start_screen()

    def _enable(self):
        self._window.enable()

    def _disable(self):
        self._window.disable()

    def on_quit(self, action, param):
        self.quit()

