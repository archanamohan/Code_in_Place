"""
Write a program that asks a user to continuously enter numbers
and print out the running total, the sum of all the numbers so
far. Once you get the program working, see if you can modify
it so that the program stops when the user enters a 0.

"""
EXIT_CODE = 0

def main():
    running_total()

def running_total():
    total = 0
    while True:
        number = int(input("Please enter a number:"))
        if number == EXIT_CODE:
            break
        total += number
        print("The running total is " + str(total) + "\n")

if __name__ == "__main__":
    main()