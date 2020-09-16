import sys
import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Gio

from .controller.game_controller import GameController
from .view.banner_view import BannerView
from .view.game_view import GameView
from .view.window import PacmanWindow


class Game(Gtk.Application):
    def __init__(self):
        super().__init__(application_id='org.peterleddiman.Pacman',
                         flags=Gio.ApplicationFlags.FLAGS_NONE)
        self._controller = GameController()

    def do_activate(self):
        self._win = self.props.active_window
        if not self._win:
            self._win = PacmanWindow(application=self)
            self._display_banner(self.start_game)
        self._win.present()
    
    def start_game(self):
        self._win.disable()
        difficulty = self._win.difficulty
        shape = self._win.shape
        controller = self._controller.start_game(difficulty, shape)
        view = GameView(controller, controller.state, self._display_banner)
        self._win.view = view

    def _display_banner(self, next, score = None):
        self._win.enable()
        view = BannerView(self.start_game, score)
        self._win.view = view
