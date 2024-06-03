#################################################################
# FILE : temperature.py
# WRITER : Ahmad , ahmad_dall7 , 324059856
# EXERCISE : intro2cse ex2 2021
# DESCRIPTION: A program that check if the temperature for the next days higher or lower.
# STUDENTS I DISCUSSED THE EXERCISE WITH: -
# WEB PAGES I USED:-
# NOTES: -
#################################################################
def is_it_summer_yet(temp, temp1, temp2, temp3):
    return (temp < temp1 and temp < temp2) or (temp < temp2 and temp < temp3) or (temp < temp1 and temp < temp3)
