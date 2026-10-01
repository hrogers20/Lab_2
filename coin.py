"""
Program: Mach Coins
Author: Hannah Rogers
Purpose: Represents a coin that can be tossed
and land on heads or tails
Starter code: None
Date: September 30, 2026
"""

import random


class Coin:
    def __init__(self):
        if random.randint(0, 1) == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"

    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"

    def get_sideup(self):
        return self.__sideup