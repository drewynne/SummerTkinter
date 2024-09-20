import random  # Unused import, consider removing if not used elsewhere
from Game_Components.Question_Types.Question import Question
from Game_Components.RoundRunner import RoundRunner
import logging

logging.basicConfig(level=logging.DEBUG)

class Game:
    """
    A class to represent a game that goes through multiple rounds of questions.

    Constants:
        ROUNDS_PER_GAME (int): Maximum number of rounds in a game, set to 3.
        MIN_START_DIFFICULTY (int): Minimum starting difficulty, set to 1.
        MAX_START_DIFFICULTY (int): Maximum starting difficulty, set to 10.
        EMPTY_STRING (str): Default empty string for user input validation.

    Attributes:
        round_number (int): The current round number.
        start_difficulty (int): The starting difficulty level for the game.
        round_runner (RoundRunner): An instance to handle rounds in the game.
        current_question (Question): The current question for the round.
    """
    # Constants:
    ROUNDS_PER_GAME: int = 3  # Somewhere between 3 and 10
    MIN_START_DIFFICULTY: int = 1
    MAX_START_DIFFICULTY: int = 10
    EMPTY_STRING = ""

    # Variables with type hints:
    round_number: int
    start_difficulty: int

    # Objects:
    round_runner: RoundRunner
    current_question: Question

    def __init__(self, start_difficulty: int):
        """ Game Constructor """
        # print("Starting game...\n")
        logging.debug("Starting Game")
        # Initialize Variables
        # Constrain Start Difficulty
        if start_difficulty < Game.MIN_START_DIFFICULTY or start_difficulty > Game.MAX_START_DIFFICULTY:
            self.start_difficulty = 5  # Middle of the Range
        else:
            self.start_difficulty = start_difficulty # Set the Start Difficulty

        self.round_number = 1  # Round number starts at 1

        # Initialize Objects
        self.round_runner = RoundRunner(self.start_difficulty) # Init Round Runner
        self.current_question = Question(self.start_difficulty) # Init Current Question




    def handle_user_response(self, user_answer: str) -> None:
        """Handles User Response"""
        
        logging.debug(f"Handling user response: {user_answer}")
        
        if user_answer == Game.EMPTY_STRING:  # Check if user has put answer in entry box
            logging.debug("User didn't enter an answer, skipping question.")

            is_correct_answer = False  # Set is_correct_answer to false if no answer has been given
        else:
            # 1st Call of next question
            is_correct_answer = self.fetch_next_question()  # Renamed variable for clarity

        self.round_runner.set_user_input(user_answer)  # Pass user input to round runner with the latest input from user

        # is_correct_answer = True
        self._log_answer_result(is_correct_answer)  # Extracted function for better readability


    def _log_answer_result(self, is_correct: bool) -> None:
        """Logs whether the user's answer was correct."""
        if is_correct:
            logging.debug('Correct Answer! Proceed to the next question.')
        else:
            logging.debug('Incorrect Answer. Try again.')

    def initiate_round(self) -> bool:
        """Start a new round of the game."""
        logging.debug(f"Initiating round {self.round_number}")
        if not self.rounds_within_range():  # too many rounds called
            self._end_game()  # End the game
            return False

        if self.round_runner.begin_round():  # Is the beginning of a round
            self._start_round()  # Start a round
            return True

        self._end_round()  # End round
        return False


    def _end_game(self):
        """Handle the end of the game when out of rounds."""
        # Add logic for saving game data
        logging.debug("Game is over, Out of Rounds!")


    def _start_round(self):
        """Handle the logic for starting a new round."""
        logging.debug("Round Starting in Game")
        self.round_number += 1  # Increment round number


    def _end_round(self):
        """Handle the logic for ending the current round."""
        logging.debug("Round Ending in Game")
        self.round_runner.end_round()  # Hand over to round runner

    def get_question_bundle(self) -> tuple:
        """ Gets Question bundle """
        return self.round_runner.get_question_bundle()  # Get question bundle from round runner

    def get_round_number(self) -> int:
        """ Returns the current round number """
        return self.round_number  # return the round number

    def rounds_within_range(self) -> bool:
        if self.round_number <= Game.ROUNDS_PER_GAME:
            logging.debug("Rounds within range")
            return True
        else:
            logging.debug(f"Rounds not within range, rounds reached {self.round_number}")
            return False

    @staticmethod
    def loving_it() -> bool:
        """ Check if user wants to continue the game """
        userIn = input("Press 1 to play a round, 0 to stop ")
        while userIn not in {"0", "1"}:  # Using set for faster membership testing
            logging.debug("Invalid input, please press 1 to play a round or 0 to stop.")
            userIn = input("Press 1 to play a round, 0 to stop ")
        return userIn == "1"

    def fetch_next_question(self) -> bool:

        """Fetches the next question for the current round using RoundRunner.

        This method delegates the task of fetching the next question
        to the round_runner instance associated with the game.

        Returns:
            bool: True if the next question was successfully fetched, False otherwise.
        """
        return self.round_runner.next_question()

    def end_of_round(self):
        """ End of round, resets the round variables """
        # Increment the Round Number
        self.round_number += 1  # Duplicated Code Here!!!
        # Do End of round Stuff...
        pass

    def end_of_game(self) -> bool:
        """ Check end of game """
        return not self.rounds_within_range()  # Basically the opposite of rounds within range

    def end_game(self):
        """ Save at End of Game """
        pass

    def check_answer(self, user_answer: str) -> bool:
        """ Checks if the user answer is correct """
        logging.debug("Checking Answer")

        try:
            return self.current_question.check_answer(user_answer)
        except Exception as e:
            logging.error("An error has occurred: %s",e)
            return False


if __name__ == '__main__':
    logging.debug("Testing Game\n")

    game = Game(10)  # Start game with start_difficulty 10
    game.initiate_round()