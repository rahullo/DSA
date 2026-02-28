def evalRPN(tokens):
    stack = []
        
    for token in tokens:
        if token not in {"+", "-", "*", "/"}:
            # It's a number, push to stack
            stack.append(int(token))
        else:
            # It's an operator
            b = stack.pop()
            a = stack.pop()
            
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            else:
                # Division: Truncate toward zero
                # In Python, int(a / b) handles truncation toward zero correctly
                # whereas a // b floors toward negative infinity.
                stack.append(int(a / b))
                
    return stack[0]

import operator

def evalRPN2(tokens):
    # Use the operator module for cleaner, faster function calls
    # We use a lambda for division to handle the 'truncate toward zero' rule
    ops = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": lambda a, b: int(a / b)
    }
    
    stack = []
    
    for token in tokens:
        if token in ops:
            b = stack.pop()
            a = stack.pop()
            # Lookup and call the operation in O(1)
            stack.append(ops[token](a, b))
        else:
            # Direct integer conversion
            stack.append(int(token))
                
    return stack[0]

print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))