def _bin_search(target, array, low, high):
    mid = (low + high) // 2

    # print("{} {} {}".format(low, high, array))

    if array[mid] == target:
        return mid
    else:
        if high == mid:
            return -1
        elif array[mid] > target:
            high = mid - 1
        elif array[mid] < target:
            low = mid + 1

        return _bin_search(target, array, low, high)


def binary_search(target, array):
    return _bin_search(target, array, 0, len(array) - 1)


array = [1, 2, 3, 4, 6, 8, 9, 12, 24, 32, 33, 34, 36]
print(binary_search(24, array))

print(binary_search(40, array))
