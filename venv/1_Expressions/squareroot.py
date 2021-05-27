"""
This program asks the user for a number and
prints its square root.
"""
import math

def main():
    num = int(input("Please enter a number:"))
    sq = math.sqrt(num)

    print("The square root of " + str(num) + " is " + str(sq))

if __name__ == "__main__":
    main()