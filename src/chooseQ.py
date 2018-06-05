# author: Levi

import Tkinter as tk 

from pacmanUI import Window
from approxQLearningAgentUI import ApproximateQAgentWindow as Aqw
from qLearningAgentUI import QAgentWindow as Nqw

class ChooseQ(Window):
    def __init__(self, title, width, height):
        super(ChooseQ, self).__init__(title, width, height)

    def setup(self, master):
        choose_label = tk.Label(master, text="Choose type of Q learning\n\n")
        choose_label.pack()

        normalQBtn = tk.Button(master, text="Normal Q Learning", command=self.toNormalQWindow)
        normalQBtn.pack()

        approxQBtn = tk.Button(master, text="Approximate Q Learning", command=self.toApproxQWindow)
        approxQBtn.pack()

    def toNormalQWindow(self):
        nq = Nqw("Normal Q Learning", 300, 300)
        nq.openWindow()
    def toApproxQWindow(self):
        aq = Aqw("Approximate Q Learning", 300, 300)
        aq.openWindow()