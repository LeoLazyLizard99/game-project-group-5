# Lab 1
# Group 5
# Florian
# Date: 9/22/2026

import num_guess_game
import rps_game

def runGame(x):
    if x == "1":
        print("The Random Number Guessing game is a great choice!")
        #num game func here
    elif x == "2":
        print("Rock Paper Scissors, this will be fun")
        #run func for game here

def Main():
    playing = True
    while playing:
        print("""
        Hello!
        What game would you like to play?
        [1] Random Number Guessing
        [2] Rock Paper Scissors
        """)
        game = input("what game?: ")
        runGame(game)

        again = input("Play a different game? (y/n): ").strip().lower()
        if again != "y":
            playing = False
            print("Thanks for playing!")

if __name__ == "__main__":
    Main()