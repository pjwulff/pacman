from .coordinate import Coordinate
from .sprite import Sprite

## An abstract base class for all moving sprites.
class MovingSprite(Sprite):

    ## Create a new MovingSprite.
    #
    # @param arena The Arena where this sprite will live.
    # @param radius The radius of the circle for this sprite's hitbox.
    # @param name The name of this sprite.
    def __init__(self, arena, radius, name):
        Sprite.__init__(self, Coordinate(0, 0), radius, name)
        self._arena = arena
        self.return_to_spawn()
        self._last_angle = None
    
    ## Return this sprite to its spawn location,
    def return_to_spawn(self):
        self._from_pos = self.start_pos
        self._to_pos = self._from_pos
        self.trans_pos = 0.0
        self.calculate_position()
        self._last_angle = None
        
    ## Moving sprites in this game travel between vertices in the graph.
    ## Their current position between the two is a value between 0 and 1
    ## and is called the sprite's trans-position. This function returns it.
    #
    # @return The sprites' trans-position.
    @property
    def trans_pos(self):
        return self._trans_pos
    
    ## Set the sprite's trans-position.
    #
    # @param trans_pos The sprite's new trans-position.
    @trans_pos.setter
    def trans_pos(self, trans_pos):
        self._trans_pos = trans_pos

    ## Calculate this sprite's current coordinates based on its from-pos,
    ## to-pos and trans-position.
    def calculate_position(self):
        from_x = self.from_pos.x
        from_y = self.from_pos.y
        to_x = self.to_pos.x
        to_y = self.to_pos.y
        
        self.x = from_x + (to_x - from_x) * self._trans_pos
        self.y = from_y + (to_y - from_y) * self._trans_pos
    
    ## Get the sprite's starting position (also its spawn location).
    #
    # @return A node in the graph.
    @property
    def start_pos(self):
        return self._arena.start_pos(self.name)

    ## Get the sprite's current `from' node; that is, which node this sprite
    ## is moving from.
    #
    # @return A node in the graph.
    @property
    def from_pos(self):
        return self._from_pos

    ## Set the sprite's current `from' node; that is, which node this sprite
    ## is moving from.
    #
    # @param from_pos A node in the graph from which this sprite is moving.
    @from_pos.setter
    def from_pos(self, from_pos):
        self._from_pos = from_pos

    ## Get the sprite's current `to' node; that is, which node this sprite is
    ## current moving towards.
    #
    # @return A node in the graph.
    @property
    def to_pos(self):
        return self._to_pos

    ## Set the sprite's current `to' node; that is, which node this sprite is
    ## currently moving towards
    #
    # @param to_pos A node in the graph to which this sprite is moving.
    @to_pos.setter
    def to_pos(self, to_pos):
        self._to_pos = to_pos

    ## Get the direction this sprite is currently facing. This may be None
    ## if the sprite is yet to move.
    #
    # @return An angle, or None if this sprite has not begun moving.
    @property
    def direction(self):
        if self.from_pos == self.to_pos:
            return self._last_angle
        d = self.from_pos.direction(self.to_pos)
        if d is not None:
            self._last_angle = d
        return d
