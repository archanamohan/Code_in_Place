"""
Part A:
10. Because the value of n from the divide_and_round()
function is not passed to the main() function.
"""

"""
Part B: 
Edit this code so that it works correctly
"""


def divide_and_round(n):
    """
    Divides an integer n by 2 and rounds
    up to the nearest whole number
    """
    if n % 2 == 0:
        n = n / 2
    else:
        n = (n + 1) / 2

    return (n)  # Adding a return function to send back the values to main()


def main():
    n = 11

    # The value of n is sent as an argument to the divide_and_round() function
    # and received back to the variable n, so that the manipulations from the code
    # are accessible in main()
    n = divide_and_round(n)

    print(n)

if __name__ == "__main__":
    main()