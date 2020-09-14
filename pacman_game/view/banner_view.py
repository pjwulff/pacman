from gi.repository import Gtk
from gi.repository import Gdk
import pkg_resources

class BannerView(Gtk.DrawingArea):
    def __init__(self, message, next, score = None, **kwargs):
        super().__init__(**kwargs)
        self.set_size_request(240, 384)
        self.set_visible(True)
        self.add_events(Gdk.EventMask.BUTTON_PRESS_MASK)
        self._message = message
        self._score = score
        self._next = next
        self.connect("draw", self.draw)
        self.connect("button-press-event", self.button_press_event)
    
    def draw(self, widget, cr):
        self._width = self.get_allocated_width()
        self._height = self.get_allocated_height()
        cr.set_font_size(48)
        (_, _, self._text_width, self._text_height, _, _) = cr.text_extents(self._message)
        self._top_left_x = self._width/2 - self._text_width/2 - 12
        self._top_left_y = self._height/3 - self._text_height/2 - 12
        self._bottom_right_x = self._width/2 + self._text_width/2 + 12
        self._bottom_right_y = self._height/3 + self._text_height/2 + 12
        cr.save()
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
        cr.show_text(self._message)
        cr.restore()
    
    def button_press_event(self, widget, event):
        x = event.x
        y = event.y
        if self._top_left_x <= x <= self._bottom_right_x and \
           self._top_left_y <= y <= self._bottom_right_y:
            self._next()

    def _display_score(self, screen, score):
        lst = self._list_numbers(score)
        length = len(lst)
        digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-"]
        digits = [pygame.image.load(f"data/{s}.png").convert() for s in digits]
        x = 336 - 24*length//2
        y = 336
        for digit in lst:
            if digit == "-":
                image = digits[10]
            else:
                image = digits[digit]
            rect = image.get_rect().move(x, y)
            self._screen.blit(image, rect)
            x += 24

    def _list_numbers(self, num):
        neg = False
        if num < 0:
            neg = True
            num = -num
        lst = [num % 10]
        num = num // 10
        while num > 0:
            lst = [(num % 10)] + lst
            num = num // 10
        if neg:
            lst = ["-"] + lst
        return lst
