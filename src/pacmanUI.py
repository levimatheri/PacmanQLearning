from Tkinter import Toplevel

class Window(object):
    t = None
    def __init__(self, title=None, width=None, height=None):
        if width == None:
            width = 500
        if height == None:
            height = 500
        if title == None:
            title = "Pacman AI"

        self.title = title
        self.width = width
        self.height = height

    def setup(self, root):
        pass
    def openWindow(self):
        t = Toplevel()      
        self.setup(t)