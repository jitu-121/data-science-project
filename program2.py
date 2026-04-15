def is_palindrome(s):
    return s == "".join(reversed(s))


result = is_palindrome("madam")
print(result)