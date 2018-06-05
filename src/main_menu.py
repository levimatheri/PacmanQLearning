# author: Levi

import Tkinter as tk
from chooseQ import ChooseQ
import launchFunctions as lf

top = tk.Tk()
top.title("Pacman AI Main menu")

# Label text
choose = tk.StringVar()
# Set label
choose.set("Choose a playing agent")

top_menu = tk.Label(top, textvariable=choose)
top_menu.pack()

# Set up buttons with onClick commands
keyboardAgentButton = tk.Button(top, text="Keyboard Agent", command=lf.launchKeyboard)
keyboardAgentButton.pack()

q = ChooseQ("Q Learning Agent", 300, 300)
qLearningButton = tk.Button(top, text="Q Learning Agent", command=lambda: q.openWindow())
qLearningButton.pack()

# Resize window
top.geometry("300x200")
top.mainloop()