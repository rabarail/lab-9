"""
Program Name: Match Coins Game - Main Game
Author: RAJANI Baraili
Purpose: This program implements the Match Coins Game, where two players toss coins each round, compete to match sides, and win or lose coins based on the outcome until the game ends.
Date: March 22, 2026
"""
from player import Player


def main():
    
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    while True:
        play = input("Do you want to toss the coin? (y/n)")
        if play.lower() != 'y':
            print("Tossing...")
            break

        player1.toss_coin()
        player2.toss_coin()

        side1 = player1.get_coin_side()
        side2 =player2.get_coin_side()

        print(f"{player1.get_name()} tossed {side1}")
        print(f"{player2.get_name()} tossed {side2}")

        if side1 == side2:
            player1.win_coin()
            player2.lose_coin()
            print(f"...Match! {player1.get_name()} wins a coin")
        else:
            player2.win_coin()
            player1.lose_coin()
            print(f"...No Match! {player2.get_name()} wins a coin")


        print("Final Score")
        print(f"{player1.get_name()}: {player1.get_wallet()}")
        print(f"{player2.get_name()}: {player2.get_wallet()}")

        if player1.get_wallet() > player2.get_wallet():
            print(f"{player1.get_name()} wins!")
        elif player1.get_wallet() < player2.get_wallet():
            print(f"{player2.get_name()} wins!")
        else:
            print("It's a draw!")


    

main()










