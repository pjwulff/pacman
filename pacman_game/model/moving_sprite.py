from .coordinate import Coordinate
from .sprite import Sprite

class MovingSprite(Sprite):
    """! Base class for all sprites which move during gameplay."""
    def __init__(self, arena, radius, name):
        Sprite.__init__(self, Coordinate(0, 0), radius, name)
        self._arena = arena
        self.return_to_spawn()
        self._last_angle = None
    
    def return_to_spawn(self):
        """! Instructs this moving sprite to return to its spawn location.
        Used when the avatar is hit by a ghost and loses a life."""
        self._from_pos = self.start_pos
        self._to_pos = self._from_pos
        self.trans_pos = 0.0
        self.calculate_position()
        self._last_angle = None
        
    @property
    def trans_pos(self):
        return self._trans_pos
    
    @trans_pos.setter
    def trans_pos(self, trans_pos):
        self._trans_pos = trans_pos

    def calculate_position(self):
        from_x = self.from_pos.x
        from_y = self.from_pos.y
        to_x = self.to_pos.x
        to_y = self.to_pos.y
        
        self.x = from_x + (to_x - from_x) * self._trans_pos
        self.y = from_y + (to_y - from_y) * self._trans_pos
    
    @property
    def start_pos(self):
        return self._arena.start_pos(self.name)

    @property
    def from_pos(self):
        """! Moving sprites move between vertices in the graph. This method
        returns the vertex this sprite was moving from.

        @returns The node in the graph this sprite is moving from."""
        return self._from_pos

    @from_pos.setter
    def from_pos(self, from_pos):
        self._from_pos = from_pos

    @property
    def to_pos(self):
        """! Moving sprites move between vertices in the graph. This method
        returns the vertex this sprite is moving towards.

        @returns The node in the graph this sprite is moving to."""
        return self._to_pos

    @to_pos.setter
    def to_pos(self, to_pos):
        self._to_pos = to_pos

    @property
    def direction(self):
        if self.from_pos == self.to_pos:
            return self._last_angle
        d = self.from_pos.direction(self.to_pos)
        if d is not None:
            self._last_angle = d
        return d
