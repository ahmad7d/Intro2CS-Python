from game_parameters import *
from game_display import GameDisplay
from utils import *



def get_apple_data():
    return get_random_apple_data()


def drawing_apples(gd: GameDisplay, apples_coordinates):
    if len(apples_coordinates) < 3:
        apples_coordinates.append(get_apple_data())
    for apple in apples_coordinates:
        gd.draw_cell(apple[ZERO], apple[1], GREEN)


def eating_apple(snake_coordinates, apples_coordinates):
    for apples_coordinate in apples_coordinates:
        if (apples_coordinate[ZERO], apples_coordinate[1]) in snake_coordinates:
            apples_coordinates.remove(apples_coordinate)
            return apples_coordinate[2]
    return ZERO


def snake_extension(direction, snake_coordinates):
    if direction == UP:
        return snake_coordinates[-1][ZERO], snake_coordinates[-1][1] + 1
    if direction == DOWN:
        return snake_coordinates[-1][ZERO], snake_coordinates[-1][1] - 1
    if direction == RIGHT:
        return snake_coordinates[-1][ZERO] + 1, snake_coordinates[-1][1]
    if direction == LEFT:
        return snake_coordinates[-1][ZERO] - 1, snake_coordinates[-1][1]
