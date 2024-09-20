import logging


class Game:
    """ Game Class """
    ROUNDS_PER_GAME: int = 3
    MIN_START_DIFFICULTY: int = 1
    MAX_START_DIFFICULTY: int = 10
    EMPTY_STRING = ""

    round_number: int
    start_difficulty: int
    round_runner: RoundRunner
    current_question: Question

    def __init__(self, start_difficulty: int):
        self.__setup_game(start_difficulty)
        self.current_question = Question(self.start_difficulty)

    def __setup_game(self, start_difficulty: int):
        self.start_difficulty = max(min(start_difficulty, Game.MAX_START_DIFFICULTY), Game.MIN_START_DIFFICULTY)
        self.round_number = 1
        self.round_runner = RoundRunner(self.start_difficulty)
        logging.debug("Game initialized with start difficulty %d", self.start_difficulty)

    def handle_user_response(self, user_answer: str) -> None:
        logging.debug("Handling user response: %s", user_answer)
        if user_answer == Game.EMPTY_STRING:
            logging.debug("No answer provided, skipping question.")
            return
        self.__process_answer(user_answer)

    def __process_answer(self, user_answer: str) -> None:
        self.round_runner.set_user_input(user_answer)
        is_correct_answer = self.round_runner.next_question()
        self.__log_answer_result(is_correct_answer)

    def __log_answer_result(self, is_correct: bool) -> None:
        logging.debug('Correct!' if is_correct else 'Incorrect, try again.')

    def initiate_round(self) -> bool:
        logging.debug("Initiating round %d", self.round_number)
        if not self.__rounds_in_range():
            self.__end_game()
            return False
        if self.round_runner.begin_round():
            self.__start_round()
            return True
        self.__end_round()
        return False

    def __rounds_in_range(self) -> bool:
        in_range = self.round_number <= Game.ROUNDS_PER_GAME
        logging.debug("Rounds within range: %s", in_range)
        return in_range

    def __start_round(self):
        self.round_number += 1
        logging.debug("Round %d starting", self.round_number)

    def __end_round(self):
        logging.debug("Ending current round")
        self.round_runner.end_round()

    def __end_game(self):
        logging.debug("Game over, out of rounds!")

    def get_question_bundle(self) -> tuple:
        return self.round_runner.get_question_bundle()

    def next_question(self) -> bool:
        return self.round_runner.next_question()

    @staticmethod
    def loving_it() -> bool:
        user_in = input("Press 1 to play a round, 0 to stop: ")
        while user_in not in {"0", "1"}:
            logging.debug("Invalid input received")
            user_in = input("Press 1 to play a round, 0 to stop: ")
        return user_in == "1"

    @property
    def round_number(self) -> int:
        return self._round_number

    # We use a property to get the current round number.