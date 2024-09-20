import random

from Game_Components.Question_Types.Question import Question


class Multiplication(Question):
    """
    class Multiplication(Question):
        Multplication class generates a multiplication question based on the difficulty level.

        RANDOM_LOWER_BOUND
            Lower bound for generating random numbers.

        RANDOM_UPPER_BOUND
            Upper bound for generating random numbers.

    def __init__(self, difficulty):
        Initializes a Multiplication instance with the specified difficulty level.

        difficulty
            An integer representing the difficulty level of the question.

    def ask_question(self):
        Ask a question by generating question text and answer.
        Calls generate_question_and_answer method.

    def generate_question_and_answer(self):
        Generate the multiplication question and answer based on difficulty level.

        Generates two numbers within the range of difficulty level and random bounds,
        sets the question text with the format "num1 x num2",
        and calculates the correct answer.
    """
    RANDOM_LOWER_BOUND = 1  # Sets the minimum number that the rng will use
    RANDOM_UPPER_BOUND = 10  # Sets the maximum number that the rng will use

    def __init__(self, difficulty):
        super().__init__(difficulty)

    def ask_question(self):
        """ Ask a question """
        self.generate_question_and_answer()

    def generate_question_and_answer(self):
        """ Generate question and answer """
        num1 = self.difficulty + random.randint(self.RANDOM_LOWER_BOUND, self.RANDOM_UPPER_BOUND)
        num2 = self.difficulty + random.randint(self.RANDOM_LOWER_BOUND, self.RANDOM_UPPER_BOUND)
        self.question_text = f"{num1} x {num2}"
        self.answer_text = str(num1 * num2)


if __name__ == "__main__":
    print("Testing Multiplication Class")
    print()
    for i in range(20):
        a = Multiplication(i)
        a.ask_question()
        test_question_text = a.get_question_text()
        test_answer_text = a.get_answer_text()
        print(test_question_text)
        user_answer = input("Enter your answer: ")
        is_correct = a.check_answer(user_answer)
        print(test_answer_text)
        print(is_correct)


