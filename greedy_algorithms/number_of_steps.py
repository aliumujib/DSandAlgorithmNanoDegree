# Your solution
def find_no_of_steps(number, target):
    if ((number * 2)) + 1 == target:
        print("{} * 2 and plus 1  to make {}".format(number, (number * 2) + 1))
        return 2
    elif number * 2 == target:
        print("{} * 2 make {}".format(number, number * 2))
        return 1


def min_operations(target):
    """
    Return number of steps taken to reach a target number
    input: target number (as an integer)
    output: number of steps (as an integer)
    """
    result = 1

    set_of_ops = __make_set__(target, set())
    set_of_ops = sorted(set_of_ops)
    print(set_of_ops)
    for index, number in enumerate(set_of_ops):
        if index == len(set_of_ops) - 1:
            result = result + find_no_of_steps(number, target)
        else:
            result = result + find_no_of_steps(number, set_of_ops[index + 1])

    return result


def __make_set__(number, set_of_intermediates):
    if number <= 1:
        return set_of_intermediates
    else:
        intermediate = number // 2
        set_of_intermediates.add(intermediate)
        return __make_set__(intermediate, set_of_intermediates)


print(min_operations(69))
print(min_operations(63))


# Udacity's Solution
def min_operations_ud(target):
    """
    Return number of steps taken to reach a target number
    input:- target number an integer
    output:- number of steps an integer
    """
    num_steps = 0

    # start backwards from the target
    # if target is odd --> subtract 1
    # if target is even --> divide by 2
    while target != 0:
        if target % 2 == 0:
            target = target // 2

        else:
            target = target - 1
        num_steps += 1
    return num_steps


print(min_operations_ud(69))
print(min_operations_ud(63))
