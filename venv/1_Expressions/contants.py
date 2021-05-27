"""
An example program with constants.
Converts feet to total number of inches.
"""

INCHES_IN_FEET = 12

def main():
    feet = float(input("Enter the distance is feet: "))
    inches = feet * INCHES_IN_FEET
    print("That is " + str(inches) + " inches!")
if __name__ == '__main__':
    main()