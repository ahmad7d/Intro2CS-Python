import boggle_board_randomizer
from ex12_utils import *
from GUI import *
from boggle_board_randomizer import *


if __name__ == '__main__':
    board = boggle_board_randomizer.randomize_board()
    words = read_words('boggle_dict.txt')
    # print(board)
    menu = Menu()
    if menu.run_game():
        boggle = Boggle(board, words)
        boggle.run()


