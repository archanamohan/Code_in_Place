"""
This program asks the user for two numbers and prints their average.
"""

def main():
    print("This program print the average of teo numbers:")
    num1 = float(input("Enter number 1: "))
    num2 = float(input("Enter number 2: "))

    avg = (num1 + num2) / 2

    print("Their average is " + str(avg))

if __name__ == "__main__":
    main()

