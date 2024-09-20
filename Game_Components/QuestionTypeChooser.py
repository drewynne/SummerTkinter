import random
import matplotlib.pyplot as plt


class QuestionTypeChooser:
    """
        class QuestionTypeChooser:
    """
    @staticmethod
    def choose_question_type():
        """ Set for Medium Difficulty Question Types """
        # Medium Difficulty Function
        question_type = random.randint(0, 3)
        return question_type

    @staticmethod
    def choose_question_type2():
        """ Set for Easy Difficulty Question Types """
        # Easy Difficulty Function
        for i in range(0, 3):
            if random.random() > 0.4:  # Happens with probability 0.6
                return i
        return 3

    @staticmethod
    def choose_question_type3():
        """ Set for Hard Difficulty Question Types """
        # Hard Difficulty Function
        for i in range(3, 0, -1):
            if random.random() > 0.4:  # Happens with probability 0.6
                return i
        return 0


if __name__ == '__main__':
    print("Testing question type functions")
    print()
    question_type_list = list()
    question_type_list2 = list()
    question_type_list3 = list()
    for question in range(1000):  # Average over 1000 Data Points
        question_type_list.append(QuestionTypeChooser.choose_question_type())
        question_type_list2.append(QuestionTypeChooser.choose_question_type2())
        question_type_list3.append(QuestionTypeChooser.choose_question_type3())

    # print(question_type_list)
    fig, axs = plt.subplots(3)
    axs[0].hist(question_type_list)
    axs[1].hist(question_type_list2)
    axs[2].hist(question_type_list3)

    plt.show()
