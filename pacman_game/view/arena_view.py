from gi.repository import Gtk
from gi.repository import Gdk
import cairo

import pkg_resources
from ..model.arena import Arena
from ..model.rect import Rect

class ArenaView:
    def __init__(self, arena):
        self._arena = arena
        path = pkg_resources.resource_filename(__name__, f"../data/images/{arena.image()}")
        self._image = cairo.ImageSurface.create_from_png(path)
        self._screen_rect = Rect(self._image.get_width(), self._image.get_height())

    def draw(self, cr):
        """! Draws the entire arena background to the screen, or optionally
        just a section of it. This is used to erase a sprite.

        @param screen The PyGame screen object on which to draw.
        @param rect An optional Rect object to specify which part of the Arena
        to drawn. If not given, this method draws the entire arena."""
        cr.set_source_rgb(0, 0, 0)
        cr.paint()
        cr.set_source_surface(self._image, 0, 0)
        cr.paint()
    
    @property
    def rect(self):
        return self._screen_rect
