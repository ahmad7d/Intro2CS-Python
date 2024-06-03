from ex7_helper import add, subtract_1, is_odd, divide_by_2, append_to_end
from typing import List, Any


def mult(x: float, y: int) -> float:
    if y == 0:
        return 0
    return add(x, mult(x, subtract_1(y)))


def is_even(n: int) -> bool:
    if n == 0:
        return True
    elif n == 1:
        return False
    else:
        return not is_even(subtract_1(n))


def log_mult(x: float, y: int) -> float:
    if y == 0:
        return 0
    n = log_mult(x, divide_by_2(y))
    if not is_odd(y):
        return add(n, n)
    else:
        return add(x, add(n, n))


def is_power(b: int, x: int) -> bool:
    if b == 1 or b == 0:
        return b == x
    elif x == 1:
        return True
    return is_power_helper(x, b, b)


def is_power_helper(n: int, x: int, new_x: float) -> bool:
    if n <= new_x:
        return n == new_x
    new_x = mult(new_x, x)
    return is_power_helper(n, x, new_x)


def reverse(s: str) -> str:
    return reverse_helper(s, len(s) - 1, '')


def reverse_helper(s: str, i: int, new_s: str) -> str:
    if len(s) == len(new_s):
        return new_s
    new_s = append_to_end(new_s, s[i])
    return reverse_helper(s, i - 1, new_s)


def play_hanoi(hanoi: Any, n: int, src: int, dst: int, temp: int) -> None:
    if n > 0:
        play_hanoi(hanoi, n - 1, src, temp, dst)
        hanoi.move(src, dst)
        play_hanoi(hanoi, n - 1, temp, dst, src)
    else:
        return


def number_of_ones(n: int) -> int:
    if n == 0:
        return 0
    return splitting_integer(n) + number_of_ones(n - 1)


def splitting_integer(n: int) -> int:
    if n <= 0:
        return 0
    val = 0
    d = n % 10
    if d == 1:
        val += 1
    return val + splitting_integer(n // 10)


def compare_2d_lists(l1: List[List[int]], l2: List[List[int]]) -> bool:
    if len(l1) != len(l2):
        return False
    return comparing_index(l1, l2, 0)


def compare_1d_lists(lst1: List[int], lst2: List[int], i: int) -> bool:
    if len(lst1) != len(lst2):
        return False
    if i == len(lst1):
        return True
    if lst1[i] != lst2[i]:
        return False
    return compare_1d_lists(lst1, lst2, i + 1)


def comparing_index(lst1: List[List[int]], lst2: List[List[int]], i: int) -> bool:
    if i == len(lst1):
        return True
    if not compare_1d_lists(lst1[i], lst2[i], 0):
        return False
    return comparing_index(lst1, lst2, i + 1)


# def cloning(lst: List[Any]) -> List[Any]:
#     new_lst = []
#     for i in lst:
#         new_lst.append(i)
#     return new_lst


def magic_list_helper(n: int, l: List[Any], new_l: List[Any]) -> List[Any]:
    if n == 0:
        return new_l
    new_l.append([i for i in l])
    return magic_list_helper(n - 1, new_l, new_l)


def magic_list(n: int) -> List[Any]:
    return magic_list_helper(n, [], [])
