class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self) -> None:
        self.top = None

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.top
        self.top = newNode
    
    def isEmpty(self):
        return self.top is None

    def pop(self):
        if self.isEmpty():
            print('List is Empty')
            return None
        
        value = self.top.data
        self.top = self.top.next
        return value
    
    def peek(self):
        if self.isEmpty():
            return 'List is Empty'
        return self.top.data
        
    def display(self):
        
        curr = self.top
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print(None, '\n')


# Example usage:
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)
stack.push(60)
stack.display()

print("Top element is:", stack.peek())

print("Popped Item", stack.pop())
stack.display()
