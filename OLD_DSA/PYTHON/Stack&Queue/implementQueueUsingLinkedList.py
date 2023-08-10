class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        if self.first == None:
           return self.last
        else:
            return self.last.data

    def enqueue(self, data):
        new_node = Node(data)
        if self.first == None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length +=1
        return self

    def dequeue(self):
        if self.first == None:
            return self.first
        temp = self.first.data
        self.first = self.first.next
        self.length -=1
        return temp

    def printQueue(self):
        curr = self.first
        while curr != None:
            print(curr.data)
            curr = curr.next

    def peek(self):
        if self.first == None:
            return self.first
        else:
            return self.first.val

    

qu = Queue()
print(qu.peek())
print('\n')
qu.enqueue(3)
qu.enqueue(4)
qu.enqueue(5)
qu.enqueue(6)
qu.enqueue(7)
qu.printQueue()
print('\n')
print(qu.dequeue())
print('\n')
qu.printQueue()
print('\n')
print(qu.dequeue())
print('\n')
print(qu.dequeue())
print('\n')
print(qu.dequeue())
print('\n')
print(qu.dequeue())
print('\n')
print(qu.dequeue())