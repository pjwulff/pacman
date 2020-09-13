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
from .popover_menu import PopoverMenu
    

class MenuButton(Gtk.MenuButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_visible(True)
        self.set_can_focus(True)
        self.set_image(Gtk.Image.new_from_icon_name("open-menu-symbolic", Gtk.IconSize.MENU))
        self._popover = PopoverMenu()
        self.set_popover(self._popover)
    
    def disable(self):
        self.set_sensitive(False)
        self._popover.disable()
    
    def enable(self):
        self.set_sensitive(True)
        self._popover.enable()
        
    @property
    def difficulty(self):
        return self._popover.difficulty
        
    @property
    def shape(self):
        return self._popover.shape

class TitleBar(Gtk.HeaderBar):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_title("Pacman")
        self.set_show_close_button(True)
        self.set_visible(True)
        self._menu_button = MenuButton()
        self.pack_end(self._menu_button)
    
    def disable(self):
        self._menu_button.disable()
    
    def enable(self):
        self._menu_button.enable()
        
    @property
    def difficulty(self):
        return self._menu_button.difficulty
        
    @property
    def shape(self):
        return self._menu_button.shape

class PacmanWindow(Gtk.ApplicationWindow):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._titlebar = TitleBar()
        self.set_titlebar(self._titlebar)
        self.set_resizable(False)
        self._view = None
    
    @property
    def view(self):
        return self._view
    
    @view.setter
    def view(self, view):
        if self._view is not None:
            self.remove(self._view)
        self._view = view
        self.add(view)
    
    def disable(self):
        self._titlebar.disable()
    
    def enable(self):
        self._titlebar.enable()
        
    @property
    def difficulty(self):
        return self._titlebar.difficulty
        
    @property
    def shape(self):
        return self._titlebar.shape
