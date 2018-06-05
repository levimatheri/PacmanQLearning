import Tkinter as tk 

class PacmanEntry(tk.Entry, object):
    def __init__(self, default_val, **kwargs):
        super(PacmanEntry, self).__init__(**kwargs)
        self.default_val = default_val