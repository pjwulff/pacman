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
                return ""
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
