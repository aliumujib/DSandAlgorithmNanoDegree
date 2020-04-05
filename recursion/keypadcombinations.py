#["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
def get_characters(num):
    if num == 2:
        return "abc"
    elif num == 3:
        return "def"
    elif num == 4:
        return "ghi"
    elif num == 5:
        return "jkl"
    elif num == 6:
        return "mno"
    elif num == 7:
        return "pqrs"
    elif num == 8:
        return "tuv"
    elif num == 9:
        return "wxyz"
    else:
        return ""


def keypad(num):
    res = list()
    # TODO: Write your keypad solution here!
    if num == 0:
        return [""]
    elif 1 < num < 10:
        return list(get_characters(num))
    else:
        big_digit = int(num/10)
        remainder = num % 10
        chars_first = keypad(big_digit)
        chars_reminder = keypad(remainder)
        for each in chars_first:
            for permute in chars_reminder:
                res.append("{}{}".format(each, permute))

        print(res)
        return res
