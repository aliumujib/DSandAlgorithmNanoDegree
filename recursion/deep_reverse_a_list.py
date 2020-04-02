"""
After I spent north of 2 hours trying to solve this, I did.
Then I looked at the solution on Udacity and felt really bad and
then I looked at stackoverflow and felt even badder
But live and learn baby!

https://stackoverflow.com/questions/10859135/python-deep-reverse-in-a-list
"""


def deep_rev(left, right, arr):
    print("L:{}, R:{}, ARR:{}".format(left, right, arr))
    if left == right:
        middle = int(len(arr)/2)
        if type(arr[middle]) is list:
            deep_rev(0, len(arr[middle])-1, arr[middle])
        return arr
    elif left == len(arr) - 1:
        return arr
    elif left - right == 1:
        return arr
    else:
        if type(arr[left]) is list:
            deep_rev(0, len(arr[left])-1, arr[left])
        elif type(arr[right]) is list:
            deep_rev(0, len(arr[right])-1, arr[right])

        swap(left, right, arr)
        return deep_rev(left+1, right-1, arr)


def swap(left, right, arr):
    temp = arr[left]
    arr[left] = arr[right]
    arr[right] = temp


def deep_reverse(arr):
    return deep_rev(0, len(arr)-1, arr)
