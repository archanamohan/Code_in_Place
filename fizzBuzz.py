"""
In the game Fizz Buzz, players take turns counting up from one.
If a player’s turn lands on a number that’s divisible by 3,
the program should say fizz instead of the number, and if it lands on
a number that’s divisible by 5, it should say buzz instead of
the number. If the number is both a multiple of 3 and of 5,
the program should say fizzbuzz instead of the number.
"""

def main():

    number = int(input("Please enter a number: "))
    fizz = 0
    buzz = 0
    fizzbuzz = 0

    for i in range(1, number + 1):
        if i % 15 == 0:
            print("FizzBuzz")
            fizzbuzz += 1
        elif i % 3 == 0:
            print("Fizz")
            fizz += 1
        elif i % 5 == 0:
            print("Buzz")
            buzz += 1
        else:
            print(i)

    print("\nNum Fizzes: " + str(fizz))
    print("Num Buzzes: " + str(buzz))
    print("Num Fizzbuzz: " + str(fizzbuzz))



if __name__  == "__main__":
    main()