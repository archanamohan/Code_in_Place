"""
TODO: Write a description here
"""

import random



def main():
    STONES = 20
    PLAYER = 0
    print("There are " + str(STONES) + " stones left")

    while STONES >= 0:
        if PLAYER % 2 == 0:
            player1_input = int(input("Player 1 would you like to remove 1 or 2 stones? "))
            STONES -= player1_input
        else:
            player2_input = int(input("\nPlayer 2 would you like to remove 1 or 2 stones? "))
            STONES -= player2_input

        print("There are " + str(STONES) + " stones left.")
        PLAYER += 1

    print("\nPlayer " + str(PLAYER % 2 + 1)+ " won!")
if __name__ == '__main__':
    main()