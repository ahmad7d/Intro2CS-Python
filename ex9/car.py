VERTICAL = 0
HORIZONTAL = 1
VERTICAL_DIR = ['u', 'd']
HORIZONTAL_DIR = ['l', 'r']


class Car:
    """
    Add class description here
    """

    def __init__(self, name, length, location, orientation):
        self.__name = name
        self.__length = length
        self.__location = location
        self.__orientation = orientation

    def car_coordinates(self):
        return [(i, self.__location[HORIZONTAL]) for i in range(self.__location[VERTICAL], self.__location[VERTICAL]
                                                                + self.__length)] \
            if self.__orientation == VERTICAL else \
            [(self.__location[VERTICAL], i) for i in range(self.__location[HORIZONTAL], self.__location[HORIZONTAL]
                                                           + self.__length)]

    def possible_moves(self):
        return {'u': 'cause the car go up', 'd': 'cause the car go down'} if self.__orientation == VERTICAL \
            else {'r': 'cause the car go right', 'l': 'cause the car go left'}

    def movement_requirements(self, movekey):
        if self.__orientation == VERTICAL and movekey in VERTICAL_DIR:
            return [(self.__location[VERTICAL] - 1, self.__location[HORIZONTAL])] if movekey == VERTICAL_DIR[0] \
                else [(self.__location[VERTICAL] + self.__length, self.__location[HORIZONTAL])]

        if self.__orientation == HORIZONTAL and movekey in HORIZONTAL_DIR:
            return [(self.__location[VERTICAL], self.__location[HORIZONTAL] - 1)] if movekey == HORIZONTAL_DIR[0] \
                else [(self.__location[VERTICAL], self.__location[HORIZONTAL] + self.__length)]

        """
        :param movekey: A string representing the key of the required move.
        :return: A list of cell locations which must be empty in order for this move to be legal.
        """
        # For example, a car in locations [(1,2),(2,2)] requires [(3,2)] to
        # be empty in order to move down (with a key 'd').
        # implement your code and erase the "pass"
        pass

    def move(self, movekey):
        if self.__orientation == VERTICAL and movekey in VERTICAL_DIR:
            if movekey == VERTICAL_DIR[0]:
                self.__location = (self.__location[VERTICAL] - 1, self.__location[HORIZONTAL])
            else:
                self.__location = (self.__location[VERTICAL] + 1, self.__location[HORIZONTAL])
        elif self.__orientation == HORIZONTAL and movekey in HORIZONTAL_DIR:
            if movekey == HORIZONTAL_DIR[0]:
                self.__location = (self.__location[VERTICAL], self.__location[HORIZONTAL] - 1)
            else:
                self.__location = (self.__location[VERTICAL], self.__location[HORIZONTAL] + 1)
        else:
            return False
        return True

    def get_name(self):
        return self.__name
