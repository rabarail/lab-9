"""
Program Name: Match Coins Game - Coin Class
Author: RAJANI BARAILI
Purpose: This program implements the Match Coins Game, where two players toss coins each round, compete to match sides, and win or lose coins based on the outcome until the game ends.
Date: March 22,2026
"""
import random

class Coin:

    def __init__(self):
        self.__sideup = 'Heads'

    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'

    def get_sideup(self):
        return self.__sideup







