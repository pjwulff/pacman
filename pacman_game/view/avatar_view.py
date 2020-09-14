import cairo
import math
import time
from .sprite_view import SpriteView

AVATAR_RADIUS = 9

class AvatarView(SpriteView):
    def __init__(self, avatar):
        SpriteView.__init__(self, avatar)
        self._last_angle = 0

    def draw(self, cr):
        coord = self._sprite.coordinate
        x = coord.x
        y = coord.y
        open_angle = (1+math.sin(4*math.pi*time.monotonic()))/2
        direction_angle = self._sprite.direction
        if direction_angle is None:
            direction_angle = self._last_angle
        else:
            direction_angle = -direction_angle
            self._last_angle = direction_angle
        cr.move_to(x, y)
        cr.arc(x, y, AVATAR_RADIUS, direction_angle+open_angle, direction_angle-open_angle)
        cr.close_path()
        cr.set_source_rgb(1.0, 1.0, 0.0)
        cr.fill()
