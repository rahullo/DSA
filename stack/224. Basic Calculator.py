def calculate(s):
    stack = []
    res = 0
    num = 0
    sign = 1
    
    for c in s:
        if '0' <= c <= '9':
            num = num * 10 + (ord(c) - 48)
        elif c in '+-':
            res += sign * num
            num = 0
            sign = 1 if c == '+' else -1
        elif c == '(':
            stack.append(res)
            stack.append(sign)
            res = 0
            sign = 1
        elif c == ')':
            res += sign * num
            num = 0
            res *= stack.pop()      # previous sign
            res += stack.pop()      # previous result
    
    return res + sign * num

# print(calculate("1 + 1"))
print(calculate("(1+(4+5+2)-3)+(6+8)"))