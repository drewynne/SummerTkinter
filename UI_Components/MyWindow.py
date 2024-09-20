from tkinter import *
from tkinter import ttk, font

from UI_Components.Utility import Utility


class MyWindow:
    """ My Window Class """
    # Constants:

    # Variables:

    # Objects:

    # UI Components:
    root: Tk
    style: ttk.Style
    custom_font: font.Font

    def __init__(self, title):
        """ My window Object Constructor """
        self.root = Tk()
        self.style = ttk.Style()
        self.custom_font = font.Font(family='Helvetica', size=12, weight='bold')
        self.root.title(title)
        Utility.set_my_style()

    def display(self):
        """ Display Function """
        self.root.mainloop()


if __name__ == '__main__':  # Test Code
    print("Testing my window")

    my_window = MyWindow("Test Window")
    my_window.display()
