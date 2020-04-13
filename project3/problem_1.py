def sqrt(number):
    return sqrt_min(number, 0, number)


def sqrt_min(number, low, high):
    mid = (low + high) // 2
    squared = int(mid * mid)
    if low >= high:
        return mid
    else:
        if squared >= number:
            high = mid - 1
        else:
            low = mid + 1

    return sqrt_min(number, low, high)


print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")
