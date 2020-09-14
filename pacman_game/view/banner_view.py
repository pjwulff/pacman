from gi.repository import Gtk
from gi.repository import Gdk
import pkg_resources

class BannerView(Gtk.DrawingArea):
    def __init__(self, next, score = None, **kwargs):
        super().__init__(**kwargs)
        self.set_size_request(240, 384)
        self.set_visible(True)
        self.add_events(Gdk.EventMask.BUTTON_PRESS_MASK)
        self._score = score
        self._next = next
        self.connect("draw", self.draw)
        self.connect("button-press-event", self.button_press_event)
    
    def draw(self, widget, cr):
        self._width = self.get_allocated_width()
        self._height = self.get_allocated_height()
        cr.set_font_size(48)
        (_, _, self._text_width, self._text_height, _, _) = cr.text_extents("START")
        self._top_left_x = self._width/2 - self._text_width/2 - 12
        self._top_left_y = self._height/3 - self._text_height/2 - 12
        self._bottom_right_x = self._width/2 + self._text_width/2 + 12
        self._bottom_right_y = self._height/3 + self._text_height/2 + 12
        cr.set_source_rgb(0, 0, 0)
        cr.paint()
        cr.set_source_rgb(1.0, 1.0, 1.0)
        cr.set_line_width(2.0)
        cr.move_to(self._top_left_x, self._top_left_y)
        cr.line_to(self._top_left_x, self._bottom_right_y)
        cr.line_to(self._bottom_right_x, self._bottom_right_y)
        cr.line_to(self._bottom_right_x, self._top_left_y)
        cr.close_path()
        cr.stroke()
        cr.move_to(self._width/2 - self._text_width/2, self._height/3 + self._text_height/2)
        cr.show_text("START")
        if self._score is not None:
            cr.set_font_size(24)
            (_, _, w, h, _, _) = cr.text_extents(str(self._score))
            cr.move_to((self._width - w) / 2, self._height/2+h)
            cr.show_text(str(self._score))
    
    def button_press_event(self, widget, event):
        x = event.x
        y = event.y
        if self._top_left_x <= x <= self._bottom_right_x and \
           self._top_left_y <= y <= self._bottom_right_y:
            self._next()
