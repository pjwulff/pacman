from .moving_sprite_controller import MovingSpriteController

## The controller for the Avatar
class AvatarController(MovingSpriteController):

    ## Create a new Avatar controller.
    #
    # @param sprite The avatar this controller should control.
    def __init__(self, sprite):
        super().__init__(sprite)
