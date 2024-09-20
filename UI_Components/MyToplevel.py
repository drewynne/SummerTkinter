from tkinter import *
from tkinter import ttk, font

from UI_Components.Utility import Utility


class MyToplevel:
    """ My Toplevel Class """
    # Constants:

    # Variables:

    # Objects:

    # UI Components:
    root: Toplevel
    style: ttk.Style
    custom_font: font.Font

    def __init__(self, main_window_root, title):
        """ My Toplevel Constructor """
        self.root = Toplevel(main_window_root)
        self.style = ttk.Style()
        self.custom_font = font.Font(family='Helvetica', size=12, weight='bold')
        self.root.title(title)
        Utility.set_my_style()

    def display(self):
        """ Display Function """
        self.root.mainloop()


if __name__ == '__main__':
    print("Testing My Toplevel")
    print()

    root = Tk()
    root.title("Test Root")
    my_toplevel = MyToplevel(root, "Test Top Level")
    my_toplevel.display()
