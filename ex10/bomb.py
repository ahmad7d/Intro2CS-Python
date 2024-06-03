from game_parameters import *
from utils import *
from utils import *


def in_range(p):
    return ZERO <= p[ZERO] <= WIDTH - 1 and 0 <= p[1] <= HEIGHT - 1


def get_neighbors(p):
    return {neighbor for neighbor in [(p[ZERO] - 1, p[1]), (p[ZERO] + 1, p[1]), (p[ZERO], p[1] - 1),
                                      (p[ZERO], p[1] + 1), p] if in_range(neighbor)}


def get_explosive_points(p, r):
    explosive_coord = [{p}]
    for i in range(r):
        neighbors = set()
        for point in explosive_coord[i]:
            neighbors = neighbors.union(get_neighbors(point))
        neighbors -= explosive_coord[i]
        if i - 1 >= ZERO:
            neighbors -= explosive_coord[i - 1]
        explosive_coord.append(neighbors)

    return explosive_coord


class Bomb:

    def __init__(self):
        self.__x, self.__y, self.__radius, self.__time = get_random_bomb_data()
        self.__stage = 0
        self.__coordinates = get_explosive_points((self.__x, self.__y), self.__radius)

    def get_bomb_data(self):
        return self.__x, self.__y, RED

    def get_curr_bomb_coords(self):
        return self.__coordinates[self.__stage]

    def reduce_time(self):
        self.__time -= 1
        return self.__time

    def explode(self):
        self.__radius -= 1
        self.__stage += 1
        return self.__radius

    def get_explosion_coordinates(self):
        return self.__coordinates[self.__stage], ORANGE

    def first_radius_coordinate(self):
        return self.__x, self.__y

    def second_radius_coordinate(self):
        pass

    def get_radius(self):
        return self.__radius
