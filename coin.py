"""
Program Name: Match Coins Game - Player Class
Author: RAJANI BARAILI
Purpose: This program implements the Match Coins Game, where two players toss coins each round, compete to match sides, and win or lose coins based on the outcome until the game ends.
Date: March 22,2026
"""
import random

class Coin:

    def __init__(self):
        self.heads = "Heads"
        self.tails = "Tails"

    def toss(self):
        self.side_up = random.choice([self.head, self.tail])

    def get_sideup(self):
        return self.side_up







