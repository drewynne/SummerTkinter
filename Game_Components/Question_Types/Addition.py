import random

from Game_Components.Question_Types.Question import Question



class Addition(Question):
    """
    class Addition(Question):
    RANDOM_LOWER_BOUND = 2
    RANDOM_UPPER_BOUND = 10

    def __init__(self, difficulty):
        super().__init__(difficulty)

        Initialize the Addition class instance with a specified difficulty level.

        :param difficulty: The difficulty level for the question, an integer.

    def ask_question(self):
        """
    RANDOM_LOWER_BOUND = 2  # Sets the minimum number that the rng will use
    RANDOM_UPPER_BOUND = 10  # Sets the maximum number that the rng will use

    def __init__(self, difficulty):
        super().__init__(difficulty)

    def ask_question(self):
        """Ask a question"""
        self.generate_question_and_answer()

    def generate_question_and_answer(self):
        """Generate question and answer"""
        num1 = self.difficulty + random.randint(self.RANDOM_LOWER_BOUND, self.RANDOM_UPPER_BOUND)
        num2 = self.difficulty + random.randint(self.RANDOM_LOWER_BOUND, self.RANDOM_UPPER_BOUND)
        self.question_text = f"{num1} + {num2}"
        self.answer_text = str(num1 + num2)


if __name__ == "__main__":
    print("Testing Addition Class")
    print()
    for i in range(20):
        a = Addition(i)
        a.ask_question()
        test_question_text = a.get_question_text()
        test_answer_text = a.get_answer_text()
        print(test_question_text)
        user_answer = input("Enter your answer: ")
        is_correct = a.check_answer(user_answer)
        print(test_answer_text)
