import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gdk, Gtk, GObject
import pkg_resources
from .avatar_view import AvatarView
from .banner_view import BannerView
from .dot_view import DotView
from .ghost_view import GhostView
from .power_view import PowerView
from .square_arena_view import SquareArenaView


class GameView(Gtk.DrawingArea):
    def __init__(self, controller, state, next, **kwargs):
        super().__init__(**kwargs)
        self.set_can_focus(True)
        self._controller = controller
        self._state = state
        self._next = next
        if state.shape == "square":
            self._arena_view = SquareArenaView(state.arena)
        self._avatar_view = AvatarView(state.avatar, self._arena_view)
        self._ghost_views = {}
        for ghost in state.ghosts:
            self._ghost_views[ghost] = GhostView(state.ghosts[ghost], self._arena_view)
        self._dot_view = DotView(self._arena_view)
        self._power_view = PowerView(self._arena_view)
        rect = self._arena_view.rect
        self.set_size_request(rect.width, rect.height)
        self.set_visible(True)
        self.connect("draw", self.draw)
        self.connect("key-press-event", self.on_key_press)
        self.connect("key-release-event", self.on_key_release)
        GObject.timeout_add(1000.0/240.0, self.tick)
        
    
    def draw(self, widget, cr):
        self._arena_view.draw(cr)
        for dot in self._state.dots:
            self._dot_view.view(dot).draw(cr)
        for power in self._state.powers:
            self._power_view.view(power).draw(cr)
        for ghost in self._ghost_views:
            self._ghost_views[ghost].draw(cr)
        self._avatar_view.draw(cr)
        self._draw_hud(cr)
    
    def _draw_hud(self, cr):
        cr.set_font_size(24)
        cr.set_source_rgb(1.0, 1.0, 1.0)
        cr.move_to(60, 24)
        cr.show_text("LIVES")
        cr.move_to(60, 48)
        cr.show_text(str(self._state.lives))
        cr.move_to(240, 24)
        cr.show_text("HIGH SCORE")
        cr.move_to(240, 48)
        cr.show_text(str(self._state.score))
        cr.move_to(480, 24)
        cr.show_text("LEVEL")
        cr.move_to(480, 48)
        cr.show_text(str(self._state.level))
    
    def tick(self):
        self.queue_draw()
        cont = self._controller.step()
        if not cont:
            self._next(self._state.condition, self._state.score)
        return cont
    
    def on_key_press(self, widget, event):
        if event.keyval == Gdk.KEY_Down:
            self._controller.add_direction("down")
        elif event.keyval == Gdk.KEY_Up:
            self._controller.add_direction("up")
        elif event.keyval == Gdk.KEY_Left:
            self._controller.add_direction("left")
        elif event.keyval == Gdk.KEY_Right:
            self._controller.add_direction("right")
    
    def on_key_release(self, widget, event):
        if event.keyval == Gdk.KEY_Down:
            self._controller.remove_direction("down")
        elif event.keyval == Gdk.KEY_Up:
            self._controller.remove_direction("up")
        elif event.keyval == Gdk.KEY_Left:
            self._controller.remove_direction("left")
        elif event.keyval == Gdk.KEY_Right:
            self._controller.remove_direction("right")