import copy


def swap_items(array, left, right):
    print("SWAPPING INDEX {} WITH INDEX {}".format(left, right))
    temp = array[left]
    array[left] = array[right]
    array[right] = temp
    return array.copy()


def calculate_permutation(array, results, start, end):
    if start >= end:
        results.append(array.copy())
    else:
        for value in range(start, end):
            swapped = swap_items(array, start, value) swap chracters for the current index in the array
            calculate_permutation(swapped, results, start+1, end)  recursively go to the next character


def permute(list_of_items):
    """
    Return a list of permutations

    Examples:
       permute([0, 1]) returns [ [0, 1], [1, 0] ]

    Args:
      l(list): list of items to be permuted

    Returns:
      list of permutation with each permuted item being represented by a list


      https://www.youtube.com/watch?v=IPWmrjE1_MU
      https://www.youtube.com/watch?v=TnZHaH9i6-0
    """
    results = []
    calculate_permutation(list_of_items, results, 0, len(list_of_items))
    print(results)
    return results
