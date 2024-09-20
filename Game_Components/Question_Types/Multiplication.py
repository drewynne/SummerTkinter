import random

from Game_Components.Question_Types.Question import Question


class Multiplication(Question):
    """ Multiplication Class """
    RANDOM_LOWER_BOUND = 1
    RANDOM_UPPER_BOUND = 10

    def __init__(self, difficulty):
        super().__init__(difficulty)

    def ask_question(self):
        """ Ask a question """
        self.generate_question_and_answer()

    def generate_question_and_answer(self):
        """ Generate question and answer """
        num1 = random.randint(self.RANDOM_LOWER_BOUND, self.RANDOM_UPPER_BOUND)
        num2 = random.randint(self.RANDOM_LOWER_BOUND, self.RANDOM_UPPER_BOUND)
        self.question_text = f"{num1} x {num2}"
        self.answer_text = str(num1 * num2)


if __name__ == "__main__":
    print("Testing Multiplication Class")
    print()
    a = Multiplication()
    a.ask_question()
    test_question_text = a.get_question_text()
    test_answer_text = a.get_answer_text()
    print(test_question_text)
    user_answer = input("Enter your answer: ")
    is_correct = a.check_answer(user_answer)
    print(test_answer_text)
    print(is_correct)


