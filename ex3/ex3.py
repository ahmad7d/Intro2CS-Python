import math


def input_list():
    lst = []
    while True:
        inp = input()
        if inp == '':
            break
        lst.append(float(inp))
    sum_lst = 0
    for i in lst:
        sum_lst += i
    lst.append(sum_lst)
    return lst


def inner_product(vec_1, vec_2):
    if len(vec_1) != len(vec_2):
        return None
    mult_lists = 0
    for i in range(len(vec_1)):
        mult_lists += (vec_1[i] * vec_2[i])

    return mult_lists


def monotonically_rising(sequence):
    result = []
    for i in range(len(sequence) - 1):
        if sequence[i] <= sequence[i + 1]:
            result.append(True)
        else:
            result.append(False)
    if False not in result:
        return True
    return False


def hard_monotonically_rising(sequence):
    result = []
    for i in range(len(sequence) - 1):
        if sequence[i] < sequence[i + 1]:
            result.append(True)
        else:
            result.append(False)
    if False not in result:
        return True
    return False


def monotonically_descending(sequence):
    result = []
    for i in range(len(sequence) - 1):
        if sequence[i] >= sequence[i + 1]:
            result.append(True)
        else:
            result.append(False)
    if False not in result:
        return True
    return False


def hard_monotonically_descending(sequence):
    result = []
    for i in range(len(sequence) - 1):
        if sequence[i] > sequence[i + 1]:
            result.append(True)
        else:
            result.append(False)
    if False not in result:
        return True
    return False


def sequence_monotonicity(sequence):
    result = [monotonically_rising(sequence), hard_monotonically_rising(sequence),
              monotonically_descending(sequence), hard_monotonically_descending(sequence)]
    return result


def monotonicity_inverse(def_bool):
    if def_bool == [True, True, False, False]:
        return [56.5, 57.5, 63, 84]
    if def_bool == [True, False, False, False]:
        return [1, 3, 3, 4]
    if def_bool == [False, False, True, True]:
        return [7.5, 4, 3.141, 0.111]
    if def_bool == [False, False, True, False]:
        return [5, 4, 3, 3]
    if def_bool == [True, False, True, False]:
        return [1, 1, 1, 1]
    if def_bool == [False, False, False, False]:
        return [1, 0, -1, 1]
    else:
        return None


def is_prime(n):
    prime = True
    if n > 1:
        for i in range(2, int(math.sqrt(n) + 1)):
            if n % i == 0:
                prime = False
                break
    return prime


def primes_for_asafi(n):
    primes_numbers = []
    num = 2
    while len(primes_numbers) != n:
        if is_prime(num):
            primes_numbers.append(num)
        num += 1
    return primes_numbers


def sum_of_vectors(vec_lst):
    if len(vec_lst) == 0:
        return None
    sum1 = []
    for i in range(len(vec_lst[0])):
        s = 0
        for j in vec_lst:
            s += j[i]
        sum1.append(s)
    return sum1


def num_of_orthogonal(vectors):
    c = 0
    for i in range(len(vectors)):
        for j in range(i + 1, len(vectors)):
            if inner_product(vectors[i], vectors[j]) == 0:
                c += 1
    return c


def print_wallak():
    counter = 0
    for i in range(-1, 2):
        print("wallak")


print([] != None)
