def return_longest(array1, array2):
    if(len(array1) > len(array2)):
        return array1
    elif(len(array1) == len(array2)):
        return array1
    else:
        return array2


def longest_consecutive_subsequence(input_list):
    # TODO: Write longest consecutive subsequence solution
    longest = []

    print(input_list)
    for item, index in enumerate(input_list):
        current_num = item

        current_sub_sequence = []

        while current_num in input_list:
            current_sub_sequence.insert(0, current_num)
            current_num = current_num - 1

        while current_num in input_list:
            current_sub_sequence.append(current_num)
            current_num = current_num + 1

        print("LONGEST {} CURRENT{}".format(longest, current_sub_sequence))
        longest = return_longest(longest, current_sub_sequence)

    return longest


def test_function(test_case):
    output = longest_consecutive_subsequence(test_case[0])
    if output == test_case[1]:
        print("Pass")
    else:
        print("Fail")


test_case_1 = [[5, 4, 7, 10, 1, 3, 55, 2], [1, 2, 3, 4, 5]]
test_function(test_case_1)


test_case_2 = [[2, 12, 9, 16, 10, 5, 3, 20, 25, 11, 1, 8, 6], [8, 9, 10, 11, 12]]
test_function(test_case_2)


test_case_3 = [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]
test_function(test_case_3)
