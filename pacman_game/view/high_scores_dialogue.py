from pkg_resources import resource_filename
from gi.repository import Gtk

class HighScore(Gtk.ListBoxRow):
    __gtype_name__ = "HighScore"

    def __init(self, builder):
        super().__init__()

    def __new__(cls):
        builder = Gtk.Builder()
        path = resource_filename("pacman_game", "data/ui/high-score.glade")
        builder.add_from_file(path)
        obj = builder.get_object("high-score")
        obj.__init(builder)
        builder.connect_signals(obj)
        return obj

class HighScoresDialogue(Gtk.Dialog):
    __gtype_name__ = "HighScoresDialogue"

    def __init(self, builder):
        super().__init__()

    def __new__(cls):
        builder = Gtk.Builder()
        path = resource_filename("pacman_game", "data/ui/high-scores-dialogue.glade")
        builder.add_from_file(path)
        obj = builder.get_object("high-scores-dialogue")
        obj.__init(builder)
        builder.connect_signals(obj)
        return obj
