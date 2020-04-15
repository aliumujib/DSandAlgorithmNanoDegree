import random


def __get_min_max_recursive__(ints, results, index):
    if index > len(ints) - 1:
        print(results)
        return results
    else:
        value = ints[index]
        if value < results[0]:
            results = (value, results[1])
        if value > results[1]:
            results = (results[0], value)
        index = index + 1
        return __get_min_max_recursive__(ints, results, index)


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    #    return __get_min_max_recursive__(ints, (ints[0], ints[0]), 0)

    return __get_min_max_div_and_conquer__(ints)


def __compare__(left, right):
    max_left = max_val(left)
    min_left = min_val(left)

    max_right = max_val(right)
    min_right = min_val(right)

    maximum = None
    minimum = None

    if max_left > max_right:
        maximum = max_left

    if max_right > max_left:
        maximum = max_right

    if min_left < min_right:
        minimum = min_left

    if min_right < min_left:
        minimum = min_right

    if max_left == max_right:
        maximum = max_left

    if min_left == min_right:
        minimum = min_left

    return minimum, maximum


def max_val(array):
    if array[0] > array[1]:
        return array[0]
    elif array[1] > array[0]:
        return array[1]
    elif array[0] == array[1]:
        return array[0]


def min_val(array):
    if array[0] < array[1]:
        return array[0]
    elif array[1] < array[0]:
        return array[1]
    elif array[0] == array[1]:
        return array[0]


def __get_min_max_div_and_conquer__(ints):
    if len(ints) == 2:
        return ints
    elif len(ints) == 1:
        ints.append(ints[0])
        return ints

    mid = (len(ints)) // 2
    left = ints[mid:]
    right = ints[:mid]

    left = __get_min_max_div_and_conquer__(left)
    right = __get_min_max_div_and_conquer__(right)

    res = __compare__(left, right)
    return res


l1 = [i for i in range(0, 10)]
random.shuffle(l1)

l2 = [i for i in range(20, 40)]
random.shuffle(l2)

l3 = [i for i in range(40, 90)]
random.shuffle(l3)

l4 = [1, 0, 0, 0, 1, 0, 0, 1]
random.shuffle(l4)

# print(l1)
# print(_get_min_max_div_and_conquer(l1))

print("Pass" if ((0, 9) == get_min_max(l1)) else "Fail")
print("Pass" if ((20, 39) == get_min_max(l2)) else "Fail")
print("Pass" if ((40, 89) == get_min_max(l3)) else "Fail")
print("Pass" if ((0, 1) == get_min_max(l4)) else "Fail")
