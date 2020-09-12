from ..model.coordinate import Coordinate
from ..model.rect import Rect

class SpriteView:
    def __init__(self, sprite, image, arena_view):
        self._sprite = sprite
        self._image = image
        self._arena_view = arena_view

    def draw(self, cr):
        """! Draw this sprite to the screen.

        @param screen The PyGame screen to which this sprite to draw."""
        r = self.rect
        x = r.x - r.width/2
        y = r.y - r.height/2
        cr.set_source_surface(self._image, x, y)
        cr.paint()

    @property
    def rect(self):
        x = self._sprite.x
        y = self._sprite.y
        w = self._image.get_width()
        h = self._image.get_height()
        return Rect(w, h, Coordinate(x, y))
