# Difficulty Class
# Commenced 07/07/2022
#


class Difficulty:
    """
    Represents the difficulty level for a set of questions and provides methods to adjust it based on user performance.

    Constants:
        MIN_DIFFICULTY: int
            Must be a minimum of 2 for the question algorithms to work.
        CONSCIOUSNESS_THRESHOLD_FACTOR: int
            Multiplier for determining the consciousness threshold.
        COEFF1: float
            First coefficient used in the compute_difficulty formula.
        COEFF2: float
            Second coefficient used in the compute_difficulty formula.
        COEFF3: float
            Third coefficient used in the compute_difficulty formula.

    Attributes:
        difficulty_levels: list[float]
            Difficulty for each question type.
        time_difference: float
            Time difference (delta/differential) in seconds.
        average_time: float
            Average time to answer a question.
        consciousness_threshold: float
            Time (in seconds) for System 1 to solve a question automatically.
    """
    # Constants:
    MIN_DIFFICULTY: int = 2  # Must Be a minimum of 2 for the question algorithms to work
    CONSCIOUSNESS_THRESHOLD_FACTOR: float = 3.5
    COEFF1: float = 0.0
    COEFF2: float = 0
    COEFF3: float = 4.0

    difficulty_list: list[float]  # difficulty for each question type
    time_difference: float = 1.0  # time difference (delta/differential) in seconds
    average_time: float = 1.0  # Average time to answer question
    consciousness_threshold: float = 3.5  # Time (in seconds) for System 1 to solve question automatically
    # Approximately 1 to 2 seconds plus allowing time for user input (1.5 seconds).

    def __init__(self, level) -> None:
        """ Difficulty object constructor """
        # print("Difficulty Object Initialised")
        self.difficulty_list = [4.0, 4.0, 4.0, 4.0]
        self.level = level

    def __le__(self, other):
        if isinstance(other, int):
            return self.level <= other
        else:
            return NotImplemented

    def __ge__(self, other):
        if isinstance(other, int):
            return self.level >= other
        elif isinstance(other, Difficulty):
            return self.level >= other.level
        return NotImplemented


    def __eq__(self, other):
        if isinstance(other, int):
            return self.level == other
        elif isinstance(other, Difficulty):
            return self.level == other.level
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, int):
            return self.level < other
        elif isinstance(other, Difficulty):
            return self.level < other.level
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, int):
            return self.level > other
        elif isinstance(other, Difficulty):
            return self.level > other.level
        return NotImplemented

    def __repr__(self):
        return f"Difficulty(level={self.level})"

    def set_start_difficulty(self, start_difficulty: int) -> None:
        """ Sets start difficulty """
        self.consciousness_threshold = start_difficulty * Difficulty.CONSCIOUSNESS_THRESHOLD_FACTOR
        self.difficulty_list = [start_difficulty] * len(self.difficulty_list)

    def set_difficulty(self, q_type: int, elapsed_time: float) -> None:
        """ Sets difficulty based on question type and elapsed time """
        self.update_average_time(elapsed_time)  # Compute Average time to answer
        diff = self.consciousness_threshold - self.average_time # Measure Average Time Against Consciousness Threshold
        temp_difficulty = self.compute_difficulty(diff)
        # Update difficulty for current question, don't allow it to go below MIN_DIFFICULTY
        self.difficulty_list[q_type] = max(int(temp_difficulty), Difficulty.MIN_DIFFICULTY)

    def update_average_time(self, elapsed_time: float) -> None:
        """ Updates average time """
        self.average_time = self.rolling_average(self.average_time, elapsed_time) # Updates the average time to answer

    @staticmethod
    def rolling_average(average: float, new_sample: float) -> float:
        """ Helper function for rolling average """
        num_samples = 8  # Number of samples to average over
        return (average * (num_samples - 1) + new_sample) / num_samples # Compute new rolling average

    def compute_difficulty(self, diff: float) -> float:
        """ Compute difficulty using the given formula """
        # Large Polynomial but generally just a coefficient on the last term (COEFF3)
        return (Difficulty.COEFF1 * diff ** 5 +
                Difficulty.COEFF2 * diff ** 3 +
                Difficulty.COEFF3 * diff)

    def get_difficulty(self):
        """get difficulty"""
        return self.difficulty_list


if __name__ == '__main__':  # Test Code
    print("Testing Difficulty Class")
    print()
