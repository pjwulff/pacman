from .shape import Shape

## A circle shape, used for hit detection by the sprites.
class Circle(Shape):

    ## Create a new circle.
    #
    # @param radius The radius of the circle.
    # @param coordinate The coordinates of the centre of the circle.
    def __init__(self, radius, coordinate = None):
        super().__init__(coordinate)
        self._radius = radius
    
    ## Get the radius of the circle.
    #
    # @return The radius of the circle.
    @property
    def radius(self):
        return self._radius
    
    ## Set the radius of the circle.
    #
    # @param radius The radius of the circle.
    @radius.setter
    def radius(self, radius):
        self._radius = radius
    
    ## Create a new circle with the same properties as this one but moved by
    ## some offset.
    #
    # @param offset The amount by which to move the circle.
    #
    # @return A new circle, moved by some offset.
    def move(self, offset):
        return Circle(self.radius, self.coordinate.move(offset))
    
    ## Detects if two circles overlap by any amount. Used for hit detection.
    #
    # @param other The other circle.
    #
    # @return True if the two circles overlap by any amount.
    def collide(self, other):
        distance = self.coordinate.distance(other.coordinate)
        return distance < (self.radius + other.radius)
