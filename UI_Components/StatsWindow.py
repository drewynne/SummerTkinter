from tkinter import *
from tkinter import ttk

from UI_Components.MyToplevel import MyToplevel


class StatsWindow(MyToplevel):
    """ Stats window class """

    # Constants:

    # Variables:

    # Objects:

    # UI Components:
    frame: ttk.Frame

    stats_label: ttk.Label  # Stats label
    operator_label: ttk.Label  # Operator Label
    level_label: ttk.Label  # Level Label

    addition_label: ttk.Label  # Addition Label
    addition_score_var: StringVar  # Addition Score Variable
    addition_score_label: ttk.Label  # Addition score label

    subtraction_label: ttk.Label  # Subtraction Label
    subtraction_score_var: StringVar  # Subtraction Score Variable
    subtraction_score_label: ttk.Label  # Subtraction score Label

    multiplication_label: ttk.Label  # Multiplication Label
    multiplication_score_var: StringVar  # Multiplication Score Variable
    multiplication_score_label: ttk.Label  # Multiplication score label

    division_label: ttk.Label  # Division Label
    division_score_var: StringVar  # Division Score Variable
    division_score_label: ttk.Label  # Division Score Label

    total_label: ttk.Label  # Total Label
    total_score_var: StringVar  # Total Score Variable
    total_score_label: ttk.Label  # Total Score Label

    advanced_stats_button: ttk.Button

    def __init__(self, main_window_root, title):
        """ Stats Window Constructor """
        super().__init__(main_window_root, title)
        # self.root.geometry("300x500+0+0")
        self.root.resizable(False, False)
        # Init UI Components
        self.frame = ttk.Frame(self.root, padding=10)

        self.stats_label = ttk.Label(self.frame, text="Stats:", font=self.custom_font)  # Stats label
        self.operator_label = ttk.Label(self.frame, text="Operator", font=self.custom_font)  # Operator Label
        self.level_label = ttk.Label(self.frame, text="Level", font=self.custom_font)   # Level Label

        self.addition_label = ttk.Label(self.frame, text="Addition", font=self.custom_font)  # Addition Label
        self.addition_score_var = StringVar(value="172")  # Addition Score Variable
        self.addition_score_label = ttk.Label(self.frame,
                                              textvariable=self.addition_score_var,
                                              font=self.custom_font)   # Addition score label

        self.subtraction_label = ttk.Label(self.frame,
                                           text="Subtraction",
                                           font=self.custom_font)   # Subtraction Label
        self.subtraction_score_var = StringVar(value="75")  # Subtraction Score Variable
        # Subtraction score Label
        self.subtraction_score_label = ttk.Label(self.frame,
                                                 textvariable=self.subtraction_score_var,
                                                 font=self.custom_font)

        self.multiplication_label = ttk.Label(self.frame,
                                              text="Multiplication",
                                              font=self.custom_font)   # Multiplication Label
        self.multiplication_score_var = StringVar(value="38")  # Multiplication Score Variable
        # Multiplication score label
        self.multiplication_score_label = ttk.Label(self.frame,
                                                    textvariable=self.multiplication_score_var,
                                                    font=self.custom_font)

        self.division_label = ttk.Label(self.frame,
                                        text="Division",
                                        font=self.custom_font)   # Division Label
        self.division_score_var = StringVar(value="12")  # Division Score Variable
        self.division_score_label = ttk.Label(self.frame,
                                              textvariable=self.division_score_var,
                                              font=self.custom_font)  # Division Score Label

        self.total_label = ttk.Label(self.frame,
                                     text="Total",
                                     font=self.custom_font)   # Total Label
        self.total_score_var = StringVar(value="297")  # Total Score Variable
        self.total_score_label = ttk.Label(self.frame,
                                           textvariable=self.total_score_var,
                                           font=self.custom_font)   # Total Score Label
        self.advanced_stats_button = ttk.Button(self.frame,
                                                text="Advanced Stats",
                                                command=self.on_press_advanced_stats_button)


        # Pack To Grid
        self.frame.grid()
        self.stats_label.grid(column=0, row=0, ipadx=10, ipady=10)
        self.operator_label.grid(column=0, row=1, ipadx=10, ipady=10)
        self.level_label.grid(column=1, row=1, ipadx=10, ipady=10)

        self.addition_label.grid(column=0, row=2, ipadx=10, ipady=10)
        self.addition_score_label.grid(column=1, row=2, ipadx=10, ipady=10)

        self.subtraction_label.grid(column=0, row=3, ipadx=10, ipady=10)
        self.subtraction_score_label.grid(column=1, row=3, ipadx=10, ipady=10)

        self.multiplication_label.grid(column=0, row=4, ipadx=10, ipady=10)
        self.multiplication_score_label.grid(column=1, row=4, ipadx=10, ipady=10)

        self.division_label.grid(column=0, row=5, ipadx=10, ipady=10)
        self.division_score_label.grid(column=1, row=5, ipadx=10, ipady=10)

        self.total_label.grid(column=0, row=6, ipadx=10, ipady=10)
        self.total_score_label.grid(column=1, row=6, ipadx=10, ipady=10)

        self.advanced_stats_button.grid(column=0, row=7, ipadx=10, ipady=10)

    def on_press_advanced_stats_button(self):
        """ Expand to advanced stats """
        pass

if __name__ == '__main__':
    print("Testing Stats Window")
    print()

    root = Tk()
    stats_window = StatsWindow(root, "Summer Stats Window")
    stats_window.display()
