def isValid(s):
    stack = []
    dic = {
        '(':')',
        '[': ']',
        '{': '}'
    }

    print('Stack: ', stack)
    for char in s:
        if char in dic.keys():
            stack.append(dic[char])
        elif not stack or stack[-1]!=char:
            return False
        else:
            stack.pop()
        print('Stack: ', stack)
        

    return len(stack) == 0

print(isValid('()[)]{}'))