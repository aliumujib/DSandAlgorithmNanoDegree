def first_and_last_index(arr, number):
    """
    Given a sorted array that may have duplicate values, use binary
    search to find the first and last indexes of a given value.

    Args:
        arr(list): Sorted array (or Python list) that may have duplicate values
        number(int): Value to search for in the array
    Returns:
        a list containing the first and last indexes of the given value
    """

    # TODO: Write your first_and_last function here
    # Note that you may want to write helper functions to find the start
    # index and the end index
    bin_occurence = find_number_recursively(arr, number, 0, len(arr) - 1)
    print(bin_occurence)
    first = find_first_index_recursively(arr, number, bin_occurence)
    last = find_last_index_recursively(arr, number, bin_occurence)
    print([first, last])
    return [first, last]


def find_first_index_recursively(arr, number, index):
    if index <= 0:
        return index
    elif arr[index - 1] != number:
        return index
    else:
        return find_first_index_recursively(arr, number, index - 1)


def find_last_index_recursively(arr, number, index):
    if index == len(arr) - 1:
        return index
    elif arr[index + 1] != number:
        return index
    else:
        return find_last_index_recursively(arr, number, index + 1)


def find_number_recursively(arr, number, start, end):
    middle = (start + end)//2
    if arr[middle] == number:
        return middle
    else:
        if middle >= end:
            return -1
        elif number > arr[middle]:
            return find_number_recursively(arr, number, middle+1, end)
        elif number < arr[middle]:
            return find_number_recursively(arr, number, middle-1, end)
