from pkg_resources import resource_filename
from gi.repository import Gtk
from ..controller.high_scores_controller import HighScoresController

## A Gtk.ListBoxRow to for a high score.
class HighScore(Gtk.ListBoxRow):
    __gtype_name__ = "HighScore"

    ## Initialise a HighScore object.
    #
    # @param initials The initials of the high score.
    # @param score The high score value.
    # @param builder The Gtk.Builder object that built this object from XML.
    def __init(self, initials, score, builder):
        super().__init__()
        self._initials = initials
        self._score = score
        self._initials_label = builder.get_object("initials")
        self._score_label = builder.get_object("score")
        self._initials_label.set_text(initials)
        self._score_label.set_text(str(score))

    ## Create a new HighScore object from XML.
    #
    # @param initials The initials of the high score.
    # @param score The high score value.
    def __new__(cls, initials, score):
        builder = Gtk.Builder()
        path = resource_filename("pacman_game", "data/ui/high-score.glade")
        builder.add_from_file(path)
        obj = builder.get_object("high-score")
        obj.__init(initials, score, builder)
        builder.connect_signals(obj)
        return obj


## A dialogue box for viewing and filtering high scores.
class HighScoresDialogue(Gtk.Dialog):
    __gtype_name__ = "HighScoresDialogue"

    ## Initialise a HighScoresDialogue object
    #
    # @param builder The Gtk.Builder object that built this object from XML.
    def __init(self, builder):
        super().__init__()
        self._stack = builder.get_object("scores-stack")
        self._scores_list = builder.get_object("high-scores-list")
        self._difficulty_easy = builder.get_object("filter-difficulty-easy")
        self._difficulty_medium = builder.get_object("filter-difficulty-medium")
        self._difficulty_hard = builder.get_object("filter-difficulty-hard")
        self._shape_square = builder.get_object("filter-shape-square")
        self._shape_hexagonal = builder.get_object("filter-shape-hexagonal")
        self._shape_graph = builder.get_object("filter-shape-graph")
        self._size_small = builder.get_object("filter-size-small")
        self._size_medium = builder.get_object("filter-size-medium")
        self._size_large = builder.get_object("filter-size-large")
        self._no_scores_label = builder.get_object("no-scores-label")
        self._high_scores_window = builder.get_object("high-scores-window")
        self.on_filter_toggled()

    ## Create a new HighScoresDialogue object.
    def __new__(cls):
        builder = Gtk.Builder()
        path = resource_filename("pacman_game",
                                 "data/ui/high-scores-dialogue.glade")
        builder.add_from_file(path)
        obj = builder.get_object("high-scores-dialogue")
        obj.__init(builder)
        builder.connect_signals(obj)
        return obj

    ## A callback called when one of the filter checkboxes is toggled.
    def on_filter_toggled(self, *args):
        f = self._filter()
        high_scores = HighScoresController.high_scores(f)
        if len(high_scores) == 0:
            self._stack.set_visible_child(self._no_scores_label)
        else:
            for child in self._scores_list.get_children():
                self._scores_list.remove(child)
            for high_score in high_scores:
                score = HighScore(high_score[0], high_score[1])
                self._scores_list.add(score)
            self._stack.set_visible_child(self._high_scores_window)

    ## Constructs a new dictionary representing the values of the filter
    ## checkboxes. This is used to be passed to controller.HighScores to
    ## retrieve filtered high scoers.
    def _filter(self):
        f = {
            "difficulty-easy": self._difficulty_easy.get_active(),
            "difficulty-medium": self._difficulty_medium.get_active(),
            "difficulty-hard": self._difficulty_hard.get_active(),
            "shape-square": self._shape_square.get_active(),
            "shape-hexagonal": self._shape_hexagonal.get_active(),
            "shape-graph": self._shape_graph.get_active(),
            "size-small": self._size_small.get_active(),
            "size-medium": self._size_medium.get_active(),
            "size-large": self._size_large.get_active(),
        }
        return f
