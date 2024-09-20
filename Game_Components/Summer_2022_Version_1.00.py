# Summer 2022 Version 1.00
# Commenced: 03/07/2022
# Completed: TBA
#
# By Drew Wynne
# This is an updated (2022) version of the summer game in python. The Following has been added
#
#
# To Add:


import random
import time
import math
from Game import Game


def run_summer():
    # Set Start Difficulty on Scale 1 to 10
    # (Sets how long you have to answer each question) i.e.:
    """ 1 = 5s
        2 = 10s
        3 = 15s
        4 = 20s
        5 = 25s
        6 = 30s
        7 = 35s
        8 = 40s
        9 = 45s
        10 = 50s
        """
    start_difficulty = 5
    print("Starting Difficulty =", start_difficulty)

    summer = Game(start_difficulty)

    summer.start_a_round()


if __name__ == '__main__':  # Test Code
    print("Running Summer")
    print()
    run_summer()

