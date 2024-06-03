#################################################################
# FILE : math_print.py
# WRITER : Ahmad , ahmad_dall7 , 324059856
# EXERCISE : intro2cse ex1 2021
# DESCRIPTION: A program that prints many values .
# STUDENTS I DISCUSSED THE EXERCISE WITH: Mahmoud .
# WEB PAGES I USED: https://docs.python.org/3.7/library/math.html
# NOTES: -
#################################################################


import math


def golden_ratio():
    print((1+math.sqrt(5))/2)       # this code prints the golden ratio


def six_squared():
    print(math.pow(6, 2))          # this code prints 6 powered by 2


def hypotenuse():
    print(math.hypot(5, 12))       # this code prints the hypotenuse of a triangle


def pi():
    print(math.pi)                 # this code prints the value of pi


def e():
    print(math.e)                  # this code prints the value of e


def squares_area():
    print(math.pow(1, 2), math.pow(2, 2), math.pow(3, 2), math.pow(4, 2), math.pow(5, 2), math.pow(6, 2),
          math.pow(7, 2), math.pow(8, 2), math.pow(9, 2), math.pow(10, 2))

    # this code prints area of squares from 1 to 10 (inclusive)


if __name__ == "__main__":
    golden_ratio()
    six_squared()
    hypotenuse()
    pi()
    e()
    squares_are()
