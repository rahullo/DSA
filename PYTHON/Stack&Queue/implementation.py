class Node:
    def __init__(self, data = 0):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.bottom = self.top

    def insert(self, val):
        new_node = Node(val)
        if self.top == None:
            self.top = new_node
            self.bottom = self.top
        else:
            self.bottom.next = new_node
            self.bottom = new_node

    def peek(self):
        if self.top ==None:
            return self.bottom
        else:
            return self.bottom.data

    def pop(self):
        curr = self.top
        if self.top ==None:
            return "Stack is Empty"
        else:
            while curr.next.next != None:
                curr = curr.next
            
            temp = curr.next.data
            curr.next = None
            return temp

    def printList(self):
        curr = self.top
        while curr != None:
            print(curr.data, end=' ')
            curr = curr.next
    
    # def pop(self):




st = Stack()
# print(st.peek())
st.insert(3)
st.insert(4)
st.insert(5)
st.insert(6)
st.insert(7)
# print(st.peek())
st.printList()
# print('\n')
# print(st.pop())
# print('\n')
# st.printList()


