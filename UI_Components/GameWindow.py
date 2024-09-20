import logging
import time
from tkinter import *
from tkinter import ttk, messagebox
from venv import logger

from Game_Components.Game import Game
from UI_Components.MyToplevel import MyToplevel

logging.basicConfig(level=logging.DEBUG)


class GameWindow(MyToplevel):
    """

    class GameWindow
        A class representing the game window, providing the primary interface for the game.

        Constants:
            MAX_QUESTIONS (int): Maximum number of questions per round.
            TOO_MANY_QUESTIONS (int): Threshold for excessive number of questions.

        Methods:
            __init__(self, main_window_root, title)
                Initialize the game window.

            _initialize_ui(self)
                Initialize the user interface components.

            _pack_ui(self)
                Pack the initialized UI components into their respective frames.

            on_end_round(self)
                Handle the End Round button press event.

            on_submit(self)
                Handle the Submit button press event.

            on_enter_press(self, event)
                Handle the pressing of the Enter key.

            _initial_submit_behaviour(self)
                Handle the first submit click behavior of the game.

            _subsequent_submit_behaviour(self)
                Handle subsequent submit clicks during a round.

            _update_ui_for_question(self, question_bundle)
                Update UI elements based on the current question.

            _show_notification(self, title, message, duration)
                Display a toast notification with a custom message.
    """
    MAX_QUESTIONS = 10
    TOO_MANY_QUESTIONS = 11

    def __init__(self, main_window_root, title):
        """ Game Window Constructor """
        super().__init__(main_window_root, title)  # Overload Super Constructor
        self.root.geometry("1920x1080+0+0")  # Uses up full Laptop Screen
        logging.debug("Starting Game Window...")

        # Init Variables
        self.already_playing = False
        self.round_number = 0
        self.user_answer = ""
        self.this_answer_text = ""
        # Initialize Game
        self.summer = Game(5)

        # Initialize GUI Components
        self._initialize_ui()

    def _initialize_ui(self):
        """ Initialize the User Interface components """
        logging.debug("Initializing UI Components...")
        self.outer_frame = ttk.Frame(self.root, padding=10)
        self.outer_frame.pack(side='top', fill='both', expand=True)

        self.top_frame = ttk.Frame(self.outer_frame, padding=10)
        self.centered_frame = ttk.Frame(self.outer_frame, padding=10)

        self.end_round_button = ttk.Button(
            self.top_frame, text="End Round", command=self.on_end_round, style='Regular.TButton')

        self.question_number_text_var = StringVar(value="Question _ of 10")
        self.question_number_text_label = ttk.Label(
            self.top_frame, textvariable=self.question_number_text_var, font=self.custom_font)

        self.round_number_text_var = StringVar(value="Round _")
        self.round_number_text_label = ttk.Label(
            self.top_frame, textvariable=self.round_number_text_var, font=self.custom_font)

        self.question_text_var = StringVar(value="Press Submit")
        self.question_text_label = ttk.Label(
            self.centered_frame, textvariable=self.question_text_var, font=self.custom_font)

        self.answer_text_var = StringVar(value="Answer")
        self.answer_text_entry = ttk.Entry(
            self.centered_frame, textvariable=self.answer_text_var, font=self.custom_font)

        self.submit_button = ttk.Button(
            self.centered_frame, text="Submit", command=self.on_submit, style='Accent.TButton')
        self.root.bind('<Return>', self.on_enter_press)
        # Pack UI Components
        self._pack_ui()

    def _pack_ui(self):
        """ Pack the initialized UI components into the frames """
        self.top_frame.grid(column=0, row=0, sticky="EW")
        self.centered_frame.place(in_=self.outer_frame, relx=0.5, rely=0.5, anchor='center')

        self.end_round_button.grid(column=0, row=0, ipadx=10, ipady=10)
        self.question_number_text_label.grid(column=1, row=0, ipadx=10, ipady=10)
        self.round_number_text_label.grid(column=2, row=0, ipadx=10, ipady=10)
        self.question_text_label.grid(column=0, row=0, ipadx=10, ipady=10)
        self.answer_text_entry.grid(column=0, row=1, ipadx=10, ipady=10)
        self.submit_button.grid(column=1, row=1, ipadx=10, ipady=10)

    def on_end_round(self):
        """ Handle End Round button press """
        logger.debug("End Round Button Pressed")
        logging.debug("Ending Round")
        self.root.destroy()

    def on_submit(self):
        """ Handle Submit button press """
        logging.debug("Submit Button Pressed.")
        self.answer_text_entry.focus()

        if not self.already_playing:
            self._initial_submit_behaviour()
        else:
            self._subsequent_submit_behaviour()

        self.round_number = self.summer.get_round_number()
        self.user_answer = self.answer_text_entry.get()
        logging.debug(f"User Answer: {self.user_answer}\n")

        self.answer_text_var.set("")

    def on_enter_press(self, event):
        self.on_submit()

    def _initial_submit_behaviour(self):
        """ Handle the first submit click behavior """
        logging.debug("Initial Submit Behaviour")
        self.question_text_var.set(f"Press Submit to Begin Round {self.round_number}")
        self.question_number_text_var.set("Question _ of 10")
        self.answer_text_var.set("")
        self.summer.handle_user_response("")
        if self.summer.initiate_round():
            logging.debug("New Round is Starting...")

        else:
            logging.debug("Round is Out of Range!")

            self.question_text_var.set("Start of Game...")
            self.root.quit()

        # self.summer.handle_user_response(self.user_answer)
        self.already_playing = True




    def _subsequent_submit_behaviour(self):
        """ Handle subsequent submit clicks during a round """
        logging.debug("Subsequent Submit Behaviour")

        question_bundle = self.summer.get_question_bundle()
        logging.debug("Getting Question Bundle:")
        question_number = question_bundle[0]
        if question_number < self.MAX_QUESTIONS:
            self.question_text_var.set(question_bundle[1])
            self.user_answer = self.answer_text_entry.get()
            self.summer.handle_user_response(self.user_answer)
        else:
            self.summer.end_of_round()
            question_bundle = (self.MAX_QUESTIONS, "Question Out of Range", "Answer = Pi")


        if question_number >= self.MAX_QUESTIONS:
            if question_number == self.TOO_MANY_QUESTIONS:
                logging.debug("Too Many Questions in round")
                question_number = 0
            if self.summer.end_of_game():
                self.already_playing = False
                self.summer.end_game()
        else:
            self._update_ui_for_question(question_bundle)
            # time.sleep(1)
            self.answer_text_var.set("")
            self.answer_text_entry.focus()
        # Check answer AFTER question has been asked
        if self.summer.check_answer(self.user_answer):
            self._show_notification("Correct Answer!", "Correct Answer!", 500)
        else:
            correct_answer_text = question_bundle[2]
            self._show_notification("Incorrect Answer!", f"Incorrect! the answer was: {correct_answer_text}"
                                    ,
                                    2000)
            logging.debug("Incorrect Answer!")

        # self._update_ui_for_question(question_bundle)


    def _update_ui_for_question(self, question_bundle):
        """ Update UI elements based on the current question """
        question_number, question_text, answer_text = question_bundle
        self.question_number_text_var.set(f"Question {question_number} of 10")
        self.question_text_var.set(question_text)
        self.round_number_text_var.set(f"Round {self.round_number}")
        self.this_answer_text = answer_text
        logging.debug(f"Answer Text: {answer_text}")

    def _show_notification(self, title, message, duration):
        """ Show a toast notification with a custom dialog """
        # Create a Toplevel window
        toast = Toplevel(self.root)
        toast.title(title)
        toast.geometry("300x100")

        # Add a Label with the message
        Label(toast, text=message).pack(expand=True)

        # Automatically close the toast after the specified duration
        toast.after(duration, toast.destroy)


if __name__ == '__main__':
    print("Testing Game Window\n")
    root = Tk()
    game_window = GameWindow(root, "Summer Game Window")
    game_window.display()