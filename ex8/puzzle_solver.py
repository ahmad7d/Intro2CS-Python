from typing import List, Tuple, Set, Optional


# We define the types of a partial picture and a constraint (for type checking).
Picture = List[List[int]]
Constraint = Tuple[int, int, int]
WHITE, BLACK, EMPTY = 1, 0, -1
GAME_VALUES = [WHITE, BLACK]


def get_relevant_constraints(constraints_set: Set[Tuple[int, int, int]], row: int,
                             col: int) -> Set[Tuple[int, int, int]]:
    return {constraint for constraint in constraints_set
            if constraint[0] == row or constraint[1] == col}


def init_picture(n: int, m: int) -> List[List[int]]:
    return [[EMPTY for _ in range(m)] for _ in range(n)]


def has_empty_cell(picutre: List[List[int]]):
    for row in picutre:
        for cell in row:
            if cell == EMPTY:
                return True
    return False


def seen_cells_row(picture: List[List[int]], row: int, col: int, as_white: bool) -> int:
    def count(start, end, step):
        c = 0
        for i in range(start, end, step):
            if picture[row][i] == BLACK or (not as_white and picture[row][i] == EMPTY):
                break
            c += 1
        return c

    return count(col + 1, len(picture[0]), 1) + count(col - 1, -1, -1)


def seen_cells_col(picture: List[List[int]], row: int, col: int, as_white: bool) -> int:
    def count(start, end, step):
        c = 0
        for i in range(start, end, step):
            if picture[i][col] == BLACK or (not as_white and picture[i][col] == EMPTY):
                break
            c += 1
        return c

    return count(row + 1, len(picture), 1) + count(row - 1, -1, -1)


def max_seen_cells(picture: List[List[int]], row: int, col: int) -> int:
    return (seen_cells_row(picture, row, col, True) +
            seen_cells_col(picture, row, col, True) + 1) if picture[row][col] != BLACK else 0


def min_seen_cells(picture: List[List[int]], row: int, col: int) -> int:
    return (seen_cells_row(picture, row, col, False) +
            seen_cells_col(picture, row, col, False) + 1) if picture[row][col] == WHITE else 0


def check_constraints(picture: List[List[int]], constraints_set: Set[Tuple[int, int, int]]) -> int:
    all_good = True
    for constraint in constraints_set:
        min_seen = min_seen_cells(picture, constraint[0], constraint[1])
        max_seen = max_seen_cells(picture, constraint[0], constraint[1])
        if constraint[2] > max_seen or constraint[2] < min_seen:
            return 0
        elif min_seen != max_seen and all_good:
            all_good = False

    return 1 if all_good else 2


def solve_puzzle(constraints_set: Set[Tuple[int, int, int]], n: int, m: int) -> Optional[List[List[int]]]:
    picture = init_picture(n, m)
    for constraint in constraints_set:
        picture[constraint[0]][constraint[1]] = WHITE if constraint[2] > 0 else BLACK

    if puzzle_ok(picture, constraints_set, 0, 0):
        return picture
    return None


def puzzle_ok(picture: List[List[int]], constraints_set: Set[Tuple[int, int, int]], row: int, col: int) -> bool:
    relevant_constraints = get_relevant_constraints(constraints_set, row, col)

    if col == len(picture[0]):
        return puzzle_ok(picture, constraints_set, row + 1, 0)
    elif row < len(picture):
        if picture[row][col] != EMPTY:
            return puzzle_ok(picture, constraints_set, row, col + 1)
        else:
            for v in GAME_VALUES:
                picture[row][col] = v
                if check_constraints(picture, relevant_constraints) > 0 and puzzle_ok(picture,
                                                                                      constraints_set, row, col + 1):
                    return True
                picture[row][col] = EMPTY
    if check_constraints(picture, relevant_constraints) == 0 or has_empty_cell(picture):
        return False
    return True


def has_constraint(constraints_set: Set[Tuple[int, int, int]], row: int, col: int) -> bool:
    for constraint in constraints_set:
        if row == constraint[0] and col == constraint[1]:
            return True
    return False


def how_many_solutions(constraints_set: Set[Tuple[int, int, int]], n: int, m: int) -> int:
    picture = solve_puzzle(constraints_set, n, m)
    return 0 if picture is None else count_solutions(picture, constraints_set, 0, 0) + 1


def count_solutions(picture: List[List[int]], constraints_set: Set[Tuple[int, int, int]],
                    row: int, col: int) -> int:
    c = 0
    if col == len(picture[0]):
        return count_solutions(picture, constraints_set, row + 1, 0)
    elif row < len(picture):
        if has_constraint(constraints_set, row, col):
            return count_solutions(picture, constraints_set, row, col + 1)
        c += count_solutions(picture, constraints_set, row, col + 1)
        temp = picture[row][col]
        picture[row][col] = WHITE if picture[row][col] == BLACK else BLACK
        if check_constraints(picture, constraints_set):
            c += 1 + count_solutions(picture, constraints_set, row, col + 1)
        picture[row][col] = temp
    return c


def generate_puzzle(picture: List[List[int]]) -> Set[Tuple[int, int, int]]:
    constraints = set()
    for row in range(len(picture)):
        for col in range(len(picture)):
            constraints.add((row, col, max_seen_cells(picture, row, col)))

    return constraints
