class Difficulty:
    def __init__(self, level):
        self.level = level

    def __le__(self, other):
        if isinstance(other, int):
            return self.level <= other
        return NotImplemented

    def __repr__(self):
        return f"Difficulty(level={self.level})"


difficulty = Difficulty(5)

try:
    if difficulty <= 10:  # Uses the __le__ method for comparison
        print("Valid difficulty level")
    else:
        print("Invalid difficulty level")
except Exception as e:
    print(f"An error has occurred: {e}")