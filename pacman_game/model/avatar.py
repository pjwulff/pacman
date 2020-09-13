from .moving_sprite import MovingSprite

AVATAR_RADIUS = 11

class Avatar(MovingSprite):
    """! Represents the controllable yellow avatar in the game."""

    def __init__(self, arena):
        """! Create a new avatar.

        @param arena The arena object to which this avatar belongs."""
        MovingSprite.__init__(self, arena, AVATAR_RADIUS, "avatar")
