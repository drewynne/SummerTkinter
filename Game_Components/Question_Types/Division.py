import random

from Game_Components.Question_Types.Question import Question


class Division(Question):
    """
    class Division(Question)

    RANDOM_LOWER_BOUND = 1
    RANDOM_UPPER_BOUND = 10

    def __init__(self, difficulty):
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

        num2 = self.difficulty + random.randint(self.RANDOM_LOWER_BOUND, self.RANDOM_UPPER_BOUND)
        num1 = num2 * random.randint(self.RANDOM_LOWER_BOUND, self.RANDOM_UPPER_BOUND)



        self.question_text = f"{num1} / {num2}"
        self.answer_text = str(int(num1 / num2))

if __name__ == "__main__":
    print("Testing Division Class")
    print()
    for i in range(20):
        a = Division(i)

        a.ask_question()
        test_question_text = a.get_question_text()
        test_answer_text = a.get_answer_text()
        print(test_question_text)
        user_answer = input("Enter your answer: ")
        is_correct = a.check_answer(user_answer)
        print(test_answer_text)
        print(is_correct)
