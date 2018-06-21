# author: Levi Muriuki

import Tkinter as tk 
from pacmanUI import Window
from pacmanEntry import PacmanEntry
import launchFunctions

class ChooseLayoutKeyboard(Window):
    def __init__(self, title, width, height):
        super(ChooseLayoutKeyboard, self).__init__(title, width, height)

    def setup(self, master):
        totalval = tk.StringVar()

        vcmd = (master.register(self.validate),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        totalval.set("10")
        total_label = tk.Label(master, text="No. of games to play").grid(row=0)
        total_entry = PacmanEntry(20, master=master, textvariable=totalval, bd=3, validate='all', validatecommand=vcmd)

        layout_label = tk.Label(master, text="Layout").grid(row=2)

        default_layout = tk.StringVar(master, value="smallGrid")
        layout_entry = tk.OptionMenu(master, default_layout,
                    "smallGrid", "mediumGrid", "smallClassic", "mediumClassic", "trickyClassic", "openClassic", "trappedClassic", "capsuleClassic", "contestClassic", "originalClassic")

        start = tk.Button(master, text="START", command=lambda: launchFunctions.launchKeyboard(total_entry.get(), default_layout.get()))
        start.pack()

        clearTotal = tk.Button(master, text="Clear", command=lambda: self.clear(totalval))

        total_entry.grid(row=0, column=1)
        clearTotal.grid(row=0, column=2)
        layout_entry.grid(row=2, column=1)
        start.grid(row=3, column=1)
        
    def validate(self, action, index, value_if_allowed,
                 prior_value, text, validation_type, trigger_type, widget_name):    
        if text in '0123456789' or '':
            try:               
                if not value_if_allowed:
                    return True
                int(value_if_allowed)
                return True
            except ValueError:
                return False
        else:
            return False

    def clear(self, curr_val):
        curr_val.set("")