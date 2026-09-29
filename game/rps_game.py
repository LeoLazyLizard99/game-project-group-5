# Lab 1
# Group 5
# Alexander
# Date: 9/28/2026

import random


def rock_paper_scissors():

    computer = random.randint(1, 3)


    player = int(input("choose 1 for rock, 2 for paper, or 3 for scissors: "))


    print("You chose:", player)
    print("Computer chose:", computer)


    if player == computer:
        print("Tie")

    elif player == 1 and computer == 3:
        print("You win")

    elif player == 2 and computer == 1:
        print("You win")

    elif player == 3 and computer == 2:
        print("You win")

    else:
        print("Computer wins")


# if __name__ == "__main__":
#     while True:
#         rock_paper_scissors()

#         again = input("Do you want to play again? (y/n): ")

#         if again.lower() == "n":
#             print("Thanks for playing!")
#             break