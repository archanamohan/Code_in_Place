"""
Given the radius of the circle, print the area of the circle.
"""

PI = 3.14159

def main():
    radius = float(input("Please enter the radius of the circle: "))
    area = PI * radius * radius

    print("Area of the circle is " + str(area))

if __name__ == "__main__":
    main()
