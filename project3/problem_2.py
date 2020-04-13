def binary_search(input_list, target, start, end):
    mid = (start + end) // 2

    if input_list[mid] == target:
        return mid
    elif start == end:
        return - 1
    else:
        if input_list[mid] > target:
            end = mid - 1
        elif input_list[mid] < target:
            start = mid + 1
    return binary_search(input_list, target, start, end)


def find_pivot_item(input_list, mid_point, iterations):
    if input_list[mid_point + 1] < input_list[mid_point]:
        return mid_point
    else:
        mid_point = mid_point - 1
        iterations = iterations + 1
        return find_pivot_item(input_list, mid_point, iterations)


def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1

    Algorithm:
    find pivot
        pivot is the item whose element to the left is > than it's value.

    if item is pivot, return pivot index
    split array in two based on pivot. if the element at index 0 < target, using binary search, search left array
    otherwise search the right array
    """
    pivot = find_pivot_item(input_list, (0 + len(input_list) - 1) // 2, 0)
    if input_list[pivot] == number:
        return pivot
    else:
        if number >= input_list[0]:
            return binary_search(input_list, number, 0, pivot - 1)
        else:
            return binary_search(input_list, number, pivot + 1, len(input_list) - 1)


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


assert find_pivot_item([6, 7, 8, 9, 10, 1, 2, 3, 4], 4, 0) == 4
assert find_pivot_item([6, 7, 8, 1, 2, 3, 4], 4, 0) == 2

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
