import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gdk, Gtk, GObject
import math
from .arena_view_factory import ArenaViewFactory
from .avatar_view import AvatarView
from .banner_view import BannerView
from .dot_view import DotView
from .ghost_view import GhostView
from .power_view import PowerView


class GameView(Gtk.DrawingArea):
    def __init__(self, controller, world, next, **kwargs):
        super().__init__(**kwargs)
        self.set_can_focus(True)
        self._controller = controller
        self._world = world
        self._next = next
        self._scale = 1.5
        self._avatar_view = AvatarView(world.avatar)
        self._arena_view = ArenaViewFactory.make_arena_view(world.arena)
        self._ghost_views = {}
        for ghost in world.ghosts:
            self._ghost_views[ghost] = GhostView(world.ghosts[ghost])
        rect = self._arena_view.rect
        self.set_size_request((rect.width + 48) * self._scale, (rect.height + 96) * self._scale)
        self.set_hexpand(False)
        self.set_vexpand(False)
        self.set_visible(True)
        self._keys = [False] * 4
        self.connect("draw", self.draw)
        self.connect("key-press-event", self.on_key_press)
        self.connect("key-release-event", self.on_key_release)
        GObject.timeout_add(1000.0/60.0, self.tick)
        
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
    
    def _draw_hud(self, cr):
        width = self._arena_view.rect.width + 48
        cr.set_font_size(24)
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
    
    def tick(self):
        self.queue_draw()
        cont = not self._controller.over
        if not cont:
            self._next()
        return cont
    
    def _key_index(self, keyval):
        if keyval == Gdk.KEY_Down:
            return 0
        elif keyval == Gdk.KEY_Up:
            return 1
        elif keyval == Gdk.KEY_Left:
            return 2
        elif keyval == Gdk.KEY_Right:
            return 3

    def on_key_press(self, widget, event):
        index = self._key_index(event.keyval)
        if index is not None:
            self._keys[index] = True
        if event.keyval == Gdk.KEY_q:
            self._controller.quit()
        self._controller.set_direction(self._direction(self._keys))
        return True
    
    def on_key_release(self, widget, event):
        index = self._key_index(event.keyval)
        if index is not None:
            self._keys[index] = False
        if event.keyval == Gdk.KEY_q:
            self._controller.quit()
        self._controller.set_direction(self._direction(self._keys))
        return True

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

