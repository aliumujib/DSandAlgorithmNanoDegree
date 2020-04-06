class Palindrome:

    @staticmethod
    def is_palindrome(word):
        # Please write your code here.
        def is_palindrome_recursive(word, start, end):
            if start == end or (start - end == 1):
                print("{} {}".format(start, end))
                return True
            else:
                if word[start] == word[end]:
                    print("retrying with{} {}".format(start, end))
                    return is_palindrome_recursive(word, start+1, end-1)
                else:
                    print("cal {} {}".format(word[start], word[end]))
                    return False
        return is_palindrome_recursive(word, 0, len(word)-1)


word = "Deleveled".lower()
print(Palindrome.is_palindrome(word))
