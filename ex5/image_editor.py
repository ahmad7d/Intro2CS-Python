#################################################################
# FILE : image_editor.py
# WRITER : your_name , your_login , your_id
# EXERCISE : intro2cs ex5 2022-2023
# DESCRIPTION: A simple program that...
# STUDENTS I DISCUSSED THE EXERCISE WITH: Bugs Bunny, b_bunny.
#								 	      Daffy Duck, duck_daffy.
# WEB PAGES I USED: www.looneytunes.com/lola_bunny
# NOTES: ...
#################################################################
import sys

##############################################################################
#                                   Imports                                  #
##############################################################################
from ex5_helper import *
from typing import Optional
from math import *
from sys import *

##############################################################################
#                                  Functions                                 #
##############################################################################

USER_INP_GREY_SCALE = 1
USER_INP_BLURRING = 2
USER_INP_RESIZE = 3
USER_INP_ROTATE = 4
USER_INP_GET_EDGES = 5
USER_INP_QUANTIZE = 6
USER_INP_SHOW = 7
USER_INP_EXIT = 8



COMMA = ','


def separate_channels(image: ColoredImage) -> List[SingleChannelImage]:
    lst1 = []
    for i in range(len(image[0][0])):
        lst2 = []
        for j in range(len(image)):
            lst3 = []
            for k in range(len(image[0])):
                lst3.append(image[j][k][i])
            lst2.append(lst3)
        lst1.append(lst2)
    return lst1


def combine_channels(channels: List[SingleChannelImage]) -> ColoredImage:
    lst1 = []
    for i in range(len(channels[0])):
        lst2 = []
        for k in range(len(channels[0][0])):
            lst3 = []
            for j in range(len(channels)):
                lst3.append(channels[j][i][k])
            lst2.append(lst3)
        lst1.append(lst2)
    return lst1


def RGB2grayscale(colored_image: ColoredImage) -> SingleChannelImage:
    lst1 = []
    for i in range(len(colored_image)):
        lst2 = []
        for j in range(len(colored_image[i])):
            r = colored_image[i][j][0] * 0.299
            g = colored_image[i][j][1] * 0.587
            b = colored_image[i][j][2] * 0.114
            m = round(r + g + b)
            lst2.append(m)
        lst1.append(lst2)
    return lst1


def blur_kernel(size: int) -> Kernel:
    lst1 = []
    for i in range(size):
        lst2 = []
        for j in range(size):
            lst2.append(1 / size ** 2)
        lst1.append(lst2)
    return lst1


def get_pixel_limit(pixel):
    if pixel > 255:
        return 255
    elif pixel < 0:
        return 0
    else:
        return round(pixel)


def apply_kernel_helper(image, kernel, row, col, kernel_center, s):
    rows = len(image)
    cols = len(image[0])
    for i, kernel_row in enumerate(kernel):
        for j, kernel_col in enumerate(kernel_row):
            desired_row = i - kernel_center + row
            desired_col = j - kernel_center + col
            s += image[row][col] * kernel_col if desired_row < 0 or desired_col < 0 or desired_row >= rows or\
                                                 desired_col >= cols else image[desired_row][desired_col] * kernel_col
    return s


def apply_kernel(image, kernel):
    return [
        [get_pixel_limit(apply_kernel_helper(image, kernel, i, j, len(kernel) // 2, 0)) for j in range(len(image[i]))]
        for i in range(len(image))]


def bilinear_interpolation(image: SingleChannelImage, y: float, x: float) -> int:
    b_x = [floor(x), ceil(x)]
    b_y = [floor(y), ceil(y)]

    return get_pixel_limit(image[b_y[0]][b_x[0]] * (1 - (x - b_x[0])) * (1 - (y - b_y[0]))
                           + image[b_y[1]][b_x[0]] * (y - b_y[0]) * (1 - (x - b_x[0]))
                           + image[b_y[0]][b_x[1]] * (x - b_x[0]) * (1 - (y - b_y[0]))
                           + image[b_y[1]][b_x[1]] * (x - b_x[0]) * (y - b_y[0]))


def resize(image, new_height, new_width):
    new_image_i = []
    new_image = []
    old_height = len(image)
    old_width = len(image[0])
    num_channels = len(image[0])
    if (old_height == new_height and old_width == new_width):
        return image
    resize_factor_row = ((old_height - 1) / (new_height - 1))
    resize_factor_col = ((old_width - 1) / (new_width - 1))

    # new_image = [[[0] * num_channels] * new_width for i in range(new_height)]
    for i in range(new_height):
        for j in range(new_width):
            new_row_index = i * resize_factor_row
            new_col_index = j * resize_factor_col
            new_pixel = bilinear_interpolation(image, new_row_index, new_col_index)
            new_image_i.append(new_pixel)
        new_image.append(new_image_i)
        new_image_i = []
    return new_image


def rotate_90(image: Image, direction: str) -> Image:
    if direction == 'R':
        return [[image[len(image) - 1 - j][i] for j in range(len(image))] for i in range(len(image[0]))]
    elif direction == 'L':
        return [[image[j][len(image[0]) - 1 - i] for j in range(len(image))] for i in range(len(image[0]))]


def get_edges(image: SingleChannelImage, blur_size: int, block_size: int, c: float) -> SingleChannelImage:
    blur_image = apply_kernel(image, blur_kernel(blur_size))
    threshold = apply_kernel(blur_image, blur_kernel(block_size))
    new_image = deepcopy(image)
    for i in range(len(blur_image)):
        for j in range(len(blur_image[0])):
            if threshold[i][j] > blur_image[i][j]:
                new_image[i][j] = 0
            else:
                new_image[i][j] = 255
    return new_image


def quantize(image: SingleChannelImage, N: int) -> SingleChannelImage:
    copied_image = deepcopy(image)
    lst1 = []
    for i in range(len(copied_image)):
        lst2 = []
        for j in range(len(copied_image[i])):
            copied_image[i][j] = round(floor(copied_image[i][j] * N / 256) * 255 / (N - 1))
            lst2.append(copied_image[i][j])
        lst1.append(lst2)
    return lst1


def quantize_colored_image(image: ColoredImage, N: int) -> ColoredImage:
    lst1 = []
    s = separate_channels(image)
    for row in range(len(s)):
        q = quantize(s[row], N)
        lst1.append(q)
    return combine_channels(lst1)


def check_user_input_kernel(size):
    if size < 0 or size % 2 == 0 or isinstance(size, int) is not True:
        return False
    return True


def check_user_input_resize(user_input):
    height, width = user_input.split(COMMA)
    if height.isdigit() and width.isdigit():
        i_height = int(height)
        i_width = int(width)
        if i_height > 1 and i_width > 1:
            return i_height, i_width
    return 0, 0


def check_user_input_get_edges(user_input):
    blur_size, block_size, c = user_input.split(COMMA)
    if blur_size.isdigit() and block_size.isdigit() and c.isdigit():
        i_blur_size = int(blur_size)
        i_block_size = int(block_size)
        i_c = float(c)
        if i_c >= 0 and i_blur_size % 2 != 0 and i_block_size % 2 != 0:
            return i_blur_size, i_block_size, i_c
    return 0, 0, 0


def check_user_input_quantize(user_input):
    if user_input.isdigit():
        quantize_num = int(user_input)
        if quantize_num > 1:
            return quantize_num
    return 0


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Invalid args')
    else:
        image_path = sys.argv[1]
        image = load_image(image_path)
        while True:
            user_input = int(input("please choose any number : "))
            if user_input == USER_INP_GREY_SCALE:
                if isinstance(image[0][0], List):
                    image = RGB2grayscale(image)
                else:
                    print("its allready grey !")

            elif user_input == USER_INP_BLURRING:
                while True:
                    kernel_size = int(input("please insert kernel size : "))
                    if check_user_input_kernel(kernel_size) is False:
                        continue
                    separated_image = separate_channels(image)
                    for i in range(len(separated_image)):
                        separated_image[i] = apply_kernel(separated_image[i], blur_kernel(kernel_size))
                    image = combine_channels(separated_image)
            elif user_input == USER_INP_RESIZE:
                two_values = input("please insert image height,width : ")
                height, width = check_user_input_resize(two_values)
                if height == 0 and width == 0:
                    print("Invalid height width ! ")
                    continue
                image = resize(image, height, width)
            elif user_input == USER_INP_ROTATE:
                direction = input("please insert direction (L, R)")
                if direction == "R" or direction == "L":
                    image = rotate_90(image, direction)
                else:
                    print("Invalid direction !")
            elif user_input == USER_INP_GET_EDGES:
                three_values = input("Insert three values , blur size , block size , c : ")
                values = check_user_input_get_edges(three_values)
                if values[0] == 0 and values[1] == 0 and values[2] == 0:
                    print("Invalid values ! ")
                else:
                    if isinstance(image[0][0], List):
                        image = RGB2grayscale(image)
                    image = get_edges(image, values[0], values[1], values[2])
            elif user_input == USER_INP_QUANTIZE:
                quantize_num = input("Insert quantize num : ")
                i_quantize_num = check_user_input_quantize(quantize_num)
                if i_quantize_num == 0:
                    print("Invalid input !")
                else:
                    if not isinstance(image[0][0], List):
                        image = quantize(image, i_quantize_num)
                    else:
                        image = quantize_colored_image(image, i_quantize_num)
            elif user_input == USER_INP_SHOW:
                show_image(image)

            elif user_input == USER_INP_EXIT:
                break

        path_input = input("Insert path ")
        save_image(image, path_input)
