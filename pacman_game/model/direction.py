import math

class Direction:
    def __init__(self, h = None, v = None):
        self._h = h
        self._v = v
        if h is not None and v is None:
            if h == "up" or h == "down":
                self._h = None
                self._v = h
            s = h.split("-", 2)
            if len(s) == 2:
                self._h = s[0]
                self._v = s[1]
    
    @property
    def h(self):
        return self._h
    
    @h.setter
    def h(self, h):
        self._h = h
    
    @property
    def v(self):
        return self._v
    
    @v.setter
    def v(self, v):
        self._v = v
    
    @property
    def valid(self):
        return self.h is not None or self.v is not None
    
    def add_direction(self, direction):
        if direction == "left":
            self.h = "left"
        elif direction == "right":
            self.h = "right"
        elif direction == "up":
            self.v = "up"
        elif direction == "down":
            self.v = "down"
    
    def remove_direction(self, direction):
        if direction == "left" or direction == "right":
            self.h = None
        if direction == "up" or direction == "down":
            self.v = None
    
    def __str__(self):
        if self.h is None:
            if self.v is None:
                return "NONE"
            return f"{self.v}"
        else:
            if self.v is None:
                return f"{self.h}"
            return f"{self.h}-{self.v}"
    
    def __contains__(self, item):
        s = item.split("-", 2)
        if len(s) == 2:
            return self.h == s[0] and self.v == s[1]
        else:
            return self.h == item or self.v == item

    def flip(self):
        h_op = None
        v_op = None
        if self.h == "left":
            h_op = "right"
        elif self.h == "right":
            h_op = "left"
        if self.v == "up":
            v_op = "down"
        elif self.v == "down":
            v_op = "up"
        return Direction(h_op, v_op)

    @property
    def angle(self):
        d = str(self)
        a = None
        if d == "left":
            a = 180
        elif d == "left-up":
            a = 135
        elif d == "up":
            a = 90
        elif d == "right-up":
            a = 45
        elif d == "right":
            a = 0
        elif d == "right-down":
            a = 315
        elif d == "down":
            a = 270
        elif d == "left-down":
            a = 225
        else:
            return None
        return 2.0*math.pi*a/360.0

    def copy(self):
        return Direction(self.h, self.v)

    @staticmethod
    def from_angle(angle):
        d = ["right", "right-up", "up", "left-up", "left", "left-down", "down", "right-down"]
        for direction in d:
            direction = Direction(direction)
            if abs(direction.angle - angle) <= math.pi/8.:
                return direction
