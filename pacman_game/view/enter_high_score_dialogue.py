from pkg_resources import resource_filename
from gi.repository import Gtk

## A dialogue box for entering high scores.
class EnterHighScoreDialogue(Gtk.Dialog):
    __gtype_name__ = "EnterHighScoreDialogue"

    ## Initialise the object.
    #
    # @param builder The Gtk.Builder object that built this object from the
    # XML.
    # @param score The high score we are to enter in the database.
    def __init(self, builder, score):
        super().__init__()
        score_label = builder.get_object("high-score")
        score_label.set_text(str(score))
        self._entry = builder.get_object("initials-entry")
        self._res = None

    ## Create a new EnterHighScoreDialogue by building it from XML.
    #
    # @param score The high score we are to enter in the database.
    def __new__(cls, score):
        builder = Gtk.Builder()
        path = resource_filename("pacman_game",
                                 "data/ui/enter-high-score-dialogue.glade")
        builder.add_from_file(path)
        obj = builder.get_object("enter-high-score-dialogue")
        obj.__init(builder, score)
        builder.connect_signals(obj)
        return obj

    ## Callback triggered if the user clicks the `cancel' button.
    def on_cancel_button_clicked(self, *args):
        self.emit("response", 0)
        self.destroy()

    ## Callback triggered if the user clicks the `save' button.
    def on_save_button_clicked(self, *args):
        self._res = self._entry.get_text()
        self.emit("response", 0)
        self.destroy()

    ## Get the initials entered into the text entry.
    #
    # @return The contents of the text entry.
    def get_result(self):
        return self._res
