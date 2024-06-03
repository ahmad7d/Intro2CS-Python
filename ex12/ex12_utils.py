import functools
import math
import boggle_board_randomizer

BOARD_WIDTH = 4
BOARD_HEIGHT = 4
ZERO = 0
ONE = 1


def read_words(filename):
    word_dict = dict()
    with open(filename, 'r') as file:
        for word in file:
            word_dict[word[:-1]] = ZERO
    return word_dict


def get_word(word_coordinates, board):
    new_word = ''
    for cor in word_coordinates:
        new_word += board[cor[ZERO]][cor[ONE]]
    return new_word


def is_valid_word(word, words):
    return True if word in words else False


def is_valid_path(board, path, words):
    if False in [False for i in range(len(path) - ONE) if abs(path[i + ONE][ZERO] - path[i][ZERO]) > ONE
                                                          or abs(path[i + ONE][ONE] - path[i][ONE]) > ONE] \
            + [False for cor in path if cor[ZERO] >= len(board)
                                        or cor[ONE] >= len(board[0]) or cor[ZERO] < ZERO or cor[ONE] < ZERO]:
        return None
    word = get_word(path, board)
    return word if is_valid_word(word, words) else None


# board = [['A', 'B', 'C', 'D'],
#          ['E', 'F', 'G', 'H'],
#          ['I', 'J', 'K', 'L'],
#          ['M', 'N', 'O', 'P']
# ]
# cor = [(0, 0), (0, 1), (1, 1), (0, 0)]
# words = ['ahmad', 'ABFA']
# print(is_valid_path(board, cor, words))

def filter_word(words):
    subsets = map(lambda w: add_subset(w), words)
    new_words = set().union(*subsets)
    return new_words


def add_subset(word):
    def add_to(a, b):
        ab = a + b
        new_l.add(ab)
        return ab

    new_l = set()
    functools.reduce(add_to, word, '')
    return new_l


def find_length_n_paths(n, board, words):
    filtered_words = filter_word(words)
    return search_word(board, filtered_words, n, words, True)


def search_word(board, filtered_words, n, words, flag):
    new_words = []
    for i in range(len(board)):
        for j in range(len(board[ZERO])):
            search_word_helper(board, i, j, filtered_words, n, '', [], new_words, words, flag)
    return new_words


def search_word_helper(board, i, j, filtered_words, n, word, cor_lst, new_words, words, flag1):
    if i < ZERO or i >= len(board) or j >= len(board[0]) or j < ZERO:
        return []
    cor_lst.append((i, j))
    if len(set(cor_lst)) != len(cor_lst):
        return []
    word += board[i][j]
    flag2 = cor_lst if flag1 else word
    if word not in filtered_words or len(flag2) > n:
        return []
    if len(flag2) == n and word in words:
        # print(word, n, flag2)
        new_words.append(cor_lst)
        return
    search_word_helper(board, i, j + 1, filtered_words, n, word, cor_lst[:], new_words, words, flag1)
    search_word_helper(board, i, j - 1, filtered_words, n, word, cor_lst[:], new_words, words, flag1)
    search_word_helper(board, i + 1, j, filtered_words, n, word, cor_lst[:], new_words, words, flag1)
    search_word_helper(board, i - 1, j, filtered_words, n, word, cor_lst[:], new_words, words, flag1)
    search_word_helper(board, i + 1, j + 1, filtered_words, n, word, cor_lst[:], new_words, words, flag1)
    search_word_helper(board, i + 1, j - 1, filtered_words, n, word, cor_lst[:], new_words, words, flag1)
    search_word_helper(board, i - 1, j + 1, filtered_words, n, word, cor_lst[:], new_words, words, flag1)
    search_word_helper(board, i - 1, j - 1, filtered_words, n, word, cor_lst[:], new_words, words, flag1)


def find_length_n_words(n, board, words):
    filtered_words = filter_word(words)
    return search_word(board, filtered_words, n, words, False)


def get_all_cords(board, words):
    return [path for paths in [find_length_n_paths(i, board, words) for i in range(2, 16)] for path in paths]


def add_dict(words):
    return {word: (ZERO, []) for word in words}


def calculate_score(board, words, paths):
    d = add_dict(words)
    for path in paths:
        word = ''
        for cor in path:
            word += board[cor[ZERO]][cor[ONE]]
        score_path = pow(len(path), 2)
        if score_path > d[word][ZERO]:
            d[word] = score_path, path
    return d


def max_score_paths(board, words):
    paths = get_all_cords(board, words)
    d = calculate_score(board, words, paths)
    return [d[word][ONE] for word in d if d[word][ZERO]]


board = [
        ['AB', 'CD', 'E', 'F'],
         ['Z', 'Y', 'X', 'W'],
         ['A', 'B', 'C', 'D'],
         ['Z', 'YX', 'WV', 'U']
]

words = 'ABCDEFWXYZABCDUWVYXZ'
print(find_length_n_paths(20, board, words))

# board = [['I', 'E', 'O', 'O'],
#          ['N', 'J', 'U', 'Q'],
#          ['E', 'P', 'E', 'G'],
#          ['W', 'QU', 'Y', 'P']]
#
# words_lst = ["ahmad", "JWS", "PEG", '', 'EG', 'IE', 'IEJNEP', 'QUYP', 'JPQU', 'QU']
# words_dc = {"ahmad": 0, "JWS": 0, "PEG": 0, '': 0, 'EG': 0, 'IE': 0, 'IEJNEP': 0, 'QUYP': 0, 'JPQU': 0, 'QU': 0}

# print(l)
# h = []
# for path in l:
#     s = ''
#     for cor in path:
#         s += board[cor[ZERO]][cor[ONE]]
#     h.append(s)
#
# print(h)
# print(board[2][1])
# board = [['T', 'D', 'D', 'N'],
#  ['C', 'T', 'E', 'O'],
#  ['S', 'E', 'S', 'N'],
#  ['E', 'D', 'U', 'F']]

# words = read_words('boggle_dict.txt')
#
#
# l = max_score_paths(board, words)
#
#
#
#
# words = []
# for path in l:
#     new_word = ''
#     new_word += get_word(path, board)
#     words.append(new_word)
# print(words)
