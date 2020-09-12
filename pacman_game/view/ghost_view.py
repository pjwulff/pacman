import cairo
import pkg_resources
from .sprite_view import SpriteView

class GhostView(SpriteView):
    def __init__(self, ghost, arena_view):
        path = pkg_resources.resource_filename(__name__, f"../data/images/{ghost.name}.png")
        image = cairo.ImageSurface.create_from_png(path)
        SpriteView.__init__(self, ghost, image, arena_view)
        path = pkg_resources.resource_filename(__name__, "../data/images/scared-ghost.png")
        self._scared_image = cairo.ImageSurface.create_from_png(path)
        eyes_path = {
            "up": "../data/images/eyes-up.png",
            "down": "../data/images/eyes-down.png",
            "left": "../data/images/eyes-left.png",
            "right": "../data/images/eyes-right.png",
        }
        self._eyes = {}
        for path in eyes_path:
            p = pkg_resources.resource_filename(__name__, eyes_path[path])
            self._eyes[path] = cairo.ImageSurface.create_from_png(p)

    def draw(self, cr):
        """! Draw this sprite to the screen.

        @param screen The PyGame screen to which this sprite to draw."""
        r = self.rect
        x = r.x - r.width/2
        y = r.y - r.height/2
        if self._sprite.scared and self._sprite.alive:
            cr.set_source_surface(self._scared_image, x, y)
            cr.paint()
        else:
            if self._sprite.alive:
                cr.set_source_surface(self._image, x, y)
                cr.paint()
            direction = self._sprite.direction
            if "left" in direction:
                d = "left"
            elif "right" in direction:
                d = "right"
            elif "up" in direction:
                d = "up"
            elif "down" in direction:
                d = "down"
            else:
                d = "up"
            cr.set_source_surface(self._eyes[d], x, y)
            cr.paint()
