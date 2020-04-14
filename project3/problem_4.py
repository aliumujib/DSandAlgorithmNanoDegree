def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    print(len(input_list))

    result = __sort_012__(input_list, 0, 0, len(input_list) - 1)
    return result


def swap(array, first_index, second_index):
    temp = array[first_index]
    array[first_index] = array[second_index]
    array[second_index] = temp


def __sort_012__(input_list, low, mid, high):
    if mid >= high:
        return input_list
    else:
        element = input_list[mid]
        if element == 0:
            swap(input_list, mid, low)
            mid = mid + 1
            low = low + 1
        elif element == 1:
            mid = mid + 1
        elif element == 2:
            swap(input_list, mid, high)
            high = high - 1

        print("{} {} {} {}".format(mid, low, high, input_list))
        return __sort_012__(input_list, low, mid, high)


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print("{} {}".format(sorted_array, sorted(test_case)))
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
