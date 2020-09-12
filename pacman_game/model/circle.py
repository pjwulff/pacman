from .shape import Shape

class Circle(Shape):
    def __init__(self, radius, coordinate = None):
        super().__init__(coordinate)
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, radius):
        self._radius = radius
    
    def move(self, offset):
        return Circle(self.radius, self.coordinate.move(offset))
    
    def collide(self, other):
        distance = self.coordinate.distance(other.coordinate)
        return distance <= (self.radius + other.radius)

    def __str__(self):
        return f"{self.x}, {self.y}, {self.radius}"
