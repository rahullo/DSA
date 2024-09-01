def isPalindrome(s):
    new = ''
    for char in s:
        if char.isalpha() or char.isdigit():
            new += char.lower()
    return (new == new[::-1])

def is_palindrome(s):
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        if left < right and s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True

print(is_palindrome('0P'))
