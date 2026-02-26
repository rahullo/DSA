class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        # Determine the new minimum
        # If min_stack is empty, the current val is the minimum
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            current_min = self.min_stack[-1]
            self.min_stack.append(min(val, current_min))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
    

minStack = MinStack()
print(minStack.push(-2))
print(minStack.push(0))
print(minStack.push(-3))
print(minStack.getMin()) # return -3
print(minStack.pop())
print(minStack.top())    # return 0
print(minStack.getMin()) # return -2