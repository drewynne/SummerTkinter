# Commenced 03/09/2024
from Game_Components.Difficulty import Difficulty
from Game_Components.LevelSelector import LevelSelector
from Game_Components.QuestionTypeChooser import QuestionTypeChooser
from Game_Components.Question_Types.Addition import Addition
from Game_Components.Question_Types.Division import Division
from Game_Components.Question_Types.Multiplication import Multiplication
from Game_Components.Question_Types.Question import Question
from Game_Components.Question_Types.Subtraction import Subtraction


class QuestionAsker2:
    """ Question Asker2 Class """

    user_defined_difficulty: int
    levels: list[int]
    level_selector: LevelSelector
    difficulty: Difficulty
    q_type: int
    question: Question
    answer_is_correct: bool
    user_input: str

    def __init__(self, start_difficulty):
        """ Constructor """
        self.q_type = 0 # init as addition
        self.user_defined_difficulty = start_difficulty
        self.levels = [1, 1, 1, 1]
        self.level_selector = LevelSelector()
        self.difficulty = Difficulty()
        self.levels = self.level_selector.start(start_difficulty)
        self.answer_is_correct = True
        self.question = Question(start_difficulty)
        self.user_input = ""




    def ask_question(self):
        """ Ask question """

        q_type = self.choose_question_type()
        difficulty = [10, 10, 10, 10]
        self.levels = self.level_selector.update(difficulty)

        if q_type == 0:
            self.question = Addition(self.levels[0])
        elif q_type == 1:
            self.question = Subtraction(self.levels[1])
        elif q_type == 2:
            self.question = Multiplication(self.levels[2])
        elif q_type == 3:
            self.question = Division(self.levels[3])

        self.question.ask_question()
        print()
        print(self.question.get_question_text())


    def set_user_input(self, user_input):
        self.user_input = user_input


    def get_question(self):
        return self.question

    def set_difficulty(self, difficulty):
        self.user_defined_difficulty = difficulty

    def get_q_type(self):
        return self.q_type

    def check_answer_is_correct(self):
        self.answer_is_correct = self.question.check_answer(self.user_input)
        return self.answer_is_correct

    def choose_question_type(self):

        if self.user_defined_difficulty <= 3: # Easy Difficulty
            q_type = QuestionTypeChooser.choose_question_type2()
        elif self.user_defined_difficulty >= 8: # Hard Difficulty
            q_type = QuestionTypeChooser.choose_question_type3()
        else: # Medium Difficulty
            q_type = QuestionTypeChooser.choose_question_type()

        return q_type



if __name__ == "__main__":
    print("Testing QuestionAsker2")

    asker = QuestionAsker2(5)
    for i in range(5):
        asker.ask_question()
        question = asker.get_question()
        print()
        print(question.get_question_text())