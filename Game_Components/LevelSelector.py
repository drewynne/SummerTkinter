class LevelSelector:
    """ Level Selector Class """

    def __init__(self):
        print("Level Selector Initialised")
        pass

    def update(self, difficulty: list[int]):
        levels = list()

        for i in range(4):
            dif = difficulty[i]
            dif = self.check_difficulty(dif)
            level = int(dif / 5)
            levels.append(level)
        return levels

    def start(self, start_difficulty: int):
        levels = list()
        for i in range(4):
            levels.append(start_difficulty)
        return levels

    def check_difficulty(self, difficulty):
        if difficulty < 1:
            difficulty = 1
        if difficulty > 10000:
            difficulty = 10000

        return difficulty
