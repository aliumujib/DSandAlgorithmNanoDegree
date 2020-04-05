def last_index(arr, target):
    """
    :param: arr - input array
    :param: target - integer element
    return: int - last index of target in arr
    TODO: complete this method to find the last index of target in arr
    """
    output = last_index_rec(arr, target, 0, -1)
    return output


def last_index_rec(arr, target, index, last_occurence):
    if index == len(arr):
        return last_occurence
    else:
        #print("{}\t{}".format(last_occurence, index))
        if(arr[index] == target):
            last_occurence = index

        index = index+1
        return last_index_rec(arr, target, index, last_occurence)


def test_function(test_case):
    arr = test_case[0]
    target = test_case[1]
    solution = test_case[2]
    output = last_index(arr, target)
    if output == solution:
        print("Pass")
    else:
        print("False")


arr = [1, 2, 5, 5, 4]
target = 5
solution = 3

test_case = [arr, target, solution]
test_function(test_case)


arr = [1, 2, 5, 5, 4]
target = 7
solution = -1

test_case = [arr, target, solution]
test_function(test_case)


arr = [91, 19, 3, 8, 9]
target = 91
solution = 0

test_case = [arr, target, solution]
test_function(test_case)


arr = [1, 1, 1, 1, 1, 1]
target = 1
solution = 5

test_case = [arr, target, solution]
test_function(test_case)
