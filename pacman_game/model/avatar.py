from .moving_sprite import MovingSprite

AVATAR_RADIUS = 11

## Represents the yellow Avatar in the game.
class Avatar(MovingSprite):

    ## Create a new Avatar.
    #
    # @param arena The Arena where this Avatar will live.
    def __init__(self, arena):
        MovingSprite.__init__(self, arena, AVATAR_RADIUS, "avatar")
