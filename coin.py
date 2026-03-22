"""
Program Name: Match Coins Game - Player Class
Author: RAJANI BARAILI
Purpose: This program implements the Match Coins Game, where two players toss coins each round, compete to match sides, and win or lose coins based on the outcome until the game ends.
Date: March 22,2026
"""
import random

class Coin:

    def _init_(self):
        self.heads = "Heads"
        self.tails = "Tails"

    def toss(self):
        tossed_coin = random.randint(0, 1)
        sets_sideup = random.choice([self.heads, self.tails])
    def get_sideup(self):
        return sets_sideup
    





