def min_platforms(arrival, departure):
    """
    Better approach that uses the merge format of merge sort to solve problem.
    https://www.geeksforgeeks.org/minimum-number-platforms-required-railwaybus-station/
    TODO: Revisit.

    :param: arrival - list of arrival time
    :param: departure - list of departure time
    TODO - complete this method and return the minimum number of platforms (int) required
    so that no train has to wait for other(s) to leave
    """
    platforms = [departure[0]]

    for train_time_index, arrival_time in enumerate(arrival[1:]):
        plat_len = len(platforms) - 1
        for plat_index, platform in enumerate(platforms):
            if arrival_time >= platform:
                platforms[plat_index] = departure[train_time_index + 1]
                break
            elif plat_index == plat_len:
                platforms.append(departure[train_time_index + 1])
                continue

    return len(platforms)


def test_function(test_case):
    arrival = test_case[0]
    departure = test_case[1]
    solution = test_case[2]

    output = min_platforms(arrival, departure)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


arrival = [900, 940, 950, 1100, 1500, 1800]
departure = [910, 1200, 1120, 1130, 1900, 2000]
test_case = [arrival, departure, 3]

test_function(test_case)

arrival = [200, 210, 300, 320, 350, 500]
departure = [230, 340, 320, 430, 400, 520]
test_case = [arrival, departure, 2]
test_function(test_case)
