import timeit

def fibonacci_number_recursive(number):
    if number <= 1:
        return number
    else:
        number1 = fibonacci_number_recursive(number - 1)
        number2 = fibonacci_number_recursive(number - 2)
        return number1 + number2


def fibonacci_number_dynamic_programming(number, lookup):
    if number <= 1:
        return number
    else:
        if number not in lookup:
            number1 = fibonacci_number_dynamic_programming(number - 1, lookup)
            number2 = fibonacci_number_dynamic_programming(number - 2, lookup)
            lookup[number] = number1 + number2

        return lookup[number]


start1 = timeit.timeit()
print(fibonacci_number_recursive(35))
end1 = timeit.timeit()
print("RECURSIVE: {}".format(end1 - start1))

map = {}
start2 = timeit.timeit()
print(fibonacci_number_dynamic_programming(35, map))
end2 = timeit.timeit()
print("DYNAMIC: {}".format(end2 - start2))
print(map)