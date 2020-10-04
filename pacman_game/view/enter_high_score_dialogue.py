from pkg_resources import resource_filename
from gi.repository import Gtk

class EnterHighScoreDialogue(Gtk.Dialog):
    __gtype_name__ = "EnterHighScoreDialogue"

    def __init(self, builder, score):
        super().__init__()
        score_label = builder.get_object("high-score")
        score_label.set_text(str(score))
        self._entry = builder.get_object("initials-entry")
        self._res = None

    def __new__(cls, score):
        builder = Gtk.Builder()
        path = resource_filename("pacman_game", "data/ui/enter-high-score-dialogue.glade")
        builder.add_from_file(path)
        obj = builder.get_object("enter-high-score-dialogue")
        obj.__init(builder, score)
        builder.connect_signals(obj)
        return obj

    def on_cancel_button_clicked(self, *args):
        self.emit("response", 0)
        self.destroy()

    def on_save_button_clicked(self, *args):
        self._res = self._entry.get_text()
        self.emit("response", 0)
        self.destroy()

    def get_result(self):
        return self._res
