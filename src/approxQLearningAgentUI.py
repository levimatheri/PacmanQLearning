# author: Levi

import Tkinter as tk
from pacmanUI import Window
from pacmanEntry import PacmanEntry
import launchFunctions

class ApproximateQAgentWindow(Window):
    def __init__(self, title=None, height=None, width=None):
        super(ApproximateQAgentWindow, self).__init__(title, height, width)
    
    # Override Window setup()
    # master is the new window
    def setup(self, master):
        master.geometry(str(self.width) + 'x' + str(self.height))
        master.title(self.title)

        totalval = tk.StringVar()
        trainval = tk.StringVar()

        total_label = tk.Label(master, text="No. of games to play").grid(row=0)
        train_label = tk.Label(master, text="No. of training episodes").grid(row=1)
        layout_label = tk.Label(master, text="Layout").grid(row=2)

        vcmd = (master.register(self.validate),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        totalval.set("20")
        trainval.set("10")

        total_entry = PacmanEntry(20, master=master, textvariable=totalval, bd=3, validate='key', validatecommand=vcmd)
        train_entry = PacmanEntry(10, master=master, textvariable=trainval, bd=3, validate='key', validatecommand=vcmd)

        clearTotal = tk.Button(master, text="Clear", command=lambda: self.clear(totalval))
        clearTrain = tk.Button(master, text="Clear", command=lambda: self.clear(trainval))

        default_layout = tk.StringVar(master, value="mediumClassic")
        layout_entry = tk.OptionMenu(master, default_layout,
                        "smallGrid", "mediumGrid", "smallClassic", "mediumClassic", "trickyClassic", "openClassic", "trappedClassic", "capsuleClassic", "contestClassic", "originalClassic")

        layout_entry.pack()

        reset = tk.Button(master, text="Reset Defaults", command=lambda: self.reset_defaults([total_entry, totalval], [train_entry, trainval], layout=[layout_entry, default_layout]))
        reset.pack()

        start = tk.Button(master, text="START", command=lambda: launchFunctions.launchApproxQLearning(total_entry.get(), train_entry.get(), default_layout.get()))
        start.pack()


        total_entry.grid(row=0, column=1)
        clearTotal.grid(row=0, column=2)
        train_entry.grid(row=1, column=1)
        clearTrain.grid(row=1, column=2)
        layout_entry.grid(row=2, column=1)
        reset.grid(row=3, column=1)
        start.grid(row=4, column=1)
        

    def validate(self, action, index, value_if_allowed,
                 prior_value, text, validation_type, trigger_type, widget_name):        
        if text in '0123456789':
            try:
                if not value_if_allowed:
                    return True
                int(value_if_allowed)
                return True
            except ValueError:
                return False
        else:
            return False
    
    def reset_defaults(self, *entries, **kwargs):
        for key, val in kwargs.iteritems():
            if str(key) == "layout":
                val[1].set("mediumClassic")
        
        for entry in entries:
            # print entry[1].get()
            entry[1].set(str(entry[0].default_val))

    def clear(self, curr_val):
        curr_val.set("")