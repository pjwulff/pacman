import gi
gi.require_version('Gtk', '3.0')
from gi.repository import GLib, Gtk, Gio

from .controller.game_controller import GameControllerFactory
from .controller.high_scores_controller import HighScoresController
from .view.enter_high_score_dialogue import EnterHighScoreDialogue
from .view.game_view import GameView
from .view.window import PacmanWindow

## A Gtk.Application class to manage the overall game, from creating the window
## to starting controllers.
class Game(Gtk.Application):

    ## Create a new Game object.
    def __init__(self):
        super().__init__(application_id='org.peterleddiman.Pacman',
                         flags=Gio.ApplicationFlags.FLAGS_NONE)
        self._controller = None

    ## A callback called when the Gtk.Application is started.
    def do_activate(self):
        self._window = self.props.active_window
        if not self._window:
            self._window = PacmanWindow(self.start_game)
        self._window.present()
        Gtk.main()

    ## Called when the user wishes to start the game.
    #
    # @param difficulty The selected difficulty.
    # @param shape The selected shape.
    # @param size The selected size.
    def start_game(self, difficulty, shape, size):
        self._disable()
        self._controller = GameControllerFactory.make_controller(
            self.game_over,
            difficulty = difficulty,
            shape = shape,
            size = size)
        world = self._controller.world
        view = GameView(self._controller, self._controller.world)
        self._window.display_game_view(view)

    ## A callback to be called when the game is over.
    #
    # @param score The score achieved by the player, or None if the player
    # quit.
    # @param difficulty The difficulty of the game.
    # @param shape The shape of the maze.
    # @param size The size of the maze.
    def game_over(self, score, difficulty, shape, size):
        self._controller = None
        self._window.stop()
        GLib.idle_add(self._game_over_aux, score, difficulty, shape, size)

    ## An auxilliary function for game_over. It is possible for the game_over
    ## function to be called outside of GLib's main loop, which can cause
    ## problems if the thread then attempts to use Gtk widgets (such as
    ## the high score dialogue). game_over will therefore call this function
    ## in GLib's main thread
    #
    # @param score The score achieved by the player, or None if the player
    # quit.
    # @param difficulty The difficulty of the game.
    # @param shape The shape of the maze.
    # @param size The size of the maze.
    def _game_over_aux(self, score, difficulty, shape, size):
        if score is not None:
            dialogue = EnterHighScoreDialogue(score)
            dialogue.run()
            initials = dialogue.get_result()
            if initials is not None and initials != "":
                HighScoresController.insert_high_score(initials, score,
                                                       difficulty, shape, size)
        self._display_start_screen()

    ## Renable the window's UI and show the start screen.
    def _display_start_screen(self):
        self._enable()
        self._window.display_start_screen()

    ## Enable the GUI.
    def _enable(self):
        self._window.enable()

    ## Disable the GUI.
    def _disable(self):
        self._window.disable()

    ## A callback called when the application should shut down.
    def do_shutdown(self):
        Gtk.Application.do_shutdown(self)
        if self._controller is not None:
            self._controller.quit()
