def __rotated_array_search_recursive__(input_list, number, start, end):
    mid_point = (start + end) // 2
    # print("list: {} start: {} end: {} mid: {} search {}".format(input_list, start, end, mid_point, number))
    if input_list[mid_point] == number:
        return mid_point
    elif input_list[mid_point - 1] == number:
        return mid_point - 1
    elif input_list[mid_point + 1] == number:
        return mid_point + 1
    elif start + end > len(input_list):
        return - 1
    else:
        if number > input_list[mid_point]:
            start = mid_point - 1
        elif number < input_list[mid_point]:
            end = mid_point + 1
        else:
            return -1
    return __rotated_array_search_recursive__(input_list, number, start, end)


def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1

    Algorithm:
    find pivot: center point, (start + end )//2
    check if number > input_list[center]
        start = center - 1
    else if number < input_list[center]:
        end = center + 1
    else:
        return -1

    This is my first try at this, passed all test cases but is trash
    """
    return __rotated_array_search_recursive__(input_list, number, 0, len(input_list))


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
