

class Question:
    """ Question class """
    # Variables
    a: int
    b: int
    difficulty: int
    question_text: str
    answer_text: str
    is_correct: bool
    user_answer: str
    # Objects

    def __init__(self, difficulty):
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

    def check_answer(self, user_answer):
        """ Check if user answer is correct """
        self.user_answer = user_answer
        self.is_correct = self.answer_text == self.user_answer
        return self.is_correct


if __name__ == '__main__':  # Test Code

    question = Question()

    question.ask_question()

