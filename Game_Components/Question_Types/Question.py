

class Question:
    """
    Class representing a question with difficulty levels, text, and answer.
    """
    # Variables
    num1: int # 1st Number for arithmetic question
    num2: int # 2nd Number for arithmetic question
    difficulty: int # difficulty variable
    question_text: str # Text containing the question (eg. num1 + num2)
    answer_text: str # Correct answer to the question
    is_correct: bool # boolean for correct answer
    user_answer: str # user's answer to question
    # Objects

    def __init__(self, difficulty: int):
        """ Question Constructor """
        self.difficulty = difficulty
        self.question_text = ""
        self.answer_text = ""
        self.is_correct = False
        self.user_answer = ""

    def ask_question(self):
        """ Ask question """
        print(self.question_text)

    def get_question_text(self):
        """ Get question text """
        return self.question_text

    def get_answer_text(self):
        """ Get answer text """
        return self.answer_text

    def check_answer(self, user_answer) -> bool:
        """ Check if user answer is correct """
        self.user_answer = user_answer
        self.is_correct = self.answer_text == self.user_answer
        return self.is_correct


if __name__ == '__main__':  # Test Code

    question = Question(5)

    question.ask_question()

