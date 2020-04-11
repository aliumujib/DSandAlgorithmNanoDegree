items = [8, 3, 1, 7, 0, 10, 2]


def quick_sort_recursive(array, left_index, pivot_index):
    while left_index != pivot_index:

        if array[left_index] <= array[pivot_index]:
            left_index = left_index + 1
            continue

        print("{} {}".format(left_index, pivot_index))
        temp = array[left_index]
        array[left_index] = array[pivot_index - 1]
        array[pivot_index - 1] = array[pivot_index]
        array[pivot_index] = temp
        pivot_index = pivot_index - 1

        print(array)

    return pivot_index


def sort_all(array, begin_index, end_index):
    if end_index <= begin_index:
        return

    pivot_index = quick_sort_recursive(array, begin_index, end_index)
    sort_all(array, begin_index, pivot_index - 1)
    sort_all(array, pivot_index + 1, end_index)


def quicksort(items):
     sort_all(items, 0, len(items) - 1)


print(quicksort(items))
