# Copyright 2020 Peter Leddiman
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from gi.repository import Gtk
from .banner_view import BannerView
from .game_view import GameView

class TitleBar(Gtk.HeaderBar):
    def __init__(self, controller, **kwargs):
        super().__init__(**kwargs)
        self._controller = controller
        self.set_title("Pacman")
        self.set_show_close_button(True)
        self.set_visible(True)

class PacmanWindow(Gtk.ApplicationWindow):
    def __init__(self, controller, **kwargs):
        super().__init__(**kwargs)
        self._controller = controller
        self._titlebar = TitleBar(controller)
        self.set_titlebar(self._titlebar)
        self._view = BannerView("START", self.get_application().start_game)
        self.add(self._view)
        self.set_resizable(False)
    
    @property
    def view(self):
        return self._view
    
    @view.setter
    def view(self, view):
        self.remove(self._view)
        self._view = view
        self.add(view)
