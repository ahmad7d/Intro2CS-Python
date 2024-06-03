#################################################################
# FILE : calculate_mathematical_expression.py
# WRITER : Ahmad , ahmad_dall7 , 324059856
# EXERCISE : intro2cse ex2 2021
# DESCRIPTION: A program that make a calculation for two numbers.
# STUDENTS I DISCUSSED THE EXERCISE WITH: -
# WEB PAGES I USED:-
# NOTES: -
#################################################################
def calculate_mathematical_expression(num1, num2, operation):
    if num2 == 0 and operation == '/' or operation != '+' and operation != '-'\
            and operation != '*' and operation != '/':
        return None
    elif operation == '*':
        return num1 * num2
    elif operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '/':
        return num1 / num2


def calculate_from_string(process):
    expression = process.split()
    calculation = expression[1]
    return calculate_mathematical_expression(float(expression[0]), float(expression[2]), calculation)
