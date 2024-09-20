import logging
import time
from Game_Components.QuestionAsker2 import QuestionAsker2
from Game_Components.Difficulty import Difficulty

logging.basicConfig(level=logging.DEBUG)

class RoundRunner:
    """
    Class RoundRunner is responsible for managing a single round of the game.

    Attributes:
        QUESTIONS_PER_ROUND (int): Number of questions per round, default is 10.

    Methods:
        __init__(start_difficulty: int):
            Initializes the RoundRunner object with the specified starting difficulty.

        begin_round() -> bool:
            Initializes and starts the round.

        _initialize_round() -> None:
            Helper method to initialize the round.

        next_question_or_end_round() -> bool:
            Checks the availability of the next question or ends the round if no more questions are available.

        measure_answer_time():
            Measures the time taken for the user to answer a question and adjusts the difficulty accordingly.

        get_question_bundle():
            Retrieves the current question bundle, including question number, text, and answer.

        end_round():
            Forces the current round to end.

        next_question() -> bool:
            Updates to the next question and checks if the current answer is correct.

        set_user_input(user_input: str):
            Sets the user input for the current question.
    """
    # (Runs one Round)

    # Constants
    QUESTIONS_PER_ROUND: int = 10

    # Initializing the class
    def __init__(self, start_difficulty: int):
        """Round Runner Object Constructor"""
        logging.debug("RoundRunner Constructor")
        self.user_input = ""  # Init blank user input
        self.question_asker = QuestionAsker2(start_difficulty)  # Init Question Asker with Start Difficulty
        # Init Difficulty Class (with start difficulty (two different variables))
        self.difficulty = Difficulty(start_difficulty)
        # Set start difficulty for difficulty class
        self.difficulty.set_start_difficulty(start_difficulty)
        self.question_number = 0
        self.question_text = ""
        self.answer_text = ""

    def begin_round(self) -> bool:
        """Initialize and Start the Round."""
        logging.debug("Begin Round")
        self._initialize_round()
        return self.next_question_or_end_round()


    def _initialize_round(self) -> None:
        """Helper method to initialize the round."""
        logging.debug("Initializing Round")
        self.question_number += 1


    def next_question_or_end_round(self) -> bool:
        """Check the next question or end the round if not available."""
        if self.next_question():
            logging.debug("Next Question Available")
            return True
        self.end_round()
        return False

    def measure_answer_time(self):
        # self.question_asker.set_difficulty(5)
        start_time = time.time()
        is_correct = True
        elapsed_time = time.time() - start_time
        if not is_correct:  # User Made a Mistake
            elapsed_time += 1.0
            # time.sleep(4)
        q_type = self.question_asker.get_q_type()
        self.difficulty.set_difficulty(q_type, elapsed_time)
        # print(elapsed_time)

    # TODO: Replace with actual functionality from next_question function
    def get_question_bundle(self):
        """Gets a full bundle"""
        self.question_number += 1
        logging.debug(f"Question Number: {self.question_number}")
        if self.question_number > RoundRunner.QUESTIONS_PER_ROUND:
            self.question_number = 1
        self.question_text = self.question_asker.get_question().get_question_text()
        self.answer_text = self.question_asker.get_question().get_answer_text()
        return self.question_number, self.question_text, self.answer_text

    def end_round(self):
        """Forces the round to end"""
        self.question_number = 0
        logging.debug("Ending Round ...")

    def next_question(self) -> bool:
        """Updates the next question"""
        logging.debug("Next Question")
        try:
            self.measure_answer_time()
            logging.debug("Next Question Called")
            logging.debug("Question asker called")

            # Display the next question
            self.question_asker.ask_question() # Duplicated??

            this_question = self.question_asker.get_question()
            self.question_text = this_question.get_question_text()


            self.question_asker.set_user_input(self.user_input)
            self.answer_text = this_question.get_answer_text()
            logging.debug(f"Question: {self.question_text}; Answer: {self.answer_text}")
            if self.question_asker.check_answer_is_correct():
                logging.debug("Correct!")
                return True
            else:
                logging.debug("Incorrect!")
                return False
        except Exception as e:
            logging.error("An error has occurred: %s",e)
            return False


    def set_user_input(self, user_input: str):
        self.user_input = user_input


if __name__ == '__main__':
    print("Testing Round Runner")
    print()
    test_start_difficulty = 5
    round_runner = RoundRunner(test_start_difficulty)
    # round_runner.start_of_round()
    i = 0
    NUM_QUESTIONS = 5
    while i < NUM_QUESTIONS:
        print(i)
        round_runner.next_question()
        i += 1
    print("Ended at i =", i)