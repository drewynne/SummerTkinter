import random  # Unused import, consider removing if not used elsewhere
from Game_Components.Question_Types.Question import Question
from Game_Components.RoundRunner import RoundRunner


class Game:
    """ Game Class """
    # Constants:
    ROUNDS_PER_GAME: int = 3  # Somewhere between 3 and 10
    MIN_START_DIFFICULTY: int = 1
    MAX_START_DIFFICULTY: int = 10

    # Variables with type hints:
    round_number: int
    start_difficulty: int

    # Objects:
    round_runner: RoundRunner
    current_question: Question

    def __init__(self, start_difficulty: int):
        """ Game Constructor """
        print("Starting game...\n")

        # Initialize Variables
        # Constrain Start Difficulty
        if start_difficulty < Game.MIN_START_DIFFICULTY or start_difficulty > Game.MAX_START_DIFFICULTY:
            self.start_difficulty = 5  # Middle of the Range
        else:
            self.start_difficulty = start_difficulty

        self.round_number = 1  # Round number starts at 1

        # Initialize Objects
        self.round_runner = RoundRunner(self.start_difficulty)
        self.current_question = Question(self.start_difficulty)

    def handle_user_response(self, user_answer: str) -> None:
        """ Handles User Response """
        # Big Ticket Item!!!
        self.round_runner.set_user_input(user_answer)
        response = self.round_runner.next_question()
        if response:
            print('Correct Answer! Proceed to the next question.')
        else:
            print('Incorrect Answer. Try again.')


    def start_a_round(self) -> bool:
        """ Play the game """
        if not self.rounds_within_range():  # Out of rounds
            print("Game is over, Out of Rounds!")
            return False
        else:  # Round Number Within Range
            if self.round_runner.start_of_round():  # Rounds Left to Play
                print("Round Starting in Game")
                self.round_number += 1  # Increment round number
                return True
            else:
                print("Round Ending in Game")
                self.round_runner.end_round()
                return False

    def get_question_bundle(self) -> tuple:
        """ Gets Question bundle """
        return self.round_runner.get_question_bundle()

    def get_round_number(self) -> int:
        """ Returns the current round number """
        return self.round_number

    def rounds_within_range(self) -> bool:
        if self.round_number <= Game.ROUNDS_PER_GAME:
            print("Rounds within range")
            return True
        else:
            print(f"Rounds not within range, rounds reached {self.round_number}")
            return False

    @staticmethod
    def loving_it() -> bool:
        """ Check if user wants to continue the game """
        userIn = input("Press 1 to play a round, 0 to stop ")
        while userIn not in {"0", "1"}:  # Using set for faster membership testing
            print("Invalid input, please press 1 to play a round or 0 to stop.")
            userIn = input("Press 1 to play a round, 0 to stop ")
        return userIn == "1"

    def next_question(self):
        """ Requests the next question """
        return self.round_runner.next_question()

    def end_of_round(self):
        """ End of round, resets the round variables """
        # Increment the Round Number
        self.round_number += 1
        # Do End of round Stuff...
        pass

    def end_of_game(self) -> bool:
        """ Check end of game """
        return not self.rounds_within_range()  # Basically the opposite of rounds within range

    def end_game(self):
        """ Save at End of Game """
        pass

    def check_answer(self, user_answer: str) -> None:
        """ Checks if the user answer is correct """
        self.current_question.check_answer(user_answer)


if __name__ == '__main__':
    print("Testing Game\n")
    game = Game(10)  # Start game with start_difficulty 10
    game.start_a_round()