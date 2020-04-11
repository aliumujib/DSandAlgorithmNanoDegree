def count_inversions(arr):
    # TODO: Complete this function
    return merge_sort(arr)


def merge_sort(arr):
    if len(arr) <= 1:
        print("returning {}".format(arr))
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    print("L: {} R: {}".format(left, right))

    left = merge_sort(left)
    right = merge_sort(right)
    return conquer(left, right)


def conquer(left, right):
    left_index = 0
    right_index = 0
    merged = []
    count = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index = left_index + 1
        else:
            merged.append(right[right_index])
            right_index = right_index + 1

    merged += left[left_index:]
    merged += right[right_index:]


    print("merged {}".format(merged))
    print("count {}".format(count))
    return merged


def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    if count_inversions(arr) == solution:
        print("Pass")
    else:
        print("Fail")


arr = [2, 5, 1, 3, 4]
solution = 4
test_case = [arr, solution]
test_function(test_case)

arr = [54, 99, 49, 22, 37, 18, 22, 90, 86, 33]
solution = 26
test_case = [arr, solution]
test_function(test_case)


arr = [1, 2, 4, 2, 3, 11, 22, 99, 108, 389]
solution = 2
test_case = [arr, solution]
test_function(test_case)
