class ArenaView:
    def __init__(self, arena):
        self._arena = arena
        self._rect = arena.rect
    
    @property
    def rect(self):
        return self._rect
    
    def draw(self, cr):
        width = self.rect.width
        height = self.rect.height
        cr.set_source_rgb(0, 0, 0)
        cr.paint()
        cr.set_source_rgb(0.0, 0.0, 1.0)
        cr.set_line_width(2.0)
        cr.move_to(24, 96)
        cr.line_to(width-24, 96)
        cr.line_to(width-24, height-24)
        cr.line_to(24, height-24)
        cr.line_to(24, 96)
        cr.stroke()
