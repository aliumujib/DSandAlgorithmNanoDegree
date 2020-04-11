def heapsort(arr):
    result = []
    for each in arr:
        result.append(each)
        heapify_recursive(result, len(result) - 1)


def calculate_parent_idx(end_index):
    if end_index == 0:
        return 0
    else:
        return (end_index - 1) // 2


def heapify_recursive(arr, end_index):
    """
    :param: arr - array to heapify
    n -- number of elements in the array
    i -- index of the current node
    TODO: Converts an array (in place) into a maxheap, a complete binary tree with the largest values at the top
    """

    if end_index <= 0:
        return arr

    parent_idx = calculate_parent_idx(end_index)
    print("end: {} array: {} parent: {}".format(end_index, arr, parent_idx))
    if arr[end_index] < arr[parent_idx]:
        print("Swapping {} with {}".format(arr[end_index], arr[parent_idx]))
        temp = arr[parent_idx]
        arr[parent_idx] = arr[end_index]
        arr[end_index] = temp

    end_index = end_index - 1
    return heapify_recursive(arr, end_index - 1)


def test_function(test_case):
    heapsort(test_case[0])
    print(test_case[0])
    if test_case[0] == test_case[1]:
        print("Pass")
    else:
        print("False")


# arr = [3, 7, 4, 6, 1, 0, 9, 8, 9, 4, 3, 5]
# solution = [0, 1, 3, 3, 4, 4, 5, 6, 7, 8, 9, 9]
# test_case = [arr, solution]
# test_function(test_case)

arr = [5, 5, 5, 3, 3, 3, 4, 4, 4, 4]
solution = [3, 3, 3, 4, 4, 4, 4, 5, 5, 5]
test_case = [arr, solution]
test_function(test_case)

# arr = [0, 1, 2, 5, 12, 21, 0]
# solution = [0, 0, 1, 2, 5, 12, 21]
# test_case = [arr, solution]
# test_function(test_case)
