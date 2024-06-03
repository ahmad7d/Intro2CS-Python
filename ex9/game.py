import sys
from helper import *
from board import *
from car import *
import re

POSSIBLE_LENGTHS = [2, 3, 4]
POSSIBLE_NAMES = ['Y', 'R', 'B', 'O', 'G', 'W']
ORIENTATION = [0, 1]


class Game:
    """
    Add class description here
    """

    def __init__(self, board):
        self.board = board

    def __single_turn(self):
        print("get the red car out the park \t choose the car and the direction to move the car"
              " \t press ! to end the game : ")
        user_input = input()
        if user_input == "!":
            return False
        matched = re.match("^((B|R|O|W|Y|G),(u|d|l|r))$", user_input)
        if bool(matched):
            if self.board.move_car(user_input[0], user_input[2]):
                print("the car has been moved")
            else:
                print("wrong way !")
        else:
            print("invalid input")
        return True

    def play(self):
        while self.board.cell_content((3, 7)) is None:
            print(self.board)
            if not self.__single_turn():
                print("game over")
                return
        print(self.board)
        print("you won")


def main():
    if len(sys.argv) != 2:
        return
    cars_dict = load_json(sys.argv[1])
    board = Board()
    for car_name, details in cars_dict.items():
        if car_name in POSSIBLE_NAMES and details[0] in POSSIBLE_LENGTHS and details[2] in ORIENTATION:
            car = Car(car_name, details[0], (details[1][0], details[1][1]), details[2])
            board.add_car(car)
    game = Game(board)
    game.play()


if __name__ == "__main__":
    main()
