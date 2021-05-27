"""
This program helps convert the inches to baby carrots.
"""
BABY_CARROT = 2

def main():
    inches = float(input("Enter the inches: "))
    babycarrot = float(inches / BABY_CARROT)

    print("That is " + str(babycarrot) + " baby carrot!")

if __name__ == '__main__':
    main()