# Difficulty Class
# Commenced 07/07/2022
#


class Difficulty:
    """ Difficulty class """
    # Constants:
    MIN_DIFFICULTY: int = 2  # Must Be a minimum of 2 for the question algorithms to work
    difficultyArray: list[int]  # difficulty for each question type
    diff: float = 1.0  # time difference (delta/differential) in seconds
    averageTime: float = 1.0  # Average time to answer question
    consciousnessThreshold: float = 20.48  # Time for System 1 to solve question automatically

    def __init__(self):
        """ Difficulty object constructor """
        print("Difficulty Object Initialised")
        self.difficultyArray = [4, 4, 4, 4]

    def set_start_difficulty(self, start_difficulty):
        """ sets start difficulty """
        self.consciousnessThreshold = start_difficulty * 5
        for d in range(0, len(self.difficultyArray)):
            self.difficultyArray[d] = start_difficulty

    def addition_difficulty(self):
        """ returns addition difficulty """
        return self.difficultyArray[0]

    def subtraction_difficulty(self):
        """ returns subtraction difficulty """
        return self.difficultyArray[1]

    def multiplication_difficulty(self):
        """ returns multiplication difficulty """
        return self.difficultyArray[2]

    def division_difficulty(self):
        """ returns division difficulty """
        return self.difficultyArray[3]

    def set_difficulty(self, q_type: int, elapsed_time):
        """ sets difficulty based on question type and elapsed time """

        self.update_average_time(elapsed_time)
        diff = self.consciousnessThreshold - self.averageTime
        temp_difficulty: float
        temp_difficulty = 0.0 * diff ** 5 + 0.0 * diff ** 3 + 4.0 * diff
        self.difficultyArray[q_type] = int(temp_difficulty)

        if self.difficultyArray[q_type] < Difficulty.MIN_DIFFICULTY:  # Constrain to Minimum Difficulty
            self.difficultyArray[q_type] = Difficulty.MIN_DIFFICULTY

    def update_average_time(self, elapsed_time):
        """ updates average time """
        self.averageTime = self.rolling_average(self.averageTime, elapsed_time)

    @staticmethod
    def rolling_average(average, new_sample):
        """ helper function for rolling average """
        num_samples = 8

        average -= average / num_samples
        average += new_sample / num_samples

        return average


if __name__ == '__main__':  # Test Code
    print("Testing Difficulty Class")
    print()
