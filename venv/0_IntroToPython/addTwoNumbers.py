"""
A Python program that asks the user for two numbers (integers) and prints their sum on the screen.
"""

def main():
    print("This program prints the sum of two numbers.")
    num1 = int(input("Enter number1: "))
    num2 = int(input("Enter number2: "))

    sum = num1 + num2

    print("Sum of two numbers are " + str(sum))

if __name__ == "__main__":
    main()