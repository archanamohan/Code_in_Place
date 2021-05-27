def main():
    """
    Write a program that asks the user to enter a
    sequence of "non-decreasing" numbers one at a
    time. Numbers are non-decreasing if each number
     is greater than or equal to the last.
    """
    print("Enter a sequence of non-decreasing numbers.")
    curr_number = float(input("Enter num: "))

    prev_number = curr_number
    sequence = 0

    while curr_number >= prev_number:
        sequence = sequence + 1
        prev_number = curr_number
        curr_number = float(input("Enter num: "))

    print("Thanks for playing!")
    print("Sequence length: " + str(sequence))


if __name__ == "__main__":
    main()