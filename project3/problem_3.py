def merge(left, right, output, left_idx, right_idx):
    if left_idx < len(left) and right_idx < len(right):
        if left[left_idx] > right[right_idx]:
            output.append(left[left_idx])
            left_idx = left_idx + 1
        else:
            output.append(right[right_idx])
            right_idx = right_idx + 1

        return merge(left, right, output, left_idx, right_idx)
    else:
        output += left[left_idx:]
        output += right[right_idx:]
        return output


def merge_sort(input_list):
    if len(input_list) <= 1:
        return input_list

    mid = len(input_list) // 2

    left = input_list[:mid]
    right = input_list[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    data = merge(left, right, [], 0, 0)
    return data


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """

    data = merge_sort(input_list)

    number1 = "0"
    number2 = "0"

    for index, number in enumerate(data):
        if index == 0:
            number1 = "{}{}".format(number1, number)
        elif index % 2 == 0:
            number1 = "{}{}".format(number1, number)
        else:
            number2 = "{}{}".format(number2, number)

    return [int(number1), int(number2)]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])

test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)

test_case_2 = [[6, 7, 2, 5, 9, 8], [975, 862]]
test_function(test_case_2)

