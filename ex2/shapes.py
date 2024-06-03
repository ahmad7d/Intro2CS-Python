#################################################################
# FILE : shapes.py
# WRITER : Ahmad , ahmad_dall7 , 324059856
# EXERCISE : intro2cse ex2 2021
# DESCRIPTION: A program that calculate the value of the area of circle and rectangle and triangle.
# STUDENTS I DISCUSSED THE EXERCISE WITH: -
# WEB PAGES I USED:-
# NOTES: -
#################################################################
import math


def shape_area():
    x = int(input('Choose shape (1=circle, 2=rectangle, 3=triangle): '))
    if 1 > x > 3:
        return None
    elif x == 1:
        r = float(input())
        return math.pow(r, 2) * math.pi

    elif x == 2:
        a = float(input())
        b = float(input())
        return a * b
    elif x == 3:
        d = float(input())
        return (math.pow(d, 2) * math.sqrt(3)) / 4
