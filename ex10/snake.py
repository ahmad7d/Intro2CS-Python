from game_display import GameDisplay
from game_parameters import *

LEFT = "Left"
RIGHT = "Right"
UP = "Up"
DOWN = "Down"
NOT_MOVING = None
HEAD_FIRST_LOCATION = [10, 10]
TAIL_FIRST_LOCATION = [10, 8]
SNEAK = [(10, 8), (10, 9), (10, 10), (10, 11), (10, 12), (10, 13), (10, 14), (10, 15)]
BLACK = "Black"
GREEN = "Green"
RED = 'Red'
ORANGE = 'Orange'
WIDTH = 40
HEIGHT = 30
ZERO = 0


def get_input(gd: GameDisplay):
    return gd.get_key_clicked()


def changing_direction(inp, direction):
    if inp == RIGHT and direction != LEFT:
        direction = RIGHT
    elif inp == LEFT and direction != RIGHT:
        direction = LEFT
    elif inp == UP and direction != DOWN:
        direction = UP
    elif inp == DOWN and direction != UP:
        direction = DOWN
    return direction


def drawing_snake(gd: GameDisplay, snake_coordinates):
    for coordinate in snake_coordinates:
        gd.draw_cell(coordinate[ZERO], coordinate[1], BLACK)


def snake_out_of_limit(coordinate):
    return False if (coordinate[0] > WIDTH - 1 or coordinate[0] < 0) \
                    or (coordinate[1] > HEIGHT - 1 or coordinate[1] < 0) else True


def checking_new_head(sneak_coordinates, bomb_coordinate):
    for coordinate in sneak_coordinates:
        if sneak_coordinates.count(coordinate) > 1 or not snake_out_of_limit(coordinate) \
                or bomb_coordinate == coordinate:
            return False
    return True


def moving_up(snake):
    del snake[0]
    return snake[-1][0], snake[-1][1] + 1


def moving_down(snake):
    del snake[0]
    return snake[-1][0], snake[-1][1] - 1


def moving_right(snake):
    del snake[0]
    return snake[-1][0] + 1, snake[-1][1]


def moving_left(snake):
    del snake[0]
    return snake[-1][0] - 1, snake[-1][1]


def moving_sneak(direction, snake):
    if direction == RIGHT:
        new_head = moving_right(snake)

        snake.append(new_head)
    if direction == LEFT:
        new_head = moving_left(snake)

        snake.append(new_head)
    if direction == UP:
        new_head = moving_up(snake)

        snake.append(new_head)
    if direction == DOWN:
        new_head = moving_down(snake)

        snake.append(new_head)
    return snake
