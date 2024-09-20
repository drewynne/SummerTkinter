# QuestionPopper Class
# Commenced 03/07/2022
#
import random
import math
from Game_Components.Difficulty import Difficulty
from Game_Components.QuestionTypeChooser import QuestionTypeChooser
from Game_Components.Question_Types.Question import Question


class QuestionAsker:
    """ Question Asker Class """
    # Variables
    qType: int  # Question Type Variable
    question_number: int
    # Objects
    difficulty: Difficulty  # Difficulty Object
    current_question = Question  # Current Question

    def __init__(self):
        """ Question Asker Object Constructor """
        print("Question Asker Activated")
        self.difficulty = Difficulty()
        self.qType = 0
        self.question_number = 0

    def ask_question(self, q_number):
        """ Asks a Question of random type (0 to 3) """

        # print("Question ", q_number)

        self.qType = QuestionTypeChooser.choose_question_type()  # random.randint(0, 3)

        if self.qType == 0:
            answers = self.addition(self.difficulty.addition_difficulty())
        elif self.qType == 1:
            answers = self.subtraction(self.difficulty.subtraction_difficulty())
        elif self.qType == 2:
            answers = self.multiplication(self.difficulty.multiplication_difficulty())
        else:
            answers = self.division(self.difficulty.division_difficulty())

        return self.check_answer(answers)

    def ask_next_question(self):
        """ Asks the next question """
        print("Asking a Question")
        self.question_number += 1
        # print("Question Number =", self.question_number)
        return self.question_number <= 10

    def addition(self, difficulty):
        """ addition question function """
        a = random.randint(2, int(difficulty) + 2)
        b = random.randint(1, int(difficulty))

        question = str(a) + ' + ' + str(b)
        # user_answer = int(self.get_input(question))
        user_answer = -1
        correct_answer = a + b
        return user_answer, correct_answer, question

    def subtraction(self, difficulty):
        """ subtraction question function """
        a = random.randint(5, difficulty + 3)
        b = a - random.randint(2, round(difficulty / 3) + 3)

        question = '\t\t\t' + str(a) + ' - ' + str(b) + ' = \n\n\n\n'

        # user_answer = int(self.get_input(question))
        user_answer = -1
        correct_answer = a - b
        return user_answer, correct_answer

    def multiplication(self, difficulty):
        """ multiplication question function """
        difficulty *= 0.5
        a = math.floor(difficulty / 10)  # Extract 1st significant digit
        b = round(difficulty % 10)  # Extract 2nd significant digit

        a = random.randint(a, a + 9)
        b = random.randint(b, b + 9)

        question = '\t\t\t' + str(a) + ' * ' + str(b) + ' = \n\n\n\n'
        # user_answer = int(self.get_input(question))
        user_answer = -1
        correct_answer = a * b
        return user_answer, correct_answer

    def division(self, difficulty):
        """ division question function """
        difficulty *= 1.5
        b = random.randint(2, 12)
        a = b * random.randint(2, round(difficulty / 3) + 3)
        question = '\t\t\t' + str(a) + ' / ' + str(b) + ' = \n\n\n\n'
        # user_answer = int(self.get_input(question))
        user_answer = -1
        correct_answer = a / b
        return user_answer, correct_answer

    def get_input(self, prompt):  # Get user input and ignore blanks
        """ Gets user inputs while ignoring accidental enter button presses """
        userIn = input(prompt)

        if userIn == '':
            userIn = self.get_input(prompt)

        return userIn

    def set_difficulty(self, difficulty):
        """ set difficulty function """
        self.difficulty = difficulty

    @staticmethod
    def check_answer(answers):
        """ check answer function """
        [user_answer, correct_answer] = answers
        is_correct = user_answer == correct_answer

        print("Answer = ", is_correct)
        return is_correct

    def get_q_type(self):
        """ returns the question type """
        return self.qType

    def get_question_number(self):
        print("Question Number =", self.question_number)
        question_number = self.question_number
        return question_number

    def get_question_text(self):
        random_question = self.addition(10)
        return random_question[2]

    def get_answer_text(self):
        print("Random Answer...")
        random_answer = random.randint(1, 5)

        return str(random_answer)


if __name__ == '__main__':
    print("Testing Question Popper")
    print()
    
    question_asker = QuestionAsker()
    test_question_number = 12  # Behaviour Will change after 10
    for i in range(test_question_number):
        if question_asker.ask_next_question():
            test_question_number = question_asker.get_question_number()
            test_answer_text = question_asker.get_answer_text()
            print(test_answer_text)
            test_question_text = question_asker.get_question_text()
            print(test_question_text)
        else:
            print("Question Number out of range")

        # print(question_asker.get_question_number())
