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
        self._win = self.props.active_window
        if not self._win:
            self._win = PacmanWindow(self._controller, application=self)
        self._win.present()
    
    def start_game(self):
        controller = self._controller.start_game()
        view = GameView(controller, controller.state)
        self._win.view = view
