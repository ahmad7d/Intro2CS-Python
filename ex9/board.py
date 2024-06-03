TARGET_LOCATION = 3, 7


def making_board():
    board = [['_' for j in range(7)] for i in range(7)]
    for i in range(len(board)):
        if i == 3:
            board[i].append('E')
        else:
            board[i].append('*')
    return board

class Board:
    """
    Add a class description here.
    Write briefly about the purpose of the class
    """

    def __init__(self):
        self.board = making_board()
        self.lst_cars = []

    def __str__(self):
        string = ""
        for i in range(len(self.board)):
            for coordinate in self.board[i]:
                string += coordinate + " "
            if i == 3:
                if self.cell_content(self.target_location()) is not None:
                    string += self.cell_content(self.target_location())
            string += "\n"
        return string

    def cell_list(self):
        coordinates = [(row, col) for row in range(len(self.board)) for col in range(len(self.board[0]))]
        coordinates.append(TARGET_LOCATION)
        return coordinates
    def possible_moves(self):
        result = []
        for car in self.lst_cars:
            movements = car.possible_moves()
            for key, val in movements.items():
                move_coordinate = car.movement_requirements(key)[0]
                if move_coordinate in self.cell_list() and self.cell_content(move_coordinate) is None:
                    result.append((car.get_name(), key, val))
        return result

    def target_location(self):
        return 3, 7

    def cell_content(self, coordinate):
        if coordinate == self.target_location():
            for car in self.lst_cars:
                if coordinate in car.car_coordinates():
                    return car.get_name()
            return None
        if self.board[coordinate[0]][coordinate[1]] != '_':
            return self.board[coordinate[0]][coordinate[1]]

    def add_car(self, car):
        for car_board in self.lst_cars:
            if car_board.get_name() == car.get_name():
                return False
        car_coordinates = car.car_coordinates()
        cell_list = self.cell_list()
        for coordinate in car_coordinates:
            if coordinate not in cell_list:
                return False
        for coordinate in car_coordinates:
            if self.cell_content(coordinate) is not None:
                return False
        self.lst_cars.append(car)
        for coordinate in car_coordinates:
            self.board[coordinate[0]][coordinate[1]] = car.get_name()
        return True

    def move_car(self, name, movekey):
        for car in self.lst_cars:
            if car.get_name() == name:
                possible_moves = self.possible_moves()
                for move in possible_moves:
                    if move[0] == name and move[1] == movekey:
                        self.car_move_in_board(car, movekey)
                        car.move(movekey)
                        return True
        return False

    def car_move_in_board(self, car, movekey):
        if movekey in ['r', 'd']:
            car_location = car.car_coordinates()[0]
        else:
            car_location = car.car_coordinates()[-1]
        self.board[car_location[0]][car_location[1]] = "_"
        car_movement_requirement = car.movement_requirements(movekey)[0]
        if car_movement_requirement == self.target_location():
            return
        self.board[car_movement_requirement[0]][car_movement_requirement[1]] = car.get_name()


