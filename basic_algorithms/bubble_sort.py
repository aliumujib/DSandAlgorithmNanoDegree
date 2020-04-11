wakeup_times = [16, 49, 3, 12, 56, 49, 55, 22, 13, 46, 19, 55, 46, 13, 25, 56, 9, 48, 45]


def bubble_sort_1(l):
    for index in reversed(range(1, len(l) - 1)):
        for inner_index in range(0, len(l) - 1):
            if l[inner_index] > l[inner_index + 1]:
                temp = l[inner_index + 1]
                l[inner_index + 1] = l[inner_index]
                l[inner_index] = temp

    print(l)


bubble_sort_1(wakeup_times)
print("Pass" if (wakeup_times[0] == 3) else "Fail")

# Entries are (h, m) where h is the hour and m is the minute
sleep_times = [(24, 13), (21, 55), (23, 20), (22, 5), (24, 23), (21, 58), (24, 3)]


def compare_times(time1, time2):
    """
    Compares two tuples and returns:
    1 if the first is greater than the second
    -1 if the first is less than the second
    0 if they are equal
    """
    if time1[0] > time2[0]:
        return 1
    elif time1[0] < time2[0]:
        return -1
    else:
        if time1[1] > time2[1]:
            return 1
        elif time1[1] < time2[1]:
            return -1
        else:
            return 0


def bubble_sort_2(l):
    # TODO: Implement bubble sort solution
    for index in reversed(range(1, len(sleep_times) - 1)):
        for inner_index in range(0, len(sleep_times) - 1):
            comparison_val = compare_times(l[inner_index], l[inner_index + 1])
            if comparison_val == -1:
                temp = l[inner_index + 1]
                l[inner_index + 1] = l[inner_index]
                l[inner_index] = temp

    print(l)


bubble_sort_2(sleep_times)
print("Pass" if (sleep_times == [(24, 23), (24, 13), (24, 3), (23, 20), (22, 5), (21, 58), (21, 55)]) else "Fail")