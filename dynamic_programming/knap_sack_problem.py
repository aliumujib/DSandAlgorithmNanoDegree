# 12433329


def init_array(number_of_items, max_weight):
    look_up_table = []
    for item in range(number_of_items + 1):
        item_count_row = []
        for weight in range(max_weight + 1):
            if weight == 0:
                item_count_row.append(0)
            elif item == 0:
                item_count_row.append(0)
            else:
                item_count_row.append(None)
        look_up_table.append(item_count_row)
    return look_up_table


def knap_sack(weights, values, capacity):
    if weights is None or values is None or capacity < 0:
        print("Ode ni yin sir")
        return

    loop_up_table = init_array(len(weights), capacity)

    for index in range(1, len(weights) + 1):
        current_weight = weights[index - 1]
        current_value = values[index - 1]

        for knap_sack_size in range(1, capacity + 1):
            loop_up_table[index][knap_sack_size] = loop_up_table[index - 1][knap_sack_size]

            if knap_sack_size > current_weight and (
                    loop_up_table[index - 1][knap_sack_size - current_weight] + current_value) > loop_up_table[index][
                knap_sack_size]:
                loop_up_table[index][knap_sack_size] = loop_up_table[index - 1][
                                                           knap_sack_size - current_weight] + current_value

    return loop_up_table, loop_up_table[-1][-1]


#def find_optimal_items(look_up_table):

data = knap_sack([3, 1, 3, 4, 2], [2, 2, 4, 5, 3], 7)
for row in data[0]:
    print(row)

print(data[1])
