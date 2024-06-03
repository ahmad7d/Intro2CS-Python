from helper import *

YES = 'Y'
NO = 'N'

INVALID_INPUT_MSG = "Invalid input !"
CORD_MSG = "enter the cordinates of the top of the ship, the ship size is "
ANOTHER_ROUND_MSG = "do you wanna play another round ? "
HIT_LOCATION_MSG = "choose hit location : "
MIN_CORD_LEN = 2
MAX_CORD_LEN = 3
ONE = 1
ZERO = 0
MIN_LETTER = 65
MAX_LETTER = 90
MAX_NUMBER = 99

def init_board(rows, columns):
    board_rows = []
    for i in range(rows):
        board_cols = []
        for j in range(columns):
            board_cols.append(WATER)
        board_rows.append(board_cols)
    return board_rows


def cell_loc(name):
    if len(name) < MIN_CORD_LEN or len(name) > MAX_CORD_LEN:
        return None
    letter = name[0]
    if letter.islower():
        letter = letter.upper()
    letter = ord(letter)

    number = int(name[1:]) if is_int(name[1:]) else None
    if not number:
        return None
    if (MIN_LETTER <= letter <= MAX_LETTER) and (ONE <= number <= MAX_NUMBER):
        return number - ONE, letter % MIN_LETTER
    else:
        return None


def valid_ship(board, size, loc):
    loc_row, loc_col = loc
    num_rows = len(board)
    num_cols = len(board[ZERO])
    if loc_row > num_rows or loc_col > num_cols:
        return False
    if num_rows < size + loc_row or num_cols < loc_col:
        return False
    for i in range(size):
        if board[loc_row + i][loc_col] != WATER:
            return False

    return True


def create_player_board(rows, columns, ship_sizes):
    board = init_board(rows, columns)
    for ship in ship_sizes:
        while True:
            print_board(board)
            cordinates = get_input(
                CORD_MSG + str(ship) + ' : ')
            cordinates = cell_loc(cordinates)
            if cordinates is None:
                print(INVALID_INPUT_MSG)
                continue
            if not valid_ship(board, ship, cordinates):
                print(INVALID_INPUT_MSG)
                continue
            for i in range(ship):
                board[cordinates[ZERO] + i][cordinates[ONE]] = SHIP
            break

    return board




def fire_torpedo(board, loc):
    hit_row, hit_col = loc
    if hit_row < len(board) or hit_col > len(board[ZERO]):
        if board[hit_row][hit_col] == WATER:
            board[hit_row][hit_col] = HIT_WATER
        if board[hit_row][hit_col] == SHIP:
            board[hit_row][hit_col] = HIT_SHIP
    return board


def get_enemy_ships_valid_locations(all_locations, enemy_board, ship_size):
    enemy_ships_valid_locations = []
    for location in all_locations:
        if valid_ship(enemy_board, ship_size, location):
            enemy_ships_valid_locations.append(location)
    return enemy_ships_valid_locations


def add_enemy_ship(enemy_board, ship_size, ship_location):
    for i in range(ship_size):
        enemy_board[ship_location[ZERO] + i][ship_location[ONE]] = SHIP


def fill_enemy_board(enemy_board, all_locations):
    for ship in SHIP_SIZES:
        enemy_ships_valid_locations = get_enemy_ships_valid_locations(all_locations, enemy_board, ship)
        enemy_ship_location = choose_ship_location(enemy_board, ship, enemy_ships_valid_locations)
        add_enemy_ship(enemy_board, ship, enemy_ship_location)


def is_empty_board(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == SHIP:
                return False
    return True


def is_valid_hit_location(hit_location, board, all_valid_locations, chosen_locations):
    if hit_location[ZERO] >= len(board) and hit_location[ONE] >= len(board[ZERO]) \
            and hit_location not in all_valid_locations and hit_location in chosen_locations:
        return False
    return True


def is_play_another_round():
    while True:
        user_input = get_input(ANOTHER_ROUND_MSG)
        if user_input == YES or user_input == NO:
            another_round = True if user_input == YES else False
            break
    return another_round


def shooting_enemy(live_board, background_board):
    for i in range(len(background_board)):
        for j in range(len(background_board[i])):
            if background_board[i][j] == HIT_SHIP or background_board[i][j] == HIT_WATER:
                live_board[i][j] = background_board[i][j]


def main():
    while True:
        player_board = create_player_board(NUM_ROWS, NUM_COLUMNS, SHIP_SIZES)
        background_enemy_board = init_board(NUM_ROWS, NUM_COLUMNS)
        enemy_board = init_board(NUM_ROWS, NUM_COLUMNS)
        all_valid_locations = [(row, col) for col in range(NUM_COLUMNS) for row in range(NUM_ROWS)]
        fill_enemy_board(background_enemy_board, all_valid_locations)
        player_chosen_locations = []
        enemy_chosen_locations = []
        while not is_empty_board(player_board) and not is_empty_board(background_enemy_board):
            print_board(player_board, enemy_board)
            player_target = cell_loc(get_input(HIT_LOCATION_MSG))
            if not player_target:
                print(INVALID_INPUT_MSG)
                continue
            if not is_valid_hit_location(player_target, background_enemy_board, all_valid_locations,
                                         player_chosen_locations):
                print(INVALID_INPUT_MSG)
                continue
            fire_torpedo(background_enemy_board, player_target)
            player_chosen_locations.append(player_target)
            # now enemy hit
            enemy_target = choose_torpedo_target(player_board,
                                                 list(set(all_valid_locations) - set(enemy_chosen_locations)))
            fire_torpedo(player_board, enemy_target)
            enemy_chosen_locations.append(enemy_target)

            shooting_enemy(enemy_board, background_enemy_board)
        print_board(player_board, background_enemy_board)  # printing the final result
        if is_play_another_round():
            continue
        else:
            break

if __name__ == '__main__':
    main()