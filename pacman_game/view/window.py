from pkg_resources import resource_filename
from gi.repository import Gtk
from .high_scores_dialogue import HighScoresDialogue

def selected_radio(group):
    for radio in group:
        if radio.get_active():
            return radio

## A Gtk.ApplicationWindow for the primary window for the game.
class PacmanWindow(Gtk.ApplicationWindow):
    __gtype_name__ = "PacmanWindow"
    
    ## Initialise a new PacmanWindow object.
    #
    # @param next A callback to be called when the user clicks the `Start'
    # button.
    # @param builder The Gtk.Builder object that built this object from XML.
    def __init(self, next, builder):
        super().__init__()
        self._next = next
        self._high_scores_button = builder.get_object("high-scores-button")
        self._difficulty_group = \
            builder.get_object("difficulty-easy").get_group()
        self._shape_group = builder.get_object("shape-square").get_group()
        self._size_group = builder.get_object("size-small").get_group()
        self._stack = builder.get_object("main-stack")

    ## Create a new PacmanWindow object.
    #
    # @param next A callback to be called when the user clicks the `Start'
    # button.
    def __new__(cls, next):
        builder = Gtk.Builder()
        path = resource_filename("pacman_game", "data/ui/window.glade")
        builder.add_from_file(path)
        obj = builder.get_object("main-window")
        obj.__init(next, builder)
        builder.connect_signals(obj)
        return obj

    ## A callback called when the user clicks the `High Scores' button.
    def on_high_scores_button_activate(self, *args):
        dialogue = HighScoresDialogue()
        dialogue.run()
    
    ## A callback called when the user closes the window.
    def on_main_window_destroy(self, *args):
        Gtk.main_quit()
    
    ## A callback called when the user clicks the `Start' button.
    def on_start_button_clicked(self, *args):
        self._next(self.difficulty, self.shape, self.size)
    
    ## Instruct the window to show the initial start screen.
    def display_start_screen(self):
        game_view = self._stack.get_child_by_name("game-view")
        if game_view is not None:
            self._stack.remove(game_view)
            game_view.destroy()

    ## Instruct the window to display a GameView.
    #
    # @param view The GameView object to be displayed in the window.
    def display_game_view(self, view):
        self._stack.add_named(view, "game-view")
        self._stack.set_visible_child_name("game-view")

    ## Disable the main user interface (that is, the `High Scores' button and
    ## main menu button). This is used when the game starts.
    def disable(self):
        self._high_scores_button.set_sensitive(False)
    
    ## Enable the main user interface (that is, the `High Scores' button and
    ## main menu button). This is used when the game ends.
    def enable(self):
        self._high_scores_button.set_sensitive(True)

    ## Get the selected difficulty in the preferences.
    #
    # @return The selected difficulty as a string.
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

    ## Get the selected shape in the preferences.
    #
    # @return The selected shape as a string.
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

    ## Get the selected size in the preferences
    #
    # @return The selected size as a string.
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
