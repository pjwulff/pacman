from gi.repository import Gtk

class ToggleGroup(Gtk.ButtonBox):
    def __init__(self, a, b, c, **kwargs):
        super().__init__(**kwargs)
        self._button_a = Gtk.ToggleButton.new_with_label(a)
        self._button_a.set_visible(True)
        self._button_a.connect("button-press-event", self._on_click)
        self._button_a.set_active(True)
        self._button_b = Gtk.ToggleButton.new_with_label(b)
        self._button_b.set_visible(True)
        self._button_b.connect("button-press-event", self._on_click)
        self._button_c = Gtk.ToggleButton.new_with_label(c)
        self._button_c.set_visible(True)
        self._button_c.connect("button-press-event", self._on_click)
        self.add(self._button_a)
        self.add(self._button_b)
        self.add(self._button_c)
        self.set_layout(Gtk.ButtonBoxStyle.EXPAND)
        self.set_visible(True)
    
    def _on_click(self, widget, event):
        self._button_a.set_active(False)
        self._button_b.set_active(False)
        self._button_c.set_active(False)
    
    def disable(self):
        self._button_a.set_sensitive(False)
        self._button_b.set_sensitive(False)
        self._button_c.set_sensitive(False)
    
    def enable(self):
        self._button_a.set_sensitive(True)
        self._button_b.set_sensitive(True)
        self._button_c.set_sensitive(True)
    
    @property
    def selection(self):
        if self._button_a.get_active():
            return 0
        elif self._button_b.get_active():
            return 1
        elif self._button_c.get_active():
            return 2

class PopoverMenu(Gtk.PopoverMenu):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._difficulty_box = ToggleGroup("Easy", "Medium", "Hard")
        self._shape_box = ToggleGroup("Rectangular", "Hexagonal", "Graph")
        self._box = Gtk.Box()
        self._box.set_orientation(Gtk.Orientation.VERTICAL)
        self._box.add(self._difficulty_box)
        self._box.add(self._shape_box)
        self._box.set_visible(True)
        self.add(self._box)
    
    def disable(self):
        self._difficulty_box.disable()
        self._shape_box.disable()
    
    def enable(self):
        self._difficulty_box.enable()
        self._shape_box.enable()
        
    @property
    def difficulty(self):
        lst = ["easy", "medium", "hard"]
        return lst[self._difficulty_box.selection]
        
    @property
    def shape(self):
        lst = ["rectangular", "hexagonal", "graph"]
        return lst[self._shape_box.selection]
