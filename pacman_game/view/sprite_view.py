## An abstract base class for drawing sprites.
class SpriteView:

    ## Create a new SpriteView.
    #
    # @param sprite The sprite to be viewed.
    def __init__(self, sprite):
        self._sprite = sprite

    ## Draw the sprite.
    #
    # @param cr The cairo context to be used for drawing.
    def draw(self, cr):
        pass
