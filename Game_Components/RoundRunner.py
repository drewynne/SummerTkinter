import time
from Game_Components.QuestionAsker2 import QuestionAsker2
from Game_Components.Difficulty import Difficulty


class RoundRunner:
    """Round Runner Class"""
    # (Runs one Round)

    # Constants
    QUESTIONS_PER_ROUND: int = 10

    # Initializing the class
    def __init__(self, start_difficulty: int):
        """Round Runner Object Constructor"""
        self.user_input = ""
        self.question_asker = QuestionAsker2(start_difficulty)
        self.difficulty = Difficulty()
        self.difficulty.set_start_difficulty(start_difficulty)
        self.question_number = 0
        self.question_text = ""
        self.answer_text = ""

    def start_of_round(self) -> bool:
        """Start of the Round"""
        print("Starting Round ...")
        if self.next_question():
            self.question_number += 1
            return True
        else:
            self.end_round()
            return False

    def run_round(self):
        """Round Run Function, runs 10 questions per round"""
        for _ in range(self.QUESTIONS_PER_ROUND):
            self.question_asker.set_difficulty(self.difficulty)
            start_time = time.time()
            is_correct = self.question_asker.ask_question()
            elapsed_time = time.time() - start_time
            if not is_correct:  # User Made a Mistake
                elapsed_time += 1000
                # time.sleep(4)
            q_type = self.question_asker.get_q_type()
            self.difficulty.set_difficulty(q_type, elapsed_time)
            # print(elapsed_time)
        self.end_round()

    # TODO: Replace with actual functionality from next_question function
    def get_question_bundle(self):
        """Gets a full bundle"""
        self.question_number += 1
        if self.question_number > RoundRunner.QUESTIONS_PER_ROUND:
            self.question_number = 1
        self.next_question()
        self.answer_text = self.user_input
        return self.question_number, self.question_text, self.answer_text

    def end_round(self):
        """Forces the round to end"""
        print("Ending Round ...")

    def next_question(self) -> bool:
        """Updates the next question"""
        try:
            print("Next Question Called")
            self.question_asker.ask_question()
            this_question = self.question_asker.get_question()
            self.question_text = this_question.get_question_text()
            self.question_asker.set_user_input(self.user_input)
            self.answer_text = this_question.get_answer_text()
            print(self.question_text, " = ", self.answer_text)
            if self.question_asker.check_answer_is_correct():
                print("Correct!")
            else:
                print("Wrong!")
            return True
        except Exception as e:
            print(f"An error has occurred: {e}")
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