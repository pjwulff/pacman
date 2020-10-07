import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gdk, Gtk, GObject
import math
from .arena_view_factory import ArenaViewFactory
from .avatar_view import AvatarView
from .dot_view import DotView
from .ghost_view import GhostView
from .power_view import PowerView

## A View to handle viewing the game. Many viewing tasks are delegated to
## sub-view objects.
class GameView(Gtk.DrawingArea):

    ## Create a new GameView object.
    #
    # @param controller The GameController used for this game. We will send this
    # controller user input.
    # @param world The World object representing the state of the game. We will
    # use this model as a source for information of what to draw.
    # @param next A callback to be called with the game ends,
    def __init__(self, controller, world, **kwargs):
        super().__init__(**kwargs)
        self.set_can_focus(True)
        self._controller = controller
        self._world = world
        self._scale = 1.5
        self._avatar_view = AvatarView(world.avatar)
        self._arena_view = ArenaViewFactory.make_arena_view(world.arena)
        self._ghost_views = {}
        for ghost in world.ghosts:
            self._ghost_views[ghost] = GhostView(world.ghosts[ghost])
        rect = self._arena_view.rect
        self.set_size_request((rect.width + 48) * self._scale,
                              (rect.height + 96) * self._scale)
        self.set_hexpand(False)
        self.set_vexpand(False)
        self.set_visible(True)
        self._keys = [False] * 4
        self.connect("draw", self.draw)
        self.connect("key-press-event", self.on_key_press)
        self.connect("key-release-event", self.on_key_release)
        GObject.timeout_add(1000.0/60.0, self.tick)
        self._continue = True

    ## A callback to be called when we need to draw the view.
    #
    # @param widget The widget which raised the signal which called this
    # function.
    # @param cr The cairo context to be used for drawing.
    def draw(self, widget, cr):
        cr.scale(self._scale, self._scale)
        cr.save()
        cr.translate(24, 72)
        self._arena_view.draw(cr)
        for dot in self._world.dots:
            DotView(dot).draw(cr)
        for power in self._world.powers:
            PowerView(power).draw(cr)
        for ghost in self._ghost_views:
            self._ghost_views[ghost].draw(cr)
        self._avatar_view.draw(cr)
        cr.restore()
        self._draw_hud(cr)
        self._keys = [False]*4
    
    ## Draw the HUD (i.e., level, score, lives).
    #
    # @param cr The cairo context to be used for drawing.
    def _draw_hud(self, cr):
        width = self._arena_view.rect.width + 48
        cr.set_font_size(18)
        cr.set_source_rgb(1.0, 1.0, 1.0)
        cr.move_to(12, 24)
        cr.show_text("LIVES")
        cr.move_to(12, 48)
        cr.show_text(str(self._world.lives))
        (_, _, w, _, _, _) = cr.text_extents("SCORE")
        cr.move_to(width/2 - w/2, 24)
        cr.show_text("SCORE")
        cr.move_to(width/2 - w/2, 48)
        cr.show_text(str(self._world.score))
        (_, _, w, _, _, _) = cr.text_extents("LEVEL")
        cr.move_to(width - w - 12, 24)
        cr.show_text("LEVEL")
        cr.move_to(width - w - 12, 48)
        cr.show_text(str(self._world.level))
    
    ## A callback used by a timer to trigger the `draw' event.
    #
    # @return True if the timer should be triggered again (because the game is
    # not over), False otherwise.
    def tick(self):
        self.queue_draw()
        return self._continue

    def stop(self):
        self._continue = False
    
    ## Get the index into an array for an arrow keypress.
    #
    # @param keyval A Gdk.Keyvalue for a keypress.
    #
    # @return The index for an array to store keypresses.
    def _key_index(self, keyval):
        if keyval == Gdk.KEY_Down:
            return 0
        elif keyval == Gdk.KEY_Up:
            return 1
        elif keyval == Gdk.KEY_Left:
            return 2
        elif keyval == Gdk.KEY_Right:
            return 3

    ## A callback triggered when the user presses a key.
    #
    # @param widget The widget which triggered the event.
    # @param event The event associated with the key press.
    def on_key_press(self, widget, event):
        index = self._key_index(event.keyval)
        if index is not None:
            self._keys[index] = True
        if event.keyval == Gdk.KEY_q:
            self._controller.quit()
            return True
        self._controller.set_direction(self._direction(self._keys))
        return True
    
    ## A callback triggered when the user releases a key.
    #
    # @param widget The widget which triggered the event.
    # @param event The event associated with the key release.
    def on_key_release(self, widget, event):
        index = self._key_index(event.keyval)
        if index is not None:
            self._keys[index] = False
        if event.keyval == Gdk.KEY_q:
            self._controller.quit()
            return True
        self._controller.set_direction(self._direction(self._keys))
        return True

    ## Calculate the direction the user is pressing as an angle in radians.
    #
    # @param keys A list of booleans representing which keys the user is
    # pressing.
    #
    # @return An angle in radians.
    def _direction(self, keys):
        x = 0
        y = 0
        if keys[0]:
            y -= 1
        if keys[1]:
            y += 1
        if keys[2]:
            x -= 1
        if keys[3]:
            x += 1
        if y == 0 and x == 0:
            return None
        angle = math.atan2(y, x)
        return angle

