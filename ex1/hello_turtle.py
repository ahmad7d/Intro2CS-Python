#################################################################
# FILE : hello_turtle.py
# WRITER : Ahmad , ahmad_dall7 , 324059856
# EXERCISE : intro2cse ex1 2021
# DESCRIPTION: A simple program that draw 3 flowers .
# STUDENTS I DISCUSSED THE EXERCISE WITH: Mahmoud Dallasheh , basil , moeen .
# WEB PAGES I USED: https://docs.python.org/3.7/library/turtle.html
# NOTES: -
#################################################################


import turtle


def draw_petal():         # These next lines draw a petal
    turtle.down()
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(30)
    turtle.right(135)
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(30)
    turtle.right(135)


def draw_flower():         # These next lines draw a flower
    turtle.left(45)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(135)
    turtle.forward(150)


def draw_flower_and_advance():            # these next lines draw flower and making distance
    draw_flower()
    turtle.right(90)
    turtle.up()
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.down()


def draw_flower_bed():                              # these next lines draw 3 flowers
    turtle.up()
    turtle.forward(200)
    turtle.left(180)
    turtle.down()
    draw_flower_and_advance()
    draw_flower_and_advance()
    draw_flower_and_advance()


if __name__ == "__main__":                             # these next lines is the main block
    draw_flower_bed()
    turtle.done()
