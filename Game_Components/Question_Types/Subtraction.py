import random

from Game_Components.Question_Types.Question import Question


class Subtraction(Question):
    """
    Subtraction class for creating and asking subtraction questions.

    Attributes:
        RANDOM_LOWER_BOUND (int): The lower bound for the random number generation.
        RANDOM_UPPER_BOUND (int): The upper bound for the random number generation.

    Methods:
        __init__(self, difficulty):
            Initializes the Subtraction question with a specified difficulty.

        ask_question(self):
            Asks a subtraction question by generating the question and answer.

        generate_question_and_answer(self):
            Generates a random subtraction question and computes the answer.
    """
    RANDOM_LOWER_BOUND = 1  # Sets the minimum number that the rng will use
    RANDOM_UPPER_BOUND = 10  # Sets the maximum number that the rng will use

    def __init__(self, difficulty):
        super().__init__(difficulty)

    def ask_question(self):
        """ Ask a question """
        self.generate_question_and_answer()

    def generate_question_and_answer(self):
        """Generate question and answer"""
        num1 = self.difficulty + random.randint(self.RANDOM_LOWER_BOUND, self.RANDOM_UPPER_BOUND)
        num2 = random.randint(self.RANDOM_LOWER_BOUND, num1)
        self.question_text = f"{num1} - {num2}"
        self.answer_text = str(num1 - num2)

if __name__ == "__main__":
    print("Testing Subtraction Class")
    print()
    for i in range(20):
        a = Subtraction(i)
        a.ask_question()
        test_question_text = a.get_question_text()
        test_answer_text = a.get_answer_text()
        print(test_question_text)
        user_answer = input("Enter your answer: ")
        is_correct = a.check_answer(user_answer)
        print(test_answer_text)
        print(is_correct)
