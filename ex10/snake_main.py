from snake import *
from apple import *
from bomb import Bomb
from utils import *


def main_loop(gd: GameDisplay) -> None:
    score = ZERO
    apples_coordinates = []
    direction = UP
    snake_coordinates = FIRST_SNAKE_COORDINATES
    flag = True
    bomb = Bomb()
    total_score = 0
    while True:
        gd.show_score(total_score)
        inp = get_input(gd)
        drawing_snake(gd, snake_coordinates)
        direction = changing_direction(inp, direction)
        drawing_apples(gd, apples_coordinates)
        x, y, color = bomb.get_bomb_data()
        if bomb.reduce_time() > 0:
            if (x, y) not in snake_coordinates:
                gd.draw_cell(x, y, color)
        elif bomb.explode():
            coordinates, color = bomb.get_explosion_coordinates()
            for coordinate in coordinates:
                gd.draw_cell(coordinate[0], coordinate[1], color)
            for i in apples_coordinates:
                if (i[0], i[1]) in coordinates:
                    apples_coordinates.remove(i)
        else:
            bomb = Bomb()
        if not flag:
            gd.end_round()
            break
        apples = eating_apple(snake_coordinates, apples_coordinates)
        total_score += apples
        score += apples
        if score:
            snake_coordinates = [snake_extension(direction, snake_coordinates)] + snake_coordinates
            score -= 1
        snake_coordinates = moving_sneak(direction, snake_coordinates)
        for coordinate in bomb.get_curr_bomb_coords():
            if not flag:
                break
            if not checking_new_head(snake_coordinates, (coordinate[0], coordinate[1])):
                flag = False
                snake_coordinates.pop()
                drawing_snake(gd, snake_coordinates)
        gd.end_round()
