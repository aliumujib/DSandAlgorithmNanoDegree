import random


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    return __get_min_max__(ints, (ints[0], ints[0]), 0)


def __get_min_max__(ints, results, index):
    if index >= len(ints) - 1:
        print(results)
        return results
    else:
        value = ints[index]
        if value < results[0]:
            results = (value, results[1])
        if value > results[1]:
            results = (results[0], value)
        index = index + 1
        return __get_min_max__(ints, results, index)


l1 = [i for i in range(0, 10)]
random.shuffle(l1)

l2 = [i for i in range(20, 40)]
random.shuffle(l2)

l3 = [i for i in range(40, 90)]
random.shuffle(l3)

l4 = [1, 0, 0, 0, 1, 0, 0, 1]
random.shuffle(l4)

print("Pass" if ((0, 9) == get_min_max(l1)) else "Fail")
print("Pass" if ((20, 39) == get_min_max(l2)) else "Fail")
print("Pass" if ((40, 89) == get_min_max(l3)) else "Fail")
print("Pass" if ((0, 1) == get_min_max(l4)) else "Fail")
