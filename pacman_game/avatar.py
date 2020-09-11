from .moving_sprite import MovingSprite

AVATAR_WIDTH = 30
AVATAR_HEIGHT = 33

class Avatar(MovingSprite):
    """! Represents the controllable yellow avatar in the game."""

    def __init__(self, arena):
        """! Create a new avatar.

        @param arena The arena object to which this avatar belongs."""
        MovingSprite.__init__(self, arena, AVATAR_WIDTH, AVATAR_HEIGHT, "avatar")

    def set_direction(self, direction):
        self._user_direction = direction

    def _new_direction(self):
        direction = self._user_direction
        if "left" in direction and self._from_pos.neighbour("left") is not None:
            return "left"
        elif "right" in direction and self._from_pos.neighbour("right") is not None:
            return "right"
        elif "up" in direction and self._from_pos.neighbour("up") is not None:
            return "up"
        elif "down" in direction and self._from_pos.neighbour("down") is not None:
            return "down"
        if self._from_pos.neighbour(self._direction) is not None:
            return self._direction
        else:
            return None

    def _turn_around(self):
        direction = self._user_direction
        if self._direction == "left" and "right" in direction:
            return True
        if self._direction == "right" and "left" in direction:
            return True
        if self._direction == "up" and "down" in direction:
            return True
        if self._direction == "down" and "up" in direction:
            return True
        return False

    def _pick_initial_direction(self):
        self._direction = self._new_direction()
        if self._direction is not None:
            self._start = False
            if self._from_pos.neighbour(self._direction) != self._to_pos:
                temp = self._from_pos
                self._from_pos = self._to_pos
                self._to_pos = temp
            self._calculate_speed()
