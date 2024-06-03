import math

BLACK = 0
WHITE = 255


def parse_pixel(pixel):
    if pixel > WHITE:
        return WHITE
    elif pixel < BLACK:
        return BLACK
    return round(pixel)


def separate_channels(image):
    return [[[image[k][j][i] for k in range(len(image))] for j in range(len(image[0]))] for i in
            range(len(image[0][0]))]


def combine_channels(channels):
    return separate_channels(channels)


def RGB2grayscale(colored_image):
    red = colored_image[0][0][0]
    green = colored_image[0][0][1]
    blue = colored_image[0][0][2]
    return round(red * 0.299 + green * 0.587 + blue * 0.114)


def blur_kernel(size):
    return [[1 / pow(size, 2) for j in range(size)] for i in range(size)]


def apply_kernel_on_pixel(image, kernel, row, col):
    kernel_center = len(kernel) // 2
    s = 0
    for k_row in range(len(kernel)):
        desired_row = k_row - kernel_center + row
        for k_col in range(len(kernel[k_row])):
            desired_col = k_col - kernel_center + col
            if desired_row < 0 or desired_col < 0 or desired_row >= len(image) or desired_col >= len(image[0]):
                s += image[row][col] * kernel[k_row][k_col]
            else:
                s += image[desired_row][desired_col] * kernel[k_row][k_col]

    return parse_pixel(s)


def apply_kernel(image, kernel):
    kerneled_image = []

    for row in range(len(image)):
        kerneled_image.append([apply_kernel_on_pixel(image, kernel, row, col) for col in range(len(image[row]))])

    return kerneled_image


# def apply_kernel(image, kernel):
#     kerneled_image = []
#
#     for row in range(len(image)):
#         kerneled_image.append([apply_kernel_on_pixel(image, kernel, row, col) for col in range(len(image[row]))])
#
#     return kerneled_image




def bilinear_interpolation(image, y, x):
    pass