import logging

logging.basicConfig(level=logging.DEBUG)

class LevelSelector:
    """
    LevelSelector class for managing and updating difficulty levels.
    """

    def __init__(self):
        logging.debug("Level Selector Initialised")
        pass

    def update(self, difficulty: list[float]):
        """update the levels based on the difficulty list"""
        levels = list()

        for i in range(4):
            dif = difficulty[i]
            dif = self.check_difficulty(dif)
            level = int(dif / 10)
            levels.append(level)
        return levels

    def start(self, start_difficulty: int):
        """ start the levels based on the start_difficulty"""
        levels = list()
        for i in range(4):
            levels.append(start_difficulty)
        return levels

    @staticmethod
    def check_difficulty(difficulty):
        """ Check that difficulty is within range"""
        if difficulty < 1: # absolute minimum of 1
            difficulty = 1.0
        if difficulty > 10000: # Max of 10K
            difficulty = 10000.0

        return difficulty
