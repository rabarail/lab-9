"""
Program Name: Match Coins Game - Main Game
Author: RAJANI Baraili
Purpose: This program implements the Match Coins Game, where two players toss coins each round, compete to match sides, and win or lose coins based on the outcome until the game ends.
Date: March 22, 2026
"""
import player as p
import coin as c

def main():
    
    player1 = Player("Player 1")
    player2 = Player("Player 2")

while True:
    play = input("Do you want to toss the coin? (y/n)")
    if play !='y' or 'Y':
        break

    player1.tossed_coin()
    player2.tossed_coin()

    side1 = player1.get_coin_side()
    side2 =player2.get_coin_side()

