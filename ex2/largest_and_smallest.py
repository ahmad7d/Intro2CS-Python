#################################################################
# FILE : largest and smallest.py
# WRITER : Ahmad , ahmad_dall7 , 324059856
# EXERCISE : intro2cse ex2 2021
# DESCRIPTION: A program that return the highest and smallest numbers
# STUDENTS I DISCUSSED THE EXERCISE WITH: -
# WEB PAGES I USED:-
# NOTES: -
#################################################################
# choosing x4 : is a good case to check the result with a 3 equals numbers
# choosing x5 : is a good case to check a negative numbers
def largest_and_smallest(num1, num2, num3):
    if num1 == num2 == num3:
        return num1, num2
    elif num1 > num2 > num3 or num1 > num2 == num3 or num1 < num2 == num3:
        return num1, num3
    elif num1 > num3 > num2 or num1 > num3 == num2 or num1 < num3 == num2:
        return num1, num2
    elif num2 > num1 > num3 or num2 > num3 == num1 or num2 < num3 == num1:
        return num2, num3
    elif num2 > num3 > num1 or num2 > num3 == num1 or num2 < num3 == num1:
        return num2, num1
    elif num3 > num1 > num2 or num3 > num1 == num2 or num3 < num1 == num2:
        return num3, num2
    elif num3 > num2 > num1 or num3 > num1 == num2 or num3 < num1 == num2:
        return num3, num1


def check_largest_and_smallest():
    x1 = largest_and_smallest(17, 1, 6)
    x2 = largest_and_smallest(1, 17, 6)
    x3 = largest_and_smallest(1, 1, 2)
    x4 = largest_and_smallest(1, 1, 1)
    x5 = largest_and_smallest(-1, 0, 2)
    if (x1 == 17, 1) and (x2 == 17, 1) and (x3 == 2, 1) and (x4 == 1, 1) and (x5 == 2, -1):
        return True
    else:
        return False
