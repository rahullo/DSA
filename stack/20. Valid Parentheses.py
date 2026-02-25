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


def isValid2(s):
    # Map of closing to opening brackets
    bracket_map = {
        ")": "(",
        "}": "{",
        "]": "["
    }
    
    stack = []

    for char in s:
        # If the character is a closing bracket
        if char in bracket_map:
            # Pop the top element if stack isn't empty, else use a dummy value
            top_element = stack.pop() if stack else '#'
            
            # Check if the popped bracket matches the required opener
            if bracket_map[char] != top_element:
                return False
        else:
            # It's an opening bracket, push it onto the stack
            stack.append(char)

    # If the stack is empty, all brackets were matched correctly
    return not stack

print(isValid2('()[]{}'))