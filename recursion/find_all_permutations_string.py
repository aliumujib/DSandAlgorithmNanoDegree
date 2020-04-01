def swap_characters(string, left, right):
    char_array = list(string)
    temp = char_array[left]
    char_array[left] = char_array[right]
    char_array[right] = temp
    return "".join(char_array)


def calculate_permutations(results, string, start, end):
    if start >= end:
        print(string)
        results.append(string)
    else:
        for index in range(start, end):
            # print(index)
            swapped = swap_characters(string, start, index)
            calculate_permutations(results, swapped, start + 1, end)


def permutations(string):
    """
    :param: input string
    Return - list of all permutations of the input string
    TODO: complete this function to return a list of all permutations of the string
    """
    results = []
    calculate_permutations(results, string, 0, len(string))
    print(results)
    return results
