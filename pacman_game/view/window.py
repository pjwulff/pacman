from pkg_resources import resource_filename
from gi.repository import Gtk

def selected_radio(group):
    for radio in group:
        if radio.get_active():
            return radio

class PacmanWindow(Gtk.ApplicationWindow):
    __gtype_name__ = "PacmanWindow"
    
    def __init(self, next, builder):
        super().__init__()
        self._next = next
        self._high_scores_button = builder.get_object("high-scores-button")
        self._difficulty_group = builder.get_object("difficulty-easy").get_group()
        self._shape_group = builder.get_object("shape-square").get_group()
        self._size_group = builder.get_object("size-small").get_group()
        self._stack = builder.get_object("main-stack")
        
    def __new__(cls, next):
        builder = Gtk.Builder()
        path = resource_filename("pacman_game", "data/ui/window.glade")
        builder.add_from_file(path)
        obj = builder.get_object("main-window")
        obj.__init(next, builder)
        builder.connect_signals(obj)
        return obj

    def on_high_scores_button_activate(self, *args):
        pass
    
    def on_main_window_destroy(self, *args):
        Gtk.main_quit()
    
    def on_start_button_clicked(self, *args):
        self._next(self.difficulty, self.shape, self.size)
    
    def display_start_screen(self):
        self._stack.set_visible_child_name("main-view")
        game_view = self._stack.get_child_by_name("game-view")
        if game_view is not None:
            self._stack.remove(game_view)
    
    def display_game_view(self, view):
        self._stack.add_named(view, "game-view")
        self._stack.set_visible_child_name("game-view")
    
    def disable(self):
        self._high_scores_button.set_sensitive(False)
    
    def enable(self):
        self._high_scores_button.set_sensitive(True)
        
    @property
    def difficulty(self):
        radio = selected_radio(self._difficulty_group)
        name = radio.get_name()
        if name == "difficulty-easy":
            return "easy"
        elif name == "difficulty-medium":
            return "medium"
        elif name == "difficulty-hard":
            return "hard"
        else:
            return None

    @property
    def shape(self):
        radio = selected_radio(self._shape_group)
        name = radio.get_name()
        if name == "shape-square":
            return "square"
        elif name == "shape-hexagonal":
            return "hexagonal"
        elif name == "shape-graph":
            return "graph"
        else:
            return None

    @property
    def size(self):
        radio = selected_radio(self._size_group)
        name = radio.get_name()
        if name == "size-small":
            return "small"
        elif name == "size-medium":
            return "medium"
        elif name == "size-large":
            return "large"
        else:
            return None
