"""
Simulate rolling two dice.
Prints results of each roll as well as the total.
"""
import random

NUM_SIDES = 6

def main():
    dice1 = random.randint(1, NUM_SIDES)
    dice2 = random.randint(1, NUM_SIDES)

    print("The dice have " + str(NUM_SIDES)+ " sides")
    print("Die 1 has rolled: " + str(dice1))
    print("Die 2 has rolled: " + str(dice2))

    print("Their sum is " + str(dice1 + dice2))

if __name__ == '__main__':
    main()