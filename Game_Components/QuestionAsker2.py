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
    """
    Class for asking questions of various types and difficulties.

    Attributes
    ----------
    user_defined_difficulty : int
        The difficulty level defined by the user.
    levels : list[int]
        A list of difficulty levels for different types of questions.
    level_selector : LevelSelector
        An instance of the LevelSelector class for selecting difficulty levels.
    difficulty : Difficulty
        An instance of the Difficulty class to manage and get the difficulty level.
    q_type : int
        The type of the current question.
    question : Question
        The current question to be asked.
    answer_is_correct : bool
        Indicates if the last user answer was correct.
    user_input : str
        The user’s input for the answer.

    Methods
    -------
    __init__(self, start_difficulty: int)
        Constructor.

    ask_question(self)
        Ask a question based on the current difficulty and type.

    set_user_input(self, user_input)
        Set the user's input.

    get_question(self)
        Get the current question.

    set_difficulty(self, difficulty: int)
        Set the user-defined difficulty.

    get_q_type(self)
        Get the type of the question.

    check_answer_is_correct(self)
        Check if the user's answer is correct.

    choose_question_type(self)
        Choose the type of question based on difficulty.
    """

    user_defined_difficulty: int
    levels: list[int]
    level_selector: LevelSelector
    difficulty: Difficulty
    q_type: int
    question: Question
    answer_is_correct: bool
    user_input: str

    def __init__(self, start_difficulty: int):
        """ Constructor """
        self.q_type = 0 # init as addition
        self.user_defined_difficulty = start_difficulty
        self.levels = [1, 1, 1, 1]
        self.level_selector = LevelSelector()
        self.difficulty = Difficulty(start_difficulty)
        self.levels = self.level_selector.start(start_difficulty)
        self.answer_is_correct = True
        self.question = Question(start_difficulty)
        self.user_input = ""




    def ask_question(self):
        """ Ask question """

        q_type = self.choose_question_type()
        temp_difficulty = self.difficulty.get_difficulty()
        self.levels = self.level_selector.update(temp_difficulty)

        if q_type == 0:
            self.question = Addition(self.levels[0])
        elif q_type == 1:
            self.question = Subtraction(self.levels[1])
        elif q_type == 2:
            self.question = Multiplication(self.levels[2])
        elif q_type == 3:
            self.question = Division(self.levels[3])

        self.question.ask_question()
        # print()
        # print(self.question.get_question_text())


    def set_user_input(self, user_input):
        self.user_input = user_input


    def get_question(self):
        return self.question

    def set_difficulty(self, difficulty: int):
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


    for i in range(30):
        asker = QuestionAsker2(i)
        asker.ask_question()
        question = asker.get_question()
        print()
        print(question.get_question_text())