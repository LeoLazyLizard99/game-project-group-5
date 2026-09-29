# Lab 1
# Group 5
# Nadwr
# Date: 9/28/2026

import random
def numGame():
    tries = 5
    min = 1
    max = 100
    win = False
    randomNumber = random.randint(min, max)
    for i in range(tries):
        print(f"Try {i + 1}")
        guess = int(input("Enter your guess: "))
        if guess == randomNumber:
            win = True
            break
        elif guess < randomNumber:
            print("too low")
        elif guess > randomNumber:
            print("too high")
    if win:
        print("Congratulations! You won!")
    else:
        print(f"Sorry, you lost. The number was {randomNumber}")