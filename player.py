"""
Program Name: Match Coins Game - Player Class
Author: RAJANI BARAILI
Purpose: This program implements the Match Coins Game, where two players toss coins each round, compete to match sides, and win or lose coins based on the outcome until the game ends.
Date:  March 22,2026
"""
from coin import Coin

class Player:
    def _init_(self, name):
        self._name = name
        self._wallet = 20
        self._coin =Coin()

    def toss_coin(self):
        self.toss_coin()

    def get_coin_side(self):
        return self._coin.get_sideup()
    
    def win_coin(self):
        return 1 + self._wallet
    
    def get_name(name):
        return name
    