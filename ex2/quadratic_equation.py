#################################################################
# FILE : quadratic_equation.py
# WRITER : Ahmad , ahmad_dall7 , 324059856
# EXERCISE : intro2cse ex2 2021
# DESCRIPTION: A program that receive 3 numbers and solve the quadratic equation
# STUDENTS I DISCUSSED THE EXERCISE WITH: -
# WEB PAGES I USED:-
# NOTES: -
#################################################################
import math


def quadratic_equation(a, b, c):
    d = (b**2) - (4*a*c)
    if d > 0:
        return (-b + math.sqrt(d)) / (2*a), (-b - math.sqrt(d)) / (2*a)
    if d == 0:
        return -b / (2*a), None
    if d < 0:
        return None, None


def quadratic_equation_user_input():
    enter = input("Insert coefficients a, b, and c: ").split()
    a = float(enter[0])
    if a == 0:
        print("The parameter 'a' may not equal 0")
        return None
    b = float(enter[1])
    c = float(enter[2])
    x1, x2 = quadratic_equation(a, b, c)
    if x1 is not None and x2 is not None:
        print("The equation has 2 solutions:", x1, 'and', x2)
    elif x1 is not None and x2 is None:
        print("The equation has 1 solution:", x1)
    elif x1 is None and x2 is not None:
        print("The equation has 1 solution:", x2)
    elif x1 is None and x2 is None:
        print("The equation has no solutions")
