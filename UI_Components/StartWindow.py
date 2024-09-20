# Test GUI Class
# By Drew Wynne
# Commenced 14/06/2024

# To Do:
# Add Start Button
# Add Question Text
# Add
# Link to Game Later

from tkinter import *
from tkinter import ttk

import logging

from UI_Components.GameWindow import GameWindow
from UI_Components.MyWindow import MyWindow
from UI_Components.StatsWindow import StatsWindow

logging.basicConfig(level=logging.DEBUG)

class StartWindow(MyWindow):
    """
    StartWindow is a subclass of MyWindow that represents the initial window of the application. It includes a variety of UI components and handles user interactions.

    Constants:

    Variables:

    Objects:

    UI Components:
    - outer_frame: Outer Frame (ttk.Frame)
    - start_button: Start Button (ttk.Button)
    - show_stats_var: Show Stats Variable (BooleanVar)
    - show_stats: Show stats check button (ttk.Checkbutton)
    - difficulty_selector_label: Difficulty Selector Text Label (ttk.Label)
    - difficulty_selector_inp: Difficulty selector spin box (ttk.Spinbox)
    - difficulty_selector_var: Value of Difficulty Selector (IntVar)
    - round_number_label: Round Number Label (ttk.Label)
    - round_number_var: Round Number String Variable (StringVar)
    - stats_button: Stats Button (ttk.Button)
    """
    # Constants:

    # Variables:

    # Objects:

    # UI Components:
    outer_frame: ttk.Frame  # Outer Frame
    start_button: ttk.Button  # Start Button
    show_stats_var: BooleanVar  # Show Stats Variable (Boolean)
    show_stats: ttk.Checkbutton  # show stats check button
    difficulty_selector_label: ttk.Label  # Difficulty Selector Text Label
    difficulty_selector_inp: ttk.Spinbox  # Difficulty selector spin box
    difficulty_selector_var: IntVar  # Value of Difficulty Selector
    round_number_label: ttk.Label  # Round Number Label
    round_number_var: StringVar  # Round Number String Variable
    stats_button: ttk.Button

    def __init__(self):  #
        """ Start Window Constructor """
        super().__init__('Summer')
        # self.root.geometry("300x500+0+0")  # Small Window
        # Init Variables

        # Init Objects:

        # Init UI Components:
        # Root
        self.root.resizable(False, False)
        self.root.protocol("WM_DELETE_WINDOW", self.on_end_game)  # Set Action on Exit
        self.style.map('StartFrame.TFrame', foreground=[('active', 'cyan')])
        self.outer_frame = ttk.Frame(self.root, padding=10, style='StartFrame.TFrame')  # Outer Frame
        # Difficulty Selector
        self.difficulty_selector_var = IntVar(value=5)  # Set Default Value for difficulty selector
        self.difficulty_selector_label = ttk.Label(self.outer_frame,
                                                   text="Select Difficulty (1 to 10)",
                                                   font=self.custom_font)
        self.difficulty_selector_inp = ttk.Spinbox(self.outer_frame, from_=1, to=10, width=5,
                                                   textvariable=self.difficulty_selector_var,
                                                   font=self.custom_font)
        self.show_stats_var = BooleanVar(value=True)
        self.show_stats = ttk.Checkbutton(self.outer_frame,
                                          text="Show Stats While Playing",
                                          )  # Show Stats While Playing
        self.show_stats.config(variable=self.show_stats_var)
        # Start Button
        self.start_button = ttk.Button(self.outer_frame,
                                       text="Start",
                                       command=self.on_press_start,
                                       style='Regular.TButton')
        self.round_number_var = StringVar(value="Round 1")  # Set Default Value for Round Number Text
        self.round_number_label = ttk.Label(self.outer_frame,
                                            textvariable=self.round_number_var,
                                            font=self.custom_font)  #
        self.stats_button = ttk.Button(self.outer_frame,
                                       text="Open Stats",
                                       command=self.on_press_open_stats,
                                       style='Regular.TButton')

        # Pack UI Components to Grid:
        self.outer_frame.pack(side='top', fill='both', expand=True)  # Pack Outer Frame to Grid
        # Pack difficulty Selector Label to Grid
        self.difficulty_selector_label.grid(column=0, row=0,  sticky="EW", ipadx=5, ipady=5)
        # Pack difficulty Selector spinbox to Grid
        self.difficulty_selector_inp.grid(column=0, row=1,  sticky="EW", ipadx=5, ipady=5)
        # Pack Show Stats Checkbox to Grid
        self.show_stats.grid(column=0, row=2, sticky="EW", ipadx=5, ipady=5)
        self.start_button.grid(column=0, row=3, sticky="EW", ipadx=5, ipady=5)  # Pack Start Button to Grid
        # Pack Round Number Label to Grid
        self.round_number_label.grid(column=0, row=4, sticky="EW", ipadx=5, ipady=5)
        self.stats_button.grid(column=0, row=5, sticky="EW", ipadx=5, ipady=5)


    def on_press_start(self):
        """ When Start Button is Pressed """
        logging.debug("Start Button Pressed")

        self.open_game_window()

    def on_press_open_stats(self):
        """ When Stats Button is Pressed """
        logging.debug("Stats Button Pressed")
        self.open_stats_window()

    def open_game_window(self):
        """ Opens Game Window """
        game_window = GameWindow(self.root, "Summer Game Window")
        game_window.display()

    def open_stats_window(self):
        """ Opens Stats Window """
        stats_window = StatsWindow(self.root, "Summer Stats Window")
        stats_window.display()

    def on_end_game(self):
        """ When Exit Button is Pressed """
        logging.debug("Exit Button Pressed")
        logging.debug("Game Window Closed")
        logging.debug("Saving Data...")
        # Save All Data
        # TODO: Save Data
        # Close All Windows
        self.root.destroy()


if __name__ == '__main__':  # Test Code
    logging.debug("Testing Start Window")

    start_window = StartWindow()
    start_window.display()
